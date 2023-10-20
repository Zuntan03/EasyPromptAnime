import os, time
from const import Path
from config import Config
from l10n import L10n
from log import Log
from ui import Form
from model import Model
from controller import Controller
from task import Task

initStartTime = time.perf_counter()

Config.load(
    Path.ini,
    ["default", "default_controlnet", "ui", "ui_color", "ui_preview", "ui_size"],
)

L10n.loadConfig()


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


editor = EasyPromptAnimeEditor()

Log.user(L10n.format("log_initialization_end", time.perf_counter() - initStartTime))
Log.user(L10n.get("log_see_prompt_help"))

editor.form.run()
