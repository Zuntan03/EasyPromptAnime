import os
import tkinter as tk
from const import Path, ControlNetType
from log import Log


class ControlNetController:
    def __init__(self, form, model):
        self.form = form
        self.model = model
        mGenerate = self.model.generate
        vControlNet = self.form.controlNet

        mGenerate.bind("controlNetDir", vControlNet.varControlNetDir)
        mGenerate.bind("controlNetLoop", vControlNet.varControlNetLoop)

        for cnType in ControlNetType:
            mGenerate.bind(
                f"cnEnable_{cnType.name}",
                getattr(vControlNet, f"varEnable_{cnType.name}"),
            )
            mGenerate.bind(
                f"cnUsePreprocessor_{cnType.name}",
                getattr(vControlNet, f"varUsePreprocessor_{cnType.name}"),
            )
            mGenerate.bind(
                f"cnGuessMode_{cnType.name}",
                getattr(vControlNet, f"varGuessMode_{cnType.name}"),
            )
            mGenerate.bind(
                f"cnScale_{cnType.name}",
                getattr(vControlNet, f"varScale_{cnType.name}"),
            )
            mGenerate.bind(
                f"cnScaleList_{cnType.name}",
                getattr(vControlNet, f"varScaleList_{cnType.name}"),
            )
            mGenerate.bind(
                f"cnStart_{cnType.name}",
                getattr(vControlNet, f"varStart_{cnType.name}"),
            )
            mGenerate.bind(
                f"cnEnd_{cnType.name}",
                getattr(vControlNet, f"varEnd_{cnType.name}"),
            )

    def initEvents(self):
        mGenerate = self.model.generate
        mGenerate.subsc("controlNetDir", self.selectControlNetDir)
        for cnType in ControlNetType:
            mGenerate.subsc(
                f"cnEnable_{cnType.name}",
                lambda *args, name=cnType.name: self.updateEnable(name, args[2]),
            )

    def selectControlNetDir(self, *args):
        basePath = os.path.join(Path.controlNet, args[2])
        for cnType in ControlNetType:
            os.makedirs(
                os.path.join(basePath, f"controlnet_{cnType.name}"), exist_ok=True
            )

    def updateEnable(self, name, isEnabled):
        vControlNet = self.form.controlNet
        frm = getattr(vControlNet, f"frm_{name}")
        vControlNet.ntb.tab(frm, text="* " + name if isEnabled else name)
