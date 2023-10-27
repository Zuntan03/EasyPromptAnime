import os, subprocess
import tkinter as tk
import tkinter.ttk as ttk
from const import Path
from l10n import L10n
from config import Config
from ui_const import UiPack


class MosaicForm:
    def __init__(self, parent):
        self.frm = ttk.Frame(parent)

        self.initControl()
        self.initMaleFemParts()
        self.initOtherParts()
        self.initMosaicScale()
        self.initMosaicIgnore()
        # mosaic list

        parent.add(self.frm, text=L10n.get("mosaic_tab"))

    def initControl(self):
        self.frmControl = ttk.Frame(self.frm)

        self.btnMosaicPngDir = ttk.Button(
            self.frmControl, text=L10n.get("mosaic_png_dir")
        )
        self.btnMosaicPngDir.pack(UiPack.btn)

        self.varMosaicEnabled = tk.BooleanVar()
        self.chkMosaicEnabled = tk.Checkbutton(
            self.frmControl,
            text=L10n.get("mosaic_enabled"),
            variable=self.varMosaicEnabled,
        )
        # self.chkMosaicEnabled.pack(UiPack.chk)

        self.lblMosaicThreshold = ttk.Label(
            self.frmControl, text=L10n.get("mosaic_threshold")
        )
        self.lblMosaicThreshold.pack(UiPack.lbl)
        self.varMosaicThreshold = tk.DoubleVar(value=0.5)
        self.sliMosaicThreshold = tk.Scale(
            self.frmControl,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=self.varMosaicThreshold,
            takefocus=True,
        )
        self.sliMosaicThreshold.pack(UiPack.sli)

        self.varTemporalMosaic = tk.BooleanVar(value=True)
        self.chkTemporalMosaic = tk.Checkbutton(
            self.frmControl,
            text=L10n.get("mosaic_temporal"),
            variable=self.varTemporalMosaic,
        )
        self.chkTemporalMosaic.pack(UiPack.chk)

        self.varEllipseMosaic = tk.BooleanVar(value=True)
        self.chkEllipseMosaic = tk.Checkbutton(
            self.frmControl,
            text=L10n.get("mosaic_ellipse"),
            variable=self.varEllipseMosaic,
        )
        self.chkEllipseMosaic.pack(UiPack.chk)

        self.lblMosaicMaskBlur = ttk.Label(
            self.frmControl, text=L10n.get("mosaic_mask_blur")
        )
        self.lblMosaicMaskBlur.pack(UiPack.lbl)
        self.varMosaicMaskBlur = tk.DoubleVar(value=0.01)
        self.sliMosaicMaskBlur = tk.Scale(
            self.frmControl,
            from_=0.0,
            to=0.1,
            resolution=0.01,
            orient=tk.HORIZONTAL,
            variable=self.varMosaicMaskBlur,
            takefocus=True,
        )
        self.sliMosaicMaskBlur.pack(UiPack.sli)

        self.frmControl.pack(UiPack.frm)

    def initMaleFemParts(self):
        self.frmMaleFemParts = ttk.Frame(self.frm)

        self.lblCovered = ttk.Label(
            self.frmMaleFemParts, text=L10n.get("mosaic_covered_info")
        )
        self.lblCovered.pack(UiPack.lbl)

        self.lblFem = ttk.Label(self.frmMaleFemParts, text=L10n.get("mosaic_fem"))
        self.lblFem.pack(UiPack.lbl)

        self.varFemFace = tk.BooleanVar()
        self.chkFemFace = tk.Checkbutton(
            self.frmMaleFemParts,
            text=L10n.get("mosaic_fem_face"),
            variable=self.varFemFace,
        )
        self.chkFemFace.pack(UiPack.chk)

        self.varFemBrst = tk.BooleanVar()
        self.chkFemBrst = tk.Checkbutton(
            self.frmMaleFemParts,
            text=L10n.get("mosaic_fem_brst"),
            variable=self.varFemBrst,
        )
        self.chkFemBrst.pack(UiPack.chk)

        self.varFemBrstCov = tk.BooleanVar()
        self.chkFemBrstCov = tk.Checkbutton(
            self.frmMaleFemParts,
            text=L10n.get("mosaic_fem_brst_cov"),
            variable=self.varFemBrstCov,
        )
        self.chkFemBrstCov.pack(UiPack.chk)

        self.varFemGntl = tk.BooleanVar(value=True)
        self.chkFemGntl = tk.Checkbutton(
            self.frmMaleFemParts,
            text=L10n.get("mosaic_fem_gntl"),
            variable=self.varFemGntl,
        )
        self.chkFemGntl.pack(UiPack.chk)

        self.varFemGntlCov = tk.BooleanVar()
        self.chkFemGntlCov = tk.Checkbutton(
            self.frmMaleFemParts,
            text=L10n.get("mosaic_fem_gntl_cov"),
            variable=self.varFemGntlCov,
        )
        self.chkFemGntlCov.pack(UiPack.chk)

        self.lblMale = ttk.Label(self.frmMaleFemParts, text=L10n.get("mosaic_male"))
        self.lblMale.pack(UiPack.lbl)

        self.varMaleFace = tk.BooleanVar()
        self.chkMaleFace = tk.Checkbutton(
            self.frmMaleFemParts,
            text=L10n.get("mosaic_male_face"),
            variable=self.varMaleFace,
        )
        self.chkMaleFace.pack(UiPack.chk)

        self.varMaleBrst = tk.BooleanVar()
        self.chkMaleBrst = tk.Checkbutton(
            self.frmMaleFemParts,
            text=L10n.get("mosaic_male_brst"),
            variable=self.varMaleBrst,
        )
        self.chkMaleBrst.pack(UiPack.chk)

        self.varMaleGntl = tk.BooleanVar(value=True)
        self.chkMaleGntl = tk.Checkbutton(
            self.frmMaleFemParts,
            text=L10n.get("mosaic_male_gntl"),
            variable=self.varMaleGntl,
        )
        self.chkMaleGntl.pack(UiPack.chk)

        self.frmMaleFemParts.pack(UiPack.frm)

    def initOtherParts(self):
        self.frmOtherParts = ttk.Frame(self.frm)

        self.varArmpit = tk.BooleanVar()
        self.chkArmpit = tk.Checkbutton(
            self.frmOtherParts, text=L10n.get("mosaic_armpit"), variable=self.varArmpit
        )
        self.chkArmpit.pack(UiPack.chk)

        self.varArmpitCov = tk.BooleanVar()
        self.chkArmpitCov = tk.Checkbutton(
            self.frmOtherParts,
            text=L10n.get("mosaic_armpit_cov"),
            variable=self.varArmpitCov,
        )
        self.chkArmpitCov.pack(UiPack.chk)

        self.varBelly = tk.BooleanVar()
        self.chkBelly = tk.Checkbutton(
            self.frmOtherParts, text=L10n.get("mosaic_belly"), variable=self.varBelly
        )
        self.chkBelly.pack(UiPack.chk)

        self.varBellyCov = tk.BooleanVar()
        self.chkBellyCov = tk.Checkbutton(
            self.frmOtherParts,
            text=L10n.get("mosaic_belly_cov"),
            variable=self.varBellyCov,
        )
        self.chkBellyCov.pack(UiPack.chk)

        self.varHip = tk.BooleanVar()
        self.chkHip = tk.Checkbutton(
            self.frmOtherParts, text=L10n.get("mosaic_hip"), variable=self.varHip
        )
        self.chkHip.pack(UiPack.chk)

        self.varHipCov = tk.BooleanVar()
        self.chkHipCov = tk.Checkbutton(
            self.frmOtherParts, text=L10n.get("mosaic_hip_cov"), variable=self.varHipCov
        )
        self.chkHipCov.pack(UiPack.chk)

        self.varAns = tk.BooleanVar()
        self.chkAns = tk.Checkbutton(
            self.frmOtherParts, text=L10n.get("mosaic_ans"), variable=self.varAns
        )
        self.chkAns.pack(UiPack.chk)

        self.varAnsCov = tk.BooleanVar()
        self.chkAnsCov = tk.Checkbutton(
            self.frmOtherParts,
            text=L10n.get("mosaic_ans_cov"),
            variable=self.varAnsCov,
        )
        self.chkAnsCov.pack(UiPack.chk)

        self.varFeet = tk.BooleanVar()
        self.chkFeet = tk.Checkbutton(
            self.frmOtherParts, text=L10n.get("mosaic_feet"), variable=self.varFeet
        )
        self.chkFeet.pack(UiPack.chk)

        self.varFeetCov = tk.BooleanVar()
        self.chkFeetCov = tk.Checkbutton(
            self.frmOtherParts,
            text=L10n.get("mosaic_feet_cov"),
            variable=self.varFeetCov,
        )
        self.chkFeetCov.pack(UiPack.chk)

        self.frmOtherParts.pack(UiPack.frm)

    def initMosaicScale(self):
        self.frmMosaicScale = ttk.Frame(self.frm)
        self.lblMosaicScale = ttk.Label(
            self.frmMosaicScale, text=L10n.get("mosaic_scale")
        )
        self.lblMosaicScale.pack(UiPack.lbl)

        self.lblMosaicScaleTop = ttk.Label(self.frmMosaicScale, text=L10n.get("top"))
        self.lblMosaicScaleTop.pack(UiPack.lbl)
        self.varMosaicScaleTop = tk.DoubleVar(value=1.0)
        self.sliMosaicScaleTop = tk.Scale(
            self.frmMosaicScale,
            from_=0.0,
            to=4.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            variable=self.varMosaicScaleTop,
            takefocus=True,
        )
        self.sliMosaicScaleTop.pack(UiPack.sli)

        self.lblMosaicScaleBottom = ttk.Label(
            self.frmMosaicScale, text=L10n.get("bottom")
        )
        self.lblMosaicScaleBottom.pack(UiPack.lbl)
        self.varMosaicScaleBottom = tk.DoubleVar(value=1.0)
        self.sliMosaicScaleBottom = tk.Scale(
            self.frmMosaicScale,
            from_=0.0,
            to=4.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            variable=self.varMosaicScaleBottom,
            takefocus=True,
        )
        self.sliMosaicScaleBottom.pack(UiPack.sli)

        self.lblMosaicScaleLeft = ttk.Label(self.frmMosaicScale, text=L10n.get("left"))
        self.lblMosaicScaleLeft.pack(UiPack.lbl)
        self.varMosaicScaleLeft = tk.DoubleVar(value=1.0)
        self.sliMosaicScaleLeft = tk.Scale(
            self.frmMosaicScale,
            from_=0.0,
            to=4.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            variable=self.varMosaicScaleLeft,
            takefocus=True,
        )
        self.sliMosaicScaleLeft.pack(UiPack.sli)

        self.lblMosaicScaleRight = ttk.Label(
            self.frmMosaicScale, text=L10n.get("right")
        )
        self.lblMosaicScaleRight.pack(UiPack.lbl)
        self.varMosaicScaleRight = tk.DoubleVar(value=1.0)
        self.sliMosaicScaleRight = tk.Scale(
            self.frmMosaicScale,
            from_=0.0,
            to=4.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            variable=self.varMosaicScaleRight,
            takefocus=True,
        )
        self.sliMosaicScaleRight.pack(UiPack.sli)

        self.frmMosaicScale.pack(UiPack.frm)

    def initMosaicIgnore(self):
        self.frmMosaicIgnore = ttk.Frame(self.frm)
        self.lblMosaicIgnore = ttk.Label(
            self.frmMosaicIgnore, text=L10n.get("mosaic_ignore")
        )
        self.lblMosaicIgnore.pack(UiPack.lbl)

        self.lblMosaicIgnoreTop = ttk.Label(self.frmMosaicIgnore, text=L10n.get("top"))
        self.lblMosaicIgnoreTop.pack(UiPack.lbl)
        self.varMosaicIgnoreTop = tk.DoubleVar(value=0.0)
        self.sliMosaicIgnoreTop = tk.Scale(
            self.frmMosaicIgnore,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=self.varMosaicIgnoreTop,
            takefocus=True,
        )
        self.sliMosaicIgnoreTop.pack(UiPack.sli)

        self.lblMosaicIgnoreBottom = ttk.Label(
            self.frmMosaicIgnore, text=L10n.get("bottom")
        )
        self.lblMosaicIgnoreBottom.pack(UiPack.lbl)
        self.varMosaicIgnoreBottom = tk.DoubleVar(value=0.0)
        self.sliMosaicIgnoreBottom = tk.Scale(
            self.frmMosaicIgnore,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=self.varMosaicIgnoreBottom,
            takefocus=True,
        )
        self.sliMosaicIgnoreBottom.pack(UiPack.sli)

        self.lblMosaicIgnoreLeft = ttk.Label(
            self.frmMosaicIgnore, text=L10n.get("left")
        )
        self.lblMosaicIgnoreLeft.pack(UiPack.lbl)
        self.varMosaicIgnoreLeft = tk.DoubleVar(value=0.0)
        self.sliMosaicIgnoreLeft = tk.Scale(
            self.frmMosaicIgnore,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=self.varMosaicIgnoreLeft,
            takefocus=True,
        )
        self.sliMosaicIgnoreLeft.pack(UiPack.sli)

        self.lblMosaicIgnoreRight = ttk.Label(
            self.frmMosaicIgnore, text=L10n.get("right")
        )
        self.lblMosaicIgnoreRight.pack(UiPack.lbl)
        self.varMosaicIgnoreRight = tk.DoubleVar(value=0.0)
        self.sliMosaicIgnoreRight = tk.Scale(
            self.frmMosaicIgnore,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=self.varMosaicIgnoreRight,
            takefocus=True,
        )
        self.sliMosaicIgnoreRight.pack(UiPack.sli)

        self.frmMosaicIgnore.pack(UiPack.frm)

    def setDarkTheme(self, colors):
        self.chkMosaicEnabled.configure(colors["chk"])
        self.sliMosaicThreshold.configure(colors["sli"])
        self.chkTemporalMosaic.configure(colors["chk"])
        self.chkEllipseMosaic.configure(colors["chk"])
        self.sliMosaicMaskBlur.configure(colors["sli"])

        self.chkMaleFace.configure(colors["chk"])
        self.chkMaleBrst.configure(colors["chk"])
        self.chkMaleGntl.configure(colors["chk"])
        self.chkFemFace.configure(colors["chk"])
        self.chkFemBrst.configure(colors["chk"])
        self.chkFemBrstCov.configure(colors["chk"])
        self.chkFemGntl.configure(colors["chk"])
        self.chkFemGntlCov.configure(colors["chk"])

        self.chkArmpit.configure(colors["chk"])
        self.chkArmpitCov.configure(colors["chk"])
        self.chkBelly.configure(colors["chk"])
        self.chkBellyCov.configure(colors["chk"])
        self.chkHip.configure(colors["chk"])
        self.chkHipCov.configure(colors["chk"])
        self.chkAns.configure(colors["chk"])
        self.chkAnsCov.configure(colors["chk"])
        self.chkFeet.configure(colors["chk"])
        self.chkFeetCov.configure(colors["chk"])

        self.sliMosaicScaleTop.configure(colors["sli"])
        self.sliMosaicScaleBottom.configure(colors["sli"])
        self.sliMosaicScaleLeft.configure(colors["sli"])
        self.sliMosaicScaleRight.configure(colors["sli"])

        self.sliMosaicIgnoreTop.configure(colors["sli"])
        self.sliMosaicIgnoreBottom.configure(colors["sli"])
        self.sliMosaicIgnoreLeft.configure(colors["sli"])
        self.sliMosaicIgnoreRight.configure(colors["sli"])
        pass
