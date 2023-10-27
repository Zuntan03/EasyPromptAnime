import os, shutil, subprocess
import tkinter as tk
from tkinter import filedialog
from const import Path
from log import Log
from l10n import L10n
from mosaic import Mosaic


class MosaicController:
    def __init__(self, form, model):
        self.form = form
        self.model = model
        mGenerate = self.model.generate
        vMosaic = self.form.mosaic

        mGenerate.bind("mosaicEnabled", vMosaic.varMosaicEnabled)
        mGenerate.bind("mosaicThreshold", vMosaic.varMosaicThreshold)
        mGenerate.bind("temporalMosaic", vMosaic.varTemporalMosaic)
        mGenerate.bind("ellipseMosaic", vMosaic.varEllipseMosaic)
        mGenerate.bind("mosaicMaskBlur", vMosaic.varMosaicMaskBlur)
        mGenerate.bind("mosaicFemFace", vMosaic.varFemFace)
        mGenerate.bind("mosaicFemBrst", vMosaic.varFemBrst)
        mGenerate.bind("mosaicFemBrstCov", vMosaic.varFemBrstCov)
        mGenerate.bind("mosaicFemGntl", vMosaic.varFemGntl)
        mGenerate.bind("mosaicFemGntlCov", vMosaic.varFemGntlCov)
        mGenerate.bind("mosaicMaleFace", vMosaic.varMaleFace)
        mGenerate.bind("mosaicMaleBrst", vMosaic.varMaleBrst)
        mGenerate.bind("mosaicMaleGntl", vMosaic.varMaleGntl)
        mGenerate.bind("mosaicArmpit", vMosaic.varArmpit)
        mGenerate.bind("mosaicArmpitCov", vMosaic.varArmpitCov)
        mGenerate.bind("mosaicBelly", vMosaic.varBelly)
        mGenerate.bind("mosaicBellyCov", vMosaic.varBellyCov)
        mGenerate.bind("mosaicHip", vMosaic.varHip)
        mGenerate.bind("mosaicHipCov", vMosaic.varHipCov)
        mGenerate.bind("mosaicAns", vMosaic.varAns)
        mGenerate.bind("mosaicAnsCov", vMosaic.varAnsCov)
        mGenerate.bind("mosaicFeet", vMosaic.varFeet)
        mGenerate.bind("mosaicFeetCov", vMosaic.varFeetCov)
        mGenerate.bind("mosaicScaleTop", vMosaic.varMosaicScaleTop)
        mGenerate.bind("mosaicScaleBottom", vMosaic.varMosaicScaleBottom)
        mGenerate.bind("mosaicScaleLeft", vMosaic.varMosaicScaleLeft)
        mGenerate.bind("mosaicScaleRight", vMosaic.varMosaicScaleRight)
        mGenerate.bind("mosaicIgnoreTop", vMosaic.varMosaicIgnoreTop)
        mGenerate.bind("mosaicIgnoreBottom", vMosaic.varMosaicIgnoreBottom)
        mGenerate.bind("mosaicIgnoreLeft", vMosaic.varMosaicIgnoreLeft)
        mGenerate.bind("mosaicIgnoreRight", vMosaic.varMosaicIgnoreRight)

    def initEvents(self):
        self.form.mosaic.btnMosaicPngDir.configure(command=self.onMosaicPngDir)

    def onMosaicPngDir(self):
        Log.user(L10n.get("log_please_wait"))
        srcDir = filedialog.askdirectory(
            title=L10n.get("dlg_mosaic_title"), initialdir=Path.promptTravelUpscaled
        )
        if srcDir == "":
            return
        mosaicDir = Mosaic.mosaicPngDir(self.model.generate, srcDir)
        if mosaicDir == "":
            Log.system(f"[FAILED] Mosaic.mosaicPngDir()")
            return

        frames2Mp4Result = subprocess.run(["Frames2Mp4.bat", mosaicDir])
        if frames2Mp4Result.returncode != 0:
            Log.system(f"[FAILED] Frames2Mp4.bat: {frames2Mp4Result.returncode}")
            return

        fpsX6Result = subprocess.run(["FpsX6.bat", mosaicDir + ".mp4"])
        if fpsX6Result.returncode != 0:
            Log.system(f"[FAILED] FpsX6.bat: {fpsX6Result.returncode}")
            return

        outputDir = os.path.join(Path.output, Path.getYYYYMMDD())
        os.makedirs(outputDir, exist_ok=True)
        dstName = f"{Path.getYYYYMMDDHHMMSS()}{os.path.basename(mosaicDir)[2:]}.mp4"
        outputPath = os.path.join(outputDir, dstName)
        shutil.copy(mosaicDir + "-M6e.mp4", outputPath)

        subprocess.Popen(f"{self.model.editor.ffplayCmd} {outputPath}", shell=True)
