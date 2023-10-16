import os, glob, shutil, subprocess
from const import Const, Path
from l10n import L10n
from log import Log
from tsk_command_prompt import CommandPromptTask
from prompt_travel import PromptTravel


class UpscaleTask(CommandPromptTask):
    @classmethod
    def upscaleWithConfigOverride(cls, model, upscaleDir):
        gen = model.generate
        config = PromptTravel.getConfig(
            gen, gen.model, gen.upscaleStrength, model.prompt.data, 10
        )
        cls.upscale(model, upscaleDir, config)

    @classmethod
    def upscale(cls, model, upscaleDir, config=None):
        gen = model.generate
        task = UpscaleTask(
            model.editor,
            "upscale",
            upscaleDir,
            gen.upscale1Mode,
            gen.getUpscale1Height(),
            gen.context,
            gen.upscaleUseHalfVae,
            gen.upscaleUseXFormers,
            config,
        )
        cls.enqueue(task)

    def __init__(
        self,
        editor,
        taskMode,
        upscaleDir,
        mode,
        height,
        context,
        useHalfVae,
        useXFormers,
        config,
    ):
        super().__init__(editor, taskMode)
        self.upscaleDir = upscaleDir
        self.mode = mode
        self.height = height
        self.context = context
        self.useHalfVae = useHalfVae
        self.useXFormers = useXFormers
        self.config = config

    def resetState(self):
        super().resetState()
        self.configName = ""
        self.configPath = ""

    def createCommand(self):
        cmd = os.path.join("editor", "bat", self.mode + ".bat")
        cmd = f"{cmd} -H {self.height}"
        if self.mode == Const.refine:
            cmd += f" -C {(int)(self.context / 2)}"
        if self.useHalfVae:
            cmd += " --half-vae"
        if self.useXFormers:
            cmd += " --xformers"

        if self.config is not None:
            self.configName = f"{self.timeStr}.json"
            configDir = os.path.abspath(os.path.join(self.upscaleDir, os.pardir))
            self.configPath = os.path.join(configDir, self.configName)
            with open(self.configPath, "w", encoding="utf-8") as f:
                f.write(self.config)
            cmd += f" -c {self.configPath}"  # dont ""
        cmd += f" {self.upscaleDir}"  # dont ""
        return cmd

    def postProcess(self):
        outputDir = ""
        if self.mode == Const.tile:
            outputDir = self.findNewDir(Path.promptTravelUpscaled)
        elif self.mode == Const.refine:
            outputDir = self.findNewDir(Path.promptTravelRefined)
            if outputDir is not None:
                outputDir = self.findNewDir(outputDir)
        if outputDir is None:
            return
        mp4Paths = glob.glob(os.path.join(outputDir, "*.mp4"))
        if len(mp4Paths) == 0:
            return
        mp4Path = max(mp4Paths, key=os.path.getmtime)
        mp4Name = os.path.basename(mp4Path)

        outputDir = os.path.join(Path.output, Path.getYYYYMMDD())
        os.makedirs(outputDir, exist_ok=True)
        outputPath = os.path.join(outputDir, mp4Name)
        shutil.copy(mp4Path, outputPath)

        seed = ""
        tokens = mp4Name.split(r"[_-]", 2)
        if len(tokens) == 3:
            seed = tokens[1]

        subprocess.Popen(f"{self.editor.ffplayCmd} {outputPath}", shell=True)
        Log.user(L10n.format("log_ffplay", seed))

    def findNewDir(self, dirPath):
        subDirs = [
            os.path.join(dirPath, name)
            for name in os.listdir(dirPath)
            if os.path.isdir(os.path.join(dirPath, name))
        ]
        newDir = max(subDirs, key=lambda x: os.path.getmtime(x), default=None)  # None
        return newDir
