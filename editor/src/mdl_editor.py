from config import Config
from mdl_notifier import Notifier


class Editor(Notifier):
    defPreviewUpscale = True
    # defPreviewInterpolation = True
    defPreviewStart = 0
    defPreviewLength = 0

    defPreviewShowKeyframe = True
    defPreviewShowHeaderFooter = True
    defPreviewShowAnime = True

    defTaskForever = False
    defTaskPauseByError = True

    defFfplayCmd = "ffplay.exe -left 160 -top 80 -loop 5 -autoexit -loglevel error"

    def __init__(self):
        super().__init__()

        # self.savePath = ""

        self.previewUpscale = Editor.defPreviewUpscale
        # self.previewInterpolation = Editor.defPreviewInterpolation
        self.previewStart = Editor.defPreviewStart
        self.previewLength = Editor.defPreviewLength

        self.previewShowKeyframe = Editor.defPreviewShowKeyframe
        self.previewShowHeaderFooter = Editor.defPreviewShowHeaderFooter
        self.previewShowAnime = Editor.defPreviewShowAnime

        self.taskForever = Editor.defTaskForever
        self.taskPauseByError = Editor.defTaskPauseByError

        self.ffplayCmd = Editor.defFfplayCmd

    @classmethod
    def loadConfig(cls):
        Editor.defPreviewUpscale = Config.getBool(
            "ui_preview", "upscale", Editor.defPreviewUpscale
        )
        # Editor.defPreviewInterpolation = Config.getBool(
        #     "ui_preview", "interpolation", Editor.defPreviewInterpolation
        # )
        Editor.defPreviewStart = Config.getInt(
            "ui_preview", "start", Editor.defPreviewStart
        )
        Editor.defPreviewLength = Config.getInt(
            "ui_preview", "length", Editor.defPreviewLength
        )

        Editor.defPreviewShowKeyframe = Config.getBool(
            "ui_preview", "show_keyframe", Editor.defPreviewShowKeyframe
        )
        Editor.defPreviewShowHeaderFooter = Config.getBool(
            "ui_preview", "show_header_footer", Editor.defPreviewShowHeaderFooter
        )
        Editor.defPreviewShowAnime = Config.getBool(
            "ui_preview", "show_anime", Editor.defPreviewShowAnime
        )

        Editor.defTaskForever = Config.getBool("ui", "forever", Editor.defTaskForever)
        Editor.defTaskPauseByError = Config.getBool(
            "ui", "pause_by_error", Editor.defTaskPauseByError
        )

        Editor.defFfplayCmd = Config.get("ui", "ffplay_cmd", Editor.defFfplayCmd)

    def updateConfig(self):
        Editor.defPreviewUpscale = self.previewUpscale
        # Editor.defPreviewInterpolation = self.previewInterpolation
        Editor.defPreviewStart = self.previewStart
        Editor.defPreviewLength = self.previewLength

        Editor.defPreviewShowKeyframe = self.previewShowKeyframe
        Editor.defPreviewShowHeaderFooter = self.previewShowHeaderFooter
        Editor.defPreviewShowAnime = self.previewShowAnime

        Editor.defTaskForever = self.taskForever
        Editor.defTaskPauseByError = self.taskPauseByError

        # Editor.defFfplayCmd = self.ffplayCmd

    def storeConfig(self):
        Config.set("ui_preview", "upscale", Editor.defPreviewUpscale)
        # Config.set("ui_preview", "interpolation", Editor.defPreviewInterpolation)
        Config.set("ui_preview", "start", Editor.defPreviewStart)
        Config.set("ui_preview", "length", Editor.defPreviewLength)

        Config.set("ui_preview", "show_keyframe", Editor.defPreviewShowKeyframe)
        Config.set(
            "ui_preview", "show_header_footer", Editor.defPreviewShowHeaderFooter
        )
        Config.set("ui_preview", "show_anime", Editor.defPreviewShowAnime)

        Config.set("ui", "forever", Editor.defTaskForever)
        Config.set("ui", "pause_by_error", Editor.defTaskPauseByError)

        Config.set("ui", "ffplay_cmd", Editor.defFfplayCmd)
