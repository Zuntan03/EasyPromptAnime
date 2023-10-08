import os, subprocess
import tkinter as tk
from tkinter import filedialog
from const import Path
from l10n import L10n
from log import Log


class MenuController:
    def __init__(self, form, model):
        self.form = form
        self.model = model

    def initEvents(self):
        self.initFileEvents()
        self.initFolderEvents()
        self.initToolEvents()
        self.initHelpEvents()

    def initFileEvents(self):
        stf = self.form.menu.settingFileMenu
        self.openFile(stf, "m_ini_file", Path.ini)
        self.openFile(stf, "m_default_prompt_file", Path.defaultPrompt)
        self.openFile(stf, "m_prompt_travel_template_file", Path.promptTravelTemplate)

    def initFolderEvents(self):
        fld = self.form.menu.folderMenu
        self.openFolder(fld, "m_output_folder", Path.output)

        ptf = self.form.menu.promptTravelFolderMenu
        self.openFolder(ptf, "m_sd_model_folder", Path.model)
        self.openFolder(ptf, "m_motion_module_folder", Path.motionModule)
        self.openFolder(ptf, "m_lora_folder", Path.lora)
        self.openFolder(ptf, "m_embeddings_folder", Path.embeddings)
        self.openFolder(ptf, "m_wildcard_folder", Path.wildcard)

        ptof = self.form.menu.promptTravelOutputFolderMenu
        self.openFolder(
            ptof, "m_prompt_travel_generate_folder", Path.promptTravelOutput
        )
        self.openFolder(ptof, "m_prompt_travel_tile_folder", Path.promptTravelUpscaled)
        self.openFolder(ptof, "m_prompt_travel_refine_folder", Path.promptTravelRefined)

        self.openFolder(fld, "m_temp_folder", Path.tmp)
        self.openFolder(fld, "m_log_folder", Path.log)

    def initToolEvents(self):
        tool = self.form.menu.toolMenu
        tool.entryconfig(
            L10n.get("m_tool_convert_lora"), command=lambda: self.convertLora()
        )

    def convertLora(self):
        srcPath = filedialog.askopenfilename(
            title=L10n.get("dlg_convert_lora_title"),
            filetypes=[("C3Lier LoRA or LoCon LoRA", "*.safetensors")],
            initialdir=Path.lora,
        )
        srcPath = os.path.abspath(srcPath)
        modelPath = os.path.abspath(os.path.join(Path.model, self.model.generate.model))
        dim = 32
        dstPath = os.path.abspath(os.path.join(Path.lora, os.path.basename(srcPath)))
        Log.user(L10n.format("log_convert_lora", dim, srcPath, modelPath, dstPath))
        subprocess.run(
            ["start", "cmd", "/c", "ConvertLora.bat", srcPath, f"{dim}", modelPath],
            shell=True,
        )

    def initHelpEvents(self):
        hlp = self.form.menu.helpMenu
        hlp.entryconfig(
            L10n.get("m_prompt_help"),
            command=lambda: self.form.input.txtInput.insert(
                tk.END, L10n.get("hlp_prompt")
            ),
        )

        self.openUrl(hlp, "m_github", "https://github.com/Zuntan03/EasyPromptAnime")

        ref = self.form.menu.referenceMenu
        self.openUrlNoL10n(
            ref,
            "AnimateDiff prompt travel",
            "https://github.com/s9roll7/animatediff-cli-prompt-travel",
        )
        self.openUrlNoL10n(ref, "sd-scripts", "https://github.com/kohya-ss/sd-scripts")
        self.openUrlNoL10n(ref, "Codex FFmpeg", "https://github.com/GyanD/codexFFmpeg")
        self.openUrlNoL10n(
            ref, "ECCV2022-RIFE", "https://github.com/megvii-research/ECCV2022-RIFE"
        )

    def openFile(self, menu, name, path):
        menu.entryconfig(
            L10n.get(name), command=lambda: subprocess.run(["start", path], shell=True)
        )

    def openFolder(self, menu, name, path):
        menu.entryconfig(
            L10n.get(name), command=lambda: subprocess.run(["explorer", path])
        )

    def openUrl(self, menu, name, url):
        menu.entryconfig(
            L10n.get(name), command=lambda: subprocess.run(["start", url], shell=True)
        )

    def openUrlNoL10n(self, menu, name, url):
        menu.entryconfig(
            name, command=lambda: subprocess.run(["start", url], shell=True)
        )
