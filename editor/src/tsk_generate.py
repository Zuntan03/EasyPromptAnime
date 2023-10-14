import os, copy, shutil, subprocess
from const import Path
from l10n import L10n
from log import Log
from tsk_command_prompt import CommandPromptTask
from prompt_travel import PromptTravel


class GenerateTask(CommandPromptTask):
    @classmethod
    def generate(cls, model):
        gen = model.generate
        config = PromptTravel.getConfig(
            gen, gen.model, gen.upscaleStrength, model.prompt.prompts, 10
        )
        configSuffix = PromptTravel.GetConfigFileSuffix(
            gen.length,
            gen.context,
            gen.width,
            gen.height,
            gen.useHalfVae,
            gen.useXFormers,
            gen.upscaleUseHalfVae,
            gen.upscaleUseXFormers,
            gen.upscale1Enabled,
            gen.upscale1Mode,
            gen.getUpscale1Height(),
            gen.upscale2Enabled,
            gen.upscale2Mode,
            gen.getUpscale2Height(),
        )
        configSuffix = configSuffix + "-D3"
        task = GenerateTask(model.editor, "generate_anime", config, configSuffix)
        cls.enqueue(task)

    @classmethod
    def seedGacha(cls, model):
        gen = model.generate
        config = PromptTravel.getConfig(
            gen, gen.model, gen.upscaleStrength, model.prompt.prompts, 10
        )
        configSuffix = PromptTravel.GetConfigFileSuffix(
            gen.length,
            gen.context,
            gen.width,
            gen.height,
            gen.useHalfVae,
            gen.useXFormers,
            gen.upscaleUseHalfVae,
            gen.upscaleUseXFormers,
            gen.upscale1Enabled,
            gen.upscale1Mode,
            (int)(gen.height * 1.5),
        )
        task = GenerateTask(model.editor, "seed_gacha", config, configSuffix)
        cls.enqueue(task)

    @classmethod
    def preview(cls, model):
        halfFps = False  # Not good

        edt = model.editor
        start = edt.previewStart
        length = model.getPreviewLength()
        end = model.getPreviewEnd()
        prompts = copy.deepcopy(model.prompt.prompts)
        promptMap = prompts["prompt_map"]

        removeKeys = []
        for keyFrame in promptMap.keys():
            if keyFrame < start or keyFrame > end:
                removeKeys.append(keyFrame)
        for keyFrame in removeKeys:
            del promptMap[keyFrame]

        for keyFrame in sorted(promptMap.keys()):
            prompt = promptMap.pop(keyFrame)
            frame = keyFrame - start
            frame = (int)(frame * 0.5) if halfFps else frame
            promptMap[frame] = prompt

        gen = model.generate
        config = PromptTravel.getConfig(
            gen, gen.model, gen.upscaleStrength, prompts, 5 if halfFps else 10
        )
        configSuffix = PromptTravel.GetConfigFileSuffix(
            (int)(length * 0.5) if halfFps else length,
            (int)(gen.context * 0.5)
            if halfFps
            else gen.context,  # halfFps & gen.context Not good
            gen.width,
            gen.height,
            gen.useHalfVae,
            gen.useXFormers,
            gen.upscaleUseHalfVae,
            gen.upscaleUseXFormers,
            gen.upscale1Enabled and edt.previewUpscale,
            gen.upscale1Mode,
            (int)(gen.height * 1.5),
        )
        configSuffix = (configSuffix + "-U5") if halfFps else configSuffix
        task = GenerateTask(model.editor, "preview", config, configSuffix)
        cls.enqueue(task)

    # コンストラクタ
    def __init__(self, editor, taskMode, config, configSuffix):
        super().__init__(editor, taskMode)
        self.config = config
        self.configSuffix = configSuffix

    def resetState(self):
        super().resetState()
        self.configName = ""
        self.configPath = ""

    def createCommand(self):
        self.configName = f"{self.timeStr}{self.configSuffix}.json"
        self.configPath = os.path.join(self.tempDir, self.configName)
        with open(self.configPath, "w", encoding="utf-8") as f:
            f.write(self.config)
        return f"Generate.bat {self.configPath}"

    def postProcess(self):
        latestTime = 0
        latestMp4FileName = ""
        latestMp4Path = ""

        for root, dirs, files in os.walk(self.tempDir):
            for file in files:
                if file.endswith(".mp4"):
                    path = os.path.join(root, file)
                    time = os.path.getmtime(path)
                    if time > latestTime:
                        latestTime = time
                        latestMp4FileName = file
                        latestMp4Path = path

        outputDir = os.path.join(Path.output, Path.getYYYYMMDD())
        os.makedirs(outputDir, exist_ok=True)
        outputPath = os.path.join(outputDir, latestMp4FileName)
        shutil.copy(latestMp4Path, outputPath)

        seed = ""
        tokens = latestMp4FileName.split("-", 2)
        if len(tokens) == 3:
            seed = tokens[1]
        seed = seed.split("_", 1)[0]

        subprocess.Popen(f"{self.editor.ffplayCmd} {outputPath}", shell=True)
        Log.user(L10n.format("log_ffplay", seed))
