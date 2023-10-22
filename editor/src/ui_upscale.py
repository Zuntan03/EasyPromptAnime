from const import Const
from l10n import L10n
from config import Config
from ui_const import UiPack
import tkinter as tk
import tkinter.ttk as ttk


class UpscaleForm:
    schedulerValues = Const.schedulerValues
    schedulerNames = Const.schedulerNames
    maxSteps = 60

    def __init__(self, parent):
        self.frm = ttk.Frame(parent)

        self.initSchedulerSteps()
        self.initGuidanceScaleDenoise()
        self.initTile()
        self.initHalfVaeXFormers()

        parent.add(self.frm, text=L10n.get("upscale_tab"))

    def initSchedulerSteps(self):
        self.frmSchedulerSteps = ttk.Frame(self.frm)

        self.lblScheduler = ttk.Label(
            self.frmSchedulerSteps, text=L10n.get("upscale_scheduler")
        )
        self.lblScheduler.pack(UiPack.lbl)

        self.varScheduler = tk.StringVar()
        self.cmbScheduler = ttk.Combobox(
            self.frmSchedulerSteps,
            textvariable=self.varScheduler,
            state="readonly",
            values=UpscaleForm.schedulerNames,
            width=21,
            height=23,
        )
        self.cmbScheduler.pack(UiPack.cmb)

        self.lblSteps = ttk.Label(
            self.frmSchedulerSteps, text=L10n.get("upscale_steps")
        )
        self.lblSteps.pack(UiPack.lbl)
        self.varSteps = tk.IntVar(value=15)
        self.sliSteps = tk.Scale(
            self.frmSchedulerSteps,
            from_=10,
            to=UpscaleForm.maxSteps,
            resolution=1,
            orient=tk.HORIZONTAL,
            variable=self.varSteps,
            takefocus=True,
        )
        self.sliSteps.pack(UiPack.sli)

        self.frmSchedulerSteps.pack(UiPack.frm)

    def initGuidanceScaleDenoise(self):
        self.frmDenoiseGuidanceScale = ttk.Frame(self.frm)

        self.lblGuidanceScale = ttk.Label(
            self.frmDenoiseGuidanceScale, text=L10n.get("upscale_guidance_scale")
        )
        self.lblGuidanceScale.pack(UiPack.lbl)

        self.varGuidanceScale = tk.DoubleVar(value=8.0)
        self.sliGuidanceScale = tk.Scale(
            self.frmDenoiseGuidanceScale,
            from_=1.0,
            to=30.0,
            resolution=0.5,
            orient=tk.HORIZONTAL,
            variable=self.varGuidanceScale,
            takefocus=True,
        )
        self.sliGuidanceScale.pack(UiPack.sli)

        self.lblDenoise = ttk.Label(
            self.frmDenoiseGuidanceScale, text=L10n.get("upscale_strength")
        )
        self.lblDenoise.pack(UiPack.lbl)
        self.varDenoise = tk.DoubleVar(value=0.5)
        self.sliDenoise = tk.Scale(
            self.frmDenoiseGuidanceScale,
            from_=0.0,
            to=4.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=self.varDenoise,
            takefocus=True,
        )
        self.sliDenoise.pack(UiPack.sli)

        self.frmDenoiseGuidanceScale.pack(UiPack.frm)

    def initTile(self):
        self.frmTile = ttk.Frame(self.frm)

        self.lblTileScale = ttk.Label(self.frmTile, text=L10n.get("upscale_tile_scale"))
        self.lblTileScale.pack(UiPack.lbl)
        self.varTileScale = tk.DoubleVar(value=1.0)
        self.sliTileScale = tk.Scale(
            self.frmTile,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=self.varTileScale,
            takefocus=True,
        )
        self.sliTileScale.pack(UiPack.sli)

        self.lblTileStart = ttk.Label(self.frmTile, text=L10n.get("upscale_tile_start"))
        self.lblTileStart.pack(UiPack.lbl)
        self.varTileStart = tk.DoubleVar(value=0.0)
        self.sliTileStart = tk.Scale(
            self.frmTile,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=self.varTileStart,
            takefocus=True,
        )
        self.sliTileStart.pack(UiPack.sli)

        self.lblTileEnd = ttk.Label(self.frmTile, text=L10n.get("upscale_tile_end"))
        self.lblTileEnd.pack(UiPack.lbl)
        self.varTileEnd = tk.DoubleVar(value=1.0)
        self.sliTileEnd = tk.Scale(
            self.frmTile,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=self.varTileEnd,
            takefocus=True,
        )
        self.sliTileEnd.pack(UiPack.sli)

        self.frmTile.pack(UiPack.frm)

    def initHalfVaeXFormers(self):
        self.frmHalfVaeXFormers = ttk.Frame(self.frm)

        self.varUseHalfVae = tk.BooleanVar(value=False)
        self.chkUseHalfVae = tk.Checkbutton(
            self.frmHalfVaeXFormers,
            text=L10n.get("upscale_use_half_vae"),
            variable=self.varUseHalfVae,
        )
        self.chkUseHalfVae.pack(UiPack.chk)

        self.varUseXFormers = tk.BooleanVar(value=False)
        self.chkUseXFormers = tk.Checkbutton(
            self.frmHalfVaeXFormers,
            text=L10n.get("upscale_use_x_formers"),
            variable=self.varUseXFormers,
        )
        self.chkUseXFormers.pack(UiPack.chk)

        self.frmHalfVaeXFormers.pack(UiPack.frm)

    @classmethod
    def loadConfig(self):
        values = ",".join(UpscaleForm.schedulerValues)
        values = Config.get("ui", "scheduler_values", values)
        UpscaleForm.schedulerValues = [s.strip() for s in values.split(",")]

        names = ",".join(UpscaleForm.schedulerNames)
        names = Config.get("ui", "scheduler_names", names)
        UpscaleForm.schedulerNames = [s.strip() for s in names.split(",")]

        UpscaleForm.maxSteps = Config.get("upscale", "max_steps", UpscaleForm.maxSteps)

    # def storeConfig(self): # by GenerateForm "scheduler_values", "scheduler_names", "max_steps"

    def setDarkTheme(self, colors):
        self.sliSteps.configure(colors["sli"])
        self.sliDenoise.configure(colors["sli"])
        self.sliGuidanceScale.configure(colors["sli"])
        self.sliTileScale.configure(colors["sli"])
        self.sliTileStart.configure(colors["sli"])
        self.sliTileEnd.configure(colors["sli"])
        self.chkUseHalfVae.configure(colors["chk"])
        self.chkUseXFormers.configure(colors["chk"])
