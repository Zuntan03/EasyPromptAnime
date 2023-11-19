from const import Const, Path
from l10n import L10n
from config import Config
from ui_const import UiPack
import tkinter as tk
import tkinter.ttk as ttk
import os, glob


class GenerateForm:
    schedulerValues = Const.schedulerValues
    schedulerNames = Const.schedulerNames
    maxSteps = 60

    def __init__(self, parent):
        self.frm = ttk.Frame(parent)

        self.initMotionModuleContext()
        self.initSchedulerSteps()
        self.initGuidanceScaleClipScale()
        self.initPromptFixedRatioHalfVaeXFormers()

        parent.add(self.frm, text=L10n.get("generate_tab"))

    def initMotionModuleContext(self):
        self.frmMotionModuleContext = ttk.Frame(self.frm)

        self.lblMotionModule = ttk.Label(
            self.frmMotionModuleContext, text=L10n.get("generate_motion_module")
        )
        self.lblMotionModule.pack(UiPack.lbl)

        self.varMotionModule = tk.StringVar()
        self.cmbMotionModule = ttk.Combobox(
            self.frmMotionModuleContext,
            textvariable=self.varMotionModule,
            state="readonly",
            postcommand=self.listMotionModuleValues,
            width=40,
            height=23,
        )
        self.cmbMotionModule.pack(UiPack.cmb)
        self.listMotionModuleValues()

        self.lblContext = ttk.Label(
            self.frmMotionModuleContext, text=L10n.get("generate_context")
        )
        self.lblContext.pack(UiPack.lbl)
        self.varContext = tk.IntVar(value=14)
        self.sliContext = tk.Scale(
            self.frmMotionModuleContext,
            from_=8,
            to=24,
            resolution=2,
            orient=tk.HORIZONTAL,
            variable=self.varContext,
            takefocus=True,
        )
        self.sliContext.pack(UiPack.sli)

        self.frmMotionModuleContext.pack(UiPack.frm)

    def listMotionModuleValues(self):
        baseQuery = os.path.join(Path.motionModule, "**", "*.")
        motionModules = glob.glob(baseQuery + "ckpt", recursive=True)
        motionModules += glob.glob(baseQuery + "safetensors", recursive=True)
        motionModules += glob.glob(baseQuery + "pth", recursive=True)
        pfxLen = len(Path.motionModule) + 1
        motionModules = [motionModule[pfxLen:] for motionModule in motionModules]
        self.cmbMotionModule.configure(values=motionModules)

    def initSchedulerSteps(self):
        self.frmSchedulerSteps = ttk.Frame(self.frm)

        self.lblScheduler = ttk.Label(
            self.frmSchedulerSteps, text=L10n.get("generate_scheduler")
        )
        self.lblScheduler.pack(UiPack.lbl)

        self.varScheduler = tk.StringVar()
        self.cmbScheduler = ttk.Combobox(
            self.frmSchedulerSteps,
            textvariable=self.varScheduler,
            state="readonly",
            values=GenerateForm.schedulerNames,
            width=21,
            height=23,
        )
        self.cmbScheduler.pack(UiPack.cmb)

        self.lblSteps = ttk.Label(
            self.frmSchedulerSteps, text=L10n.get("generate_steps")
        )
        self.lblSteps.pack(UiPack.lbl)

        self.varSteps = tk.IntVar(value=20)
        self.sliSteps = tk.Scale(
            self.frmSchedulerSteps,
            from_=1,
            to=GenerateForm.maxSteps,
            resolution=1,
            orient=tk.HORIZONTAL,
            variable=self.varSteps,
            takefocus=True,
        )
        self.sliSteps.pack(UiPack.sli)

        self.frmSchedulerSteps.pack(UiPack.frm)

    def initGuidanceScaleClipScale(self):
        self.frmClipScaleGuidanceScale = ttk.Frame(self.frm)

        self.lblGuidanceScale = ttk.Label(
            self.frmClipScaleGuidanceScale, text=L10n.get("generate_guidance_scale")
        )
        self.lblGuidanceScale.pack(UiPack.lbl)

        self.varGuidanceScale = tk.DoubleVar(value=8.0)
        self.sliGuidanceScale = tk.Scale(
            self.frmClipScaleGuidanceScale,
            from_=1.0,
            to=30.0,
            resolution=0.5,
            orient=tk.HORIZONTAL,
            variable=self.varGuidanceScale,
            takefocus=True,
        )
        self.sliGuidanceScale.pack(UiPack.sli)

        self.lblClipSkip = ttk.Label(
            self.frmClipScaleGuidanceScale, text=L10n.get("generate_clip_skip")
        )
        self.lblClipSkip.pack(UiPack.lbl)

        self.varClipSkip = tk.IntVar(value=2)
        self.sliClipSkip = tk.Scale(
            self.frmClipScaleGuidanceScale,
            from_=1,
            to=5,
            resolution=1,
            orient=tk.HORIZONTAL,
            variable=self.varClipSkip,
            takefocus=True,
        )
        self.sliClipSkip.pack(UiPack.sli)

        self.frmClipScaleGuidanceScale.pack(UiPack.frm)

    def initPromptFixedRatioHalfVaeXFormers(self):
        self.frmPromptFixedRatioHalfVaeXFormers = ttk.Frame(self.frm)

        self.lblPromptFixedRatio = ttk.Label(
            self.frmPromptFixedRatioHalfVaeXFormers,
            text=L10n.get("generate_prompt_fixed_ratio"),
        )
        self.lblPromptFixedRatio.pack(UiPack.lbl)

        self.varPromptFixedRatio = tk.DoubleVar(value=0.5)
        self.sliPromptFixedRatio = tk.Scale(
            self.frmPromptFixedRatioHalfVaeXFormers,
            from_=0.0,
            to=1.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            variable=self.varPromptFixedRatio,
            takefocus=True,
        )
        self.sliPromptFixedRatio.pack(UiPack.sli)

        self.varUseHalfVae = tk.BooleanVar(value=False)
        self.chkUseHalfVae = tk.Checkbutton(
            self.frmPromptFixedRatioHalfVaeXFormers,
            text=L10n.get("generate_use_half_vae"),
            variable=self.varUseHalfVae,
        )
        self.chkUseHalfVae.pack(UiPack.chk)

        self.varUseXFormers = tk.BooleanVar(value=False)
        self.chkUseXFormers = tk.Checkbutton(
            self.frmPromptFixedRatioHalfVaeXFormers,
            text=L10n.get("generate_use_x_formers"),
            variable=self.varUseXFormers,
        )
        self.chkUseXFormers.pack(UiPack.chk)

        self.frmPromptFixedRatioHalfVaeXFormers.pack(UiPack.frm)

    @classmethod
    def loadConfig(self):
        values = ",".join(GenerateForm.schedulerValues)
        values = Config.get("ui", "scheduler_values", values)
        GenerateForm.schedulerValues = [s.strip() for s in values.split(",")]

        names = ",".join(GenerateForm.schedulerNames)
        names = Config.get("ui", "scheduler_names", names)
        GenerateForm.schedulerNames = [s.strip() for s in names.split(",")]

        GenerateForm.maxSteps = Config.getInt("ui", "max_steps", GenerateForm.maxSteps)

    def storeConfig(self):
        Config.set("ui", "scheduler_values", ",".join(GenerateForm.schedulerValues))
        Config.set("ui", "scheduler_names", ",".join(GenerateForm.schedulerNames))
        Config.set("ui", "max_steps", GenerateForm.maxSteps)

    def setDarkTheme(self, colors):
        self.sliContext.configure(colors["sli"])
        self.sliSteps.configure(colors["sli"])
        self.sliClipSkip.configure(colors["sli"])
        self.sliGuidanceScale.configure(colors["sli"])
        self.sliPromptFixedRatio.configure(colors["sli"])
        self.chkUseHalfVae.configure(colors["chk"])
        self.chkUseXFormers.configure(colors["chk"])
