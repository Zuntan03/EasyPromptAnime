import os, subprocess, shutil
import tkinter as tk
from tkinter import filedialog
from const import Path, ControlNetType
from log import Log
from l10n import L10n


class ControlNetController:
    def __init__(self, form, model):
        self.form = form
        self.model = model
        vControlNet = self.form.controlNet

        mGenerate = self.model.generate
        mGenerate.bind("controlNetDir", vControlNet.varControlNetDir)
        mGenerate.bind("controlNetLoop", vControlNet.varControlNetLoop)

        mEditor = self.model.editor
        mEditor.bind("importSpeed", vControlNet.varImportSpeed)
        mEditor.bind("importStart", vControlNet.varImportStart)
        mEditor.bind("importLength", vControlNet.varImportLength)
        mEditor.bind("importIndex", vControlNet.varImportIndex)

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

        vControlNet = self.form.controlNet
        vControlNet.btnImport.configure(command=self.importMovie)

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

    def importMovie(self):
        srcPath = filedialog.askopenfilename(
            title=L10n.get("dlg_control_net_import"), filetypes=[("MP4", "*.mp4")]
        )
        mEditor = self.model.editor
        speed = mEditor.importSpeed
        start = mEditor.importStart
        length = mEditor.importLength
        index = mEditor.importIndex
        basePath = os.path.join(Path.controlNet, self.model.generate.controlNetDir)

        cmd = ["ffmpeg", "-i", srcPath]
        vf = "fps=10,scale='if(gt(a,1),-1,512)':'if(gt(a,1),512,-1)'"
        if speed != "":
            vf = f"setpts=PTS/{speed},{vf}"
        cmd += ["-vf", vf]
        if start != "":
            cmd += ["-ss", start]
        if length != "":
            cmd += ["-t", length]
        if index != "":
            cmd += ["-start_number", index]
        outDir = os.path.join(basePath, f"controlnet_canny") + os.path.sep
        cmd += [f"{outDir}%08d.png"]

        Log.system(cmd)
        result = subprocess.run(cmd, shell=True)
        if result.returncode != 0:
            return
        for cnType in ControlNetType:
            if cnType == ControlNetType.canny:
                continue
            shutil.copytree(
                os.path.join(basePath, f"controlnet_canny"),
                os.path.join(basePath, f"controlnet_{cnType.name}"),
                dirs_exist_ok=True,
            )
