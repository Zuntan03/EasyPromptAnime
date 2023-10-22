from const import Const, Path
from l10n import L10n
from config import Config
from ui_const import UiPack
import tkinter as tk
import tkinter.ttk as ttk
import os, glob


class BasicForm:
    maxLength = 600
    sizeResolution = 64

    def __init__(self, parent):
        self.frm = ttk.Frame(parent)

        self.initLengthSeed()
        self.initModelVae()
        self.initSize()
        self.initUpsdcale1()
        self.initUpsdcale2()

        parent.add(self.frm, text=L10n.get("basic_tab"))

    def initLengthSeed(self):
        self.frmLengthSeed = ttk.Frame(self.frm)

        self.varLength = tk.IntVar(value=10)
        self.lblLength = ttk.Label(self.frmLengthSeed, text=L10n.get("generate_length"))
        self.varLength.trace_add("write", self.updateLength)
        self.lblLength.pack(UiPack.lbl)
        self.sliLength = tk.Scale(
            self.frmLengthSeed,
            from_=10,
            to=BasicForm.maxLength,
            resolution=10,
            orient=tk.HORIZONTAL,
            variable=self.varLength,
            takefocus=True,
        )
        self.sliLength.pack(UiPack.sli)

        self.lblSeed = ttk.Label(self.frmLengthSeed, text=L10n.get("generate_seed"))
        self.lblSeed.pack(UiPack.lbl)

        self.varSeed = tk.StringVar(value="-1")
        self.entSeed = tk.Entry(self.frmLengthSeed, textvariable=self.varSeed, width=20)
        self.entSeed.pack(UiPack.ent)
        self.btnRandomSeed = ttk.Button(
            self.frmLengthSeed,
            text="🎲",
            command=lambda: self.varSeed.set("-1"),
        )
        self.btnRandomSeed.pack(UiPack.btn)

        self.frmLengthSeed.pack(UiPack.frm)

    def updateLength(self, *args):
        self.lblLength.configure(
            text=L10n.get("generate_length").format(int(self.varLength.get() / 10))
        )

    def initModelVae(self):
        self.frmModelVae = ttk.Frame(self.frm)
        self.lblModel = ttk.Label(self.frmModelVae, text=L10n.get("generate_model"))
        self.lblModel.pack(UiPack.lbl)

        self.varModel = tk.StringVar()
        self.cmbModel = ttk.Combobox(
            self.frmModelVae,
            textvariable=self.varModel,
            state="readonly",
            postcommand=self.listModeValues,
            width=40,
            height=23,
        )
        self.cmbModel.pack(UiPack.cmb, fill=tk.X, expand=True)
        self.listModeValues()

        self.lblVae = ttk.Label(self.frmModelVae, text=L10n.get("generate_vae"))
        self.lblVae.pack(UiPack.lbl)

        self.varVae = tk.StringVar()
        self.cmbVae = ttk.Combobox(
            self.frmModelVae,
            textvariable=self.varVae,
            state="readonly",
            postcommand=self.listVaeValues,
            width=30,
            height=23,
        )
        self.cmbVae.pack(UiPack.cmb)
        self.listVaeValues()

        self.frmModelVae.pack(UiPack.frm)

    def listModeValues(self):
        baseQuery = os.path.join(Path.model, "**", "*.")
        models = glob.glob(baseQuery + "safetensors", recursive=True)
        models += glob.glob(baseQuery + "ckpt", recursive=True)
        pfxLen = len(Path.model) + 1
        models = [model[pfxLen:] for model in models]
        self.cmbModel.configure(values=models)

    def listVaeValues(self):
        baseQuery = os.path.join(Path.vae, "**", "*.")
        vaes = glob.glob(baseQuery + "safetensors", recursive=True)
        vaes += glob.glob(baseQuery + "pt", recursive=True)
        vaes += glob.glob(baseQuery + "ckpt", recursive=True)
        pfxLen = len(Path.vae) + 1
        vaes = [vae[pfxLen:] for vae in vaes]
        self.cmbVae.configure(values=vaes)

    def initSize(self):
        self.frmSize = ttk.Frame(self.frm)

        self.varWidth = tk.IntVar(value=384)
        self.varWidth.trace_add("write", self.updateSize)
        self.lblWidth = ttk.Label(self.frmSize, text=L10n.get("generate_width"))
        self.lblWidth.pack(UiPack.lbl)
        self.sliWidth = tk.Scale(
            self.frmSize,
            from_=256,
            to=1280,
            resolution=BasicForm.sizeResolution,
            orient=tk.HORIZONTAL,
            variable=self.varWidth,
            takefocus=True,
        )
        self.sliWidth.pack(UiPack.sli)

        self.varHeight = tk.IntVar(value=512)
        self.varHeight.trace_add("write", self.updateSize)
        self.lblHeight = ttk.Label(self.frmSize, text=L10n.get("generate_height"))
        self.lblHeight.pack(UiPack.lbl)
        self.sliHeight = tk.Scale(
            self.frmSize,
            from_=256,
            to=1280,
            resolution=BasicForm.sizeResolution,
            orient=tk.HORIZONTAL,
            variable=self.varHeight,
            takefocus=True,
        )

        self.sliHeight.pack(UiPack.sli)

        self.btnSwap = ttk.Button(
            self.frmSize, text=L10n.get("swap"), command=self.swapSize
        )
        self.btnSwap.pack(UiPack.btn)

        self.frmSize.pack(UiPack.frm)

    def swapSize(self):
        width = self.varWidth.get()
        self.varWidth.set(self.varHeight.get())
        self.varHeight.set(width)

    def initUpsdcale1(self):
        self.frmUpscale1 = ttk.Frame(self.frm)
        self.varUpscale1Enabled = tk.BooleanVar(value=True)
        self.chkUpscale1Enabled = tk.Checkbutton(
            self.frmUpscale1,
            text=L10n.get("upscale1"),
            variable=self.varUpscale1Enabled,
        )
        self.chkUpscale1Enabled.pack(UiPack.chk)

        self.varUpscale1Mode = tk.StringVar()
        self.cmbUpscale1Mode = ttk.Combobox(
            self.frmUpscale1,
            values=(
                Const.tile,
                Const.refine,
            ),
            textvariable=self.varUpscale1Mode,
            state="readonly",
            width=11,
        )
        self.cmbUpscale1Mode.current(1)
        self.cmbUpscale1Mode.pack(UiPack.cmb)

        self.lblUpscale1Scale = ttk.Label(
            self.frmUpscale1, text=L10n.get("upscale_scale")
        )
        self.lblUpscale1Scale.pack(UiPack.lbl)
        self.varUpscale1Scale = tk.DoubleVar(value=2.0)
        self.varUpscale1Scale.trace_add("write", self.updateSize)
        self.sliUpscale1Scale = tk.Scale(
            self.frmUpscale1,
            from_=1.0,
            to=4.0,
            resolution=0.5,
            orient=tk.HORIZONTAL,
            variable=self.varUpscale1Scale,
            takefocus=True,
        )
        self.sliUpscale1Scale.pack(UiPack.sli)

        self.frmUpscale1.pack(UiPack.frm)

    def initUpsdcale2(self):
        self.frmUpscale2 = ttk.Frame(self.frm)
        self.varUpscale2Enabled = tk.BooleanVar(value=True)
        self.chkUpscale2Enabled = tk.Checkbutton(
            self.frmUpscale2,
            text=L10n.get("upscale2"),
            variable=self.varUpscale2Enabled,
        )
        self.chkUpscale2Enabled.pack(UiPack.chk)

        self.varUpscale2Mode = tk.StringVar()
        self.cmbUpscale2Mode = ttk.Combobox(
            self.frmUpscale2,
            values=(
                Const.tile,
                Const.refine,
            ),
            textvariable=self.varUpscale2Mode,
            state="readonly",
            width=11,
        )
        self.cmbUpscale2Mode.current(0)
        self.cmbUpscale2Mode.pack(UiPack.cmb)

        self.lblUpscale2Scale = ttk.Label(
            self.frmUpscale2, text=L10n.get("upscale_scale")
        )
        self.lblUpscale2Scale.pack(UiPack.lbl)
        self.varUpscale2Scale = tk.DoubleVar(value=1.5)
        self.varUpscale2Scale.trace_add("write", self.updateSize)
        self.sliUpscale2Scale = tk.Scale(
            self.frmUpscale2,
            from_=1.0,
            to=4.0,
            resolution=0.5,
            orient=tk.HORIZONTAL,
            variable=self.varUpscale2Scale,
            takefocus=True,
        )
        self.sliUpscale2Scale.pack(UiPack.sli)

        self.frmUpscale2.pack(UiPack.frm)

    def updateSize(self, *args):
        width = self.varWidth.get()
        height = self.varHeight.get()
        upscale1 = self.varUpscale1Scale.get()
        upscale2 = upscale1 * self.varUpscale2Scale.get()

        self.chkUpscale1Enabled.configure(
            text=f"{L10n.get('upscale1')}\n{int(width * upscale1):>4} x {int(height * upscale1):>4}"
        )
        self.chkUpscale2Enabled.configure(
            text=f"{L10n.get('upscale2')}\n{int(width * upscale2):>4} x {int(height * upscale2):>4}"
        )

    @classmethod
    def loadConfig(self):
        BasicForm.maxLength = Config.get("ui", "max_length", BasicForm.maxLength)
        BasicForm.sizeResolution = Config.get(
            "ui", "size_resolution", BasicForm.sizeResolution
        )

    def storeConfig(self):
        Config.set("ui", "max_length", BasicForm.maxLength)
        Config.set("ui", "size_resolution", BasicForm.sizeResolution)

    def setDarkTheme(self, colors):
        self.sliLength.configure(colors["sli"])
        self.entSeed.configure(colors["ent"])
        self.sliWidth.configure(colors["sli"])
        self.sliHeight.configure(colors["sli"])
        self.chkUpscale1Enabled.configure(colors["chk"])
        self.sliUpscale1Scale.configure(colors["sli"])
        self.chkUpscale2Enabled.configure(colors["chk"])
        self.sliUpscale2Scale.configure(colors["sli"])
