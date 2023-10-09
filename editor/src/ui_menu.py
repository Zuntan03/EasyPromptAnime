import json
import tkinter as tk
import tkinter.ttk as ttk
from const import Path
from l10n import L10n
from ui_const import Ui, UiPack


class Menu:
    def __init__(self, parent):
        self.menuBar = tk.Menu(parent)
        parent.config(menu=self.menuBar)

        self.initFileMenu()
        self.initFolderMenu()
        self.initToolMenu()
        self.initDownloadMenu()
        self.initHelpMenu()

    def initFileMenu(self):
        self.fileMenu = tk.Menu(self.menuBar, tearoff=False)
        self.menuBar.add_cascade(label=L10n.get("m_file"), menu=self.fileMenu)

        self.settingFileMenu = tk.Menu(self.fileMenu, tearoff=False)
        self.fileMenu.add_cascade(
            label=L10n.get("m_setting_file"), menu=self.settingFileMenu
        )

        self.settingFileMenu.add_command(label=L10n.get("m_ini_file"))
        self.settingFileMenu.add_command(label=L10n.get("m_default_prompt_file"))
        self.settingFileMenu.add_command(
            label=L10n.get("m_prompt_travel_template_file")
        )

    def initFolderMenu(self):
        self.folderMenu = tk.Menu(self.menuBar, tearoff=False)
        self.menuBar.add_cascade(label=L10n.get("m_folder"), menu=self.folderMenu)

        self.folderMenu.add_command(label=L10n.get("m_output_folder"))

        self.promptTravelFolderMenu = tk.Menu(self.folderMenu, tearoff=False)
        self.folderMenu.add_cascade(
            label=L10n.get("m_prompt_travel_folder"), menu=self.promptTravelFolderMenu
        )

        self.promptTravelFolderMenu.add_command(label=L10n.get("m_sd_model_folder"))
        self.promptTravelFolderMenu.add_command(
            label=L10n.get("m_motion_module_folder")
        )
        self.promptTravelFolderMenu.add_command(label=L10n.get("m_lora_folder"))
        self.promptTravelFolderMenu.add_command(label=L10n.get("m_embeddings_folder"))
        self.promptTravelFolderMenu.add_command(label=L10n.get("m_wildcard_folder"))

        self.promptTravelOutputFolderMenu = tk.Menu(self.folderMenu, tearoff=False)
        self.folderMenu.add_cascade(
            label=L10n.get("m_prompt_travel_output_folder"),
            menu=self.promptTravelOutputFolderMenu,
        )

        self.promptTravelOutputFolderMenu.add_command(
            label=L10n.get("m_prompt_travel_generate_folder")
        )
        self.promptTravelOutputFolderMenu.add_command(
            label=L10n.get("m_prompt_travel_tile_folder")
        )
        self.promptTravelOutputFolderMenu.add_command(
            label=L10n.get("m_prompt_travel_refine_folder")
        )

        self.folderMenu.add_command(label=L10n.get("m_temp_folder"))
        self.folderMenu.add_command(label=L10n.get("m_log_folder"))

    def initToolMenu(self):
        self.toolMenu = tk.Menu(self.menuBar, tearoff=False)
        self.menuBar.add_cascade(label=L10n.get("m_tool"), menu=self.toolMenu)

        self.toolMenu.add_command(label=L10n.get("m_tool_convert_lora"))

        self.toolMenu.add_command(label=L10n.get("m_tool_easy_leco"))

    def initDownloadMenu(self):
        self.downloadMenuData = ""
        with open(Path.downloadMenu, "r", encoding="utf-8-sig") as f:
            self.downloadMenuData = json.load(f)

        self.downloadMenu = tk.Menu(self.menuBar, tearoff=False)
        self.menuBar.add_cascade(label=L10n.get("m_download"), menu=self.downloadMenu)

        def initDlMenu(category):
            dlMenu = tk.Menu(self.downloadMenu, tearoff=False)
            self.downloadMenu.add_cascade(
                label=L10n.get(f"m_dl_{category}"), menu=dlMenu
            )

            for name, data in self.downloadMenuData[category].items():
                data["menu"] = dlMenu
                data["checked"] = tk.BooleanVar(value=True)
                dlMenu.add_checkbutton(label=name, variable=data["checked"])
            return dlMenu

        self.dlModel = initDlMenu("model")
        self.dlMotionModule = initDlMenu("motion_module")
        self.dlVae = initDlMenu("vae")
        self.dlEmbedding = initDlMenu("embedding")

    def initHelpMenu(self):
        self.helpMenu = tk.Menu(self.menuBar, tearoff=False)
        self.menuBar.add_cascade(label=L10n.get("m_help"), menu=self.helpMenu)

        self.helpMenu.add_command(label=L10n.get("m_prompt_help"))

        self.helpMenu.add_command(label=L10n.get("m_github"))

        self.referenceMenu = tk.Menu(self.helpMenu, tearoff=False)
        self.helpMenu.add_cascade(
            label=L10n.get("m_reference"), menu=self.referenceMenu
        )

        self.referenceMenu.add_command(label="AnimateDiff prompt travel")
        self.referenceMenu.add_command(label="sd-scripts")
        self.referenceMenu.add_command(label="Codex FFmpeg")
        self.referenceMenu.add_command(label="ECCV2022-RIFE")
