﻿import os, time
from const import Path
from config import Config
from l10n import L10n
from log import Log
from ui import Form
from model import Model
from controller import Controller
from task import Task
from prompt_travel import PromptTravel


class EasyPromptAnimeEditor:
    def __init__(self):
        Path.cwd = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        os.chdir(Path.cwd)

        ffmpegBinPath = os.path.join(Path.cwd, "ffmpeg-master-latest-win64-gpl", "bin")
        os.environ["PATH"] = f'{ffmpegBinPath};{os.environ["PATH"]}'

        Form.loadConfig()
        self.form = Form()

        Model.loadConfig()
        self.model = Model()

        Task.initialize(self.form.win)

        self.controller = Controller(self.form, self.model)

        # TODO: Load file or default prompt
        self.model.prompt.loadDefaultPrompt()
        lastFrame = self.model.prompt.getLastPrompt()[0]
        if lastFrame > 0:
            self.model.generate.length = lastFrame + 10  # notifyAll
        self.model.notifyAll()

        self.form.win.protocol("WM_DELETE_WINDOW", self.onWinClose)
        self.form.win.after(50, self.saveConfig)
        PromptTravel.loadTemplate()

    def saveConfig(self):
        L10n.storeConfig()
        self.model.storeConfig()
        self.form.storeConfig()
        Config.save(Path.ini)

    def onWinClose(self):
        self.saveConfig()
        self.form.win.destroy()

    def run(self):
        self.form.run()


initStartTime = time.perf_counter()

Config.load(Path.ini, ["default", "ui", "ui_color", "ui_preview", "ui_size"])

L10n.load()

editor = EasyPromptAnimeEditor()

Log.user(L10n.format("log_initialization_end", time.perf_counter() - initStartTime))

editor.run()