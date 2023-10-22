import os, subprocess
import tkinter as tk
import tkinter.ttk as ttk
from const import Path, ControlNetType
from l10n import L10n
from config import Config
from ui_const import UiPack


class ControlNetForm:
    def __init__(self, parent):
        self.frm = ttk.Frame(parent)

        self.initControlNetDirLoop()
        self.initControlNetInfo()
        self.initImport()

        self.ntb = ttk.Notebook(self.frm)
        self.ntb.pack(fill=tk.BOTH, expand=True)

        for cnType in ControlNetType:
            self.initControlNetTab(self.ntb, cnType)

        parent.add(self.frm, text=L10n.get("control_net_tab"))

    def initControlNetDirLoop(self):
        self.frmControlNetDirLoop = ttk.Frame(self.frm)

        self.lblControlNetDir = ttk.Label(
            self.frmControlNetDirLoop, text=L10n.get("control_net_dir")
        )
        self.lblControlNetDir.pack(UiPack.lbl)

        self.varControlNetDir = tk.StringVar()
        self.cmbControlNetDir = ttk.Combobox(
            self.frmControlNetDirLoop,
            textvariable=self.varControlNetDir,
            state="readonly",
            postcommand=self.listControlNetDirValues,
            width=20,
            height=20,
        )
        self.cmbControlNetDir.pack(UiPack.cmb, fill=tk.X, expand=True)

        self.btnControlNetDirExplorer = ttk.Button(
            self.frmControlNetDirLoop,
            text=L10n.get("ip_adapter_image_dir_explorer"),
            command=lambda: subprocess.run(["explorer", Path.controlNet]),
        )
        self.btnControlNetDirExplorer.pack(UiPack.btn)

        self.varControlNetLoop = tk.BooleanVar(value=True)
        self.chkControlNetLoop = tk.Checkbutton(
            self.frmControlNetDirLoop,
            text=L10n.get("control_net_loop"),
            variable=self.varControlNetLoop,
        )
        self.chkControlNetLoop.pack(UiPack.chk)

        self.frmControlNetDirLoop.pack(UiPack.frm)

    def listControlNetDirValues(self):
        subDirs = [f.name for f in os.scandir(Path.controlNet) if f.is_dir()]
        self.cmbControlNetDir.configure(values=subDirs)

    def initControlNetInfo(self):
        self.frmInfo = ttk.Frame(self.frm)

        self.lblControlNetInfo = ttk.Label(
            self.frmInfo, text=L10n.get("control_net_info")
        )
        self.lblControlNetInfo.pack(UiPack.lbl)

        self.frmInfo.pack(UiPack.frm)

    def initImport(self):
        self.frmImport = ttk.Frame(self.frm)

        self.btnImport = ttk.Button(
            self.frmImport,
            text=L10n.get("control_net_import"),
        )
        self.btnImport.pack(UiPack.btn)

        self.lblImportSpeed = ttk.Label(
            self.frmImport, text=L10n.get("control_net_import_speed")
        )
        self.lblImportSpeed.pack(UiPack.lbl)
        self.varImportSpeed = tk.StringVar(value="1")
        self.entImportSpeed = tk.Entry(
            self.frmImport, textvariable=self.varImportSpeed, width=4
        )
        self.entImportSpeed.pack(UiPack.ent)

        self.lblImportStart = ttk.Label(
            self.frmImport, text=L10n.get("control_net_import_start")
        )
        self.lblImportStart.pack(UiPack.lbl)
        self.varImportStart = tk.StringVar(value="")
        self.entImportStart = tk.Entry(
            self.frmImport, textvariable=self.varImportStart, width=11
        )
        self.entImportStart.pack(UiPack.ent)

        self.lblImportStart = ttk.Label(
            self.frmImport, text=L10n.get("control_net_import_length")
        )
        self.lblImportStart.pack(UiPack.lbl)
        self.varImportLength = tk.StringVar(value="")
        self.entImportLength = tk.Entry(
            self.frmImport, textvariable=self.varImportLength, width=11
        )
        self.entImportLength.pack(UiPack.ent)

        self.lblImportIndex = ttk.Label(
            self.frmImport, text=L10n.get("control_net_import_index")
        )
        self.lblImportIndex.pack(UiPack.lbl)
        self.varImportIndex = tk.StringVar(value="0")
        self.entImportIndex = tk.Entry(
            self.frmImport, textvariable=self.varImportIndex, width=4
        )
        self.entImportIndex.pack(UiPack.ent)

        self.frmImport.pack(UiPack.frm)
        pass

    def initControlNetTab(self, parent, cnType):
        name = cnType.name
        frm = ttk.Frame(parent)
        setattr(self, f"frm_{name}", frm)

        self.initControlNetFlags(frm, name)
        self.initControlNetScaleScaleList(frm, name)
        self.initControlNetStartEnd(frm, name)

        parent.add(frm, text=name)

    def initControlNetFlags(self, parent, name):
        frm = ttk.Frame(parent)
        setattr(self, f"frmFlags_{name}", frm)

        varEnable = tk.BooleanVar()
        setattr(self, f"varEnable_{name}", varEnable)
        chkEnable = tk.Checkbutton(
            frm,
            text=L10n.format("control_net_enable", name),
            variable=varEnable,
        )
        setattr(self, f"chkEnable_{name}", chkEnable)
        chkEnable.pack(UiPack.chk)

        btnOpenDir = ttk.Button(
            frm,
            text=L10n.format("control_net_open_dir", name),
            command=lambda: self.varControlNetDir.get() == ""
            or subprocess.run(
                [
                    "explorer",
                    os.path.join(
                        Path.controlNet,
                        self.varControlNetDir.get(),
                        f"controlnet_{name}",
                    ),
                ]
            ),
        )
        setattr(self, f"btnOpenDir_{name}", btnOpenDir)
        btnOpenDir.pack(UiPack.btn)

        varUsePreprocessor = tk.BooleanVar(value=True)
        setattr(self, f"varUsePreprocessor_{name}", varUsePreprocessor)
        chkPreprocessor = tk.Checkbutton(
            frm,
            text=L10n.get("control_net_preprocessor"),
            variable=varUsePreprocessor,
        )
        setattr(self, f"chkPreprocessor_{name}", chkPreprocessor)
        chkPreprocessor.pack(UiPack.chk)

        varGuessMode = tk.BooleanVar()
        setattr(self, f"varGuessMode_{name}", varGuessMode)
        chkGuessMode = tk.Checkbutton(
            frm,
            text=L10n.format("control_net_guess_mode", name),
            variable=varGuessMode,
        )
        setattr(self, f"chkGuessMode_{name}", chkGuessMode)
        chkGuessMode.pack(UiPack.chk)

        frm.pack(UiPack.frm)

    def initControlNetScaleScaleList(self, parent, name):
        frm = ttk.Frame(parent)
        setattr(self, f"frmScaleScaleList_{name}", frm)

        varScale = tk.DoubleVar(value=1.0)
        setattr(self, f"varScale_{name}", varScale)
        lblScale = ttk.Label(frm, text=L10n.format("control_net_scale", name))
        lblScale.pack(UiPack.lbl)
        sliScale = tk.Scale(
            frm,
            from_=0.0,
            to=2.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=varScale,
            takefocus=True,
        )
        setattr(self, f"sliScale_{name}", sliScale)
        sliScale.pack(UiPack.sli)

        varScaleList = tk.StringVar()
        setattr(self, f"varScaleList_{name}", varScaleList)
        lblScaleList = ttk.Label(frm, text=L10n.get("control_net_scale_list"))
        lblScaleList.pack(UiPack.lbl)
        entScaleList = tk.Entry(frm, textvariable=varScaleList)
        setattr(self, f"entScaleList_{name}", entScaleList)
        entScaleList.pack(UiPack.ent, fill=tk.X, expand=True)

        frm.pack(UiPack.frm)

    def initControlNetStartEnd(self, parent, name):
        frm = ttk.Frame(parent)

        varStart = tk.DoubleVar(value=0.0)
        setattr(self, f"varStart_{name}", varStart)
        lblStart = ttk.Label(frm, text=L10n.format("control_net_start", name))
        lblStart.pack(UiPack.lbl)
        sliStart = tk.Scale(
            frm,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=varStart,
            takefocus=True,
        )
        setattr(self, f"sliStart_{name}", sliStart)
        sliStart.pack(UiPack.sli)

        varEnd = tk.DoubleVar(value=1.0)
        setattr(self, f"varEnd_{name}", varEnd)
        lblEnd = ttk.Label(frm, text=L10n.format("control_net_end", name))
        lblEnd.pack(UiPack.lbl)
        sliEnd = tk.Scale(
            frm,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=varEnd,
            takefocus=True,
        )
        setattr(self, f"sliEnd_{name}", sliEnd)
        sliEnd.pack(UiPack.sli)

        frm.pack(UiPack.frm)

    def setDarkTheme(self, colors):
        self.chkControlNetLoop.configure(colors["chk"])
        self.entImportSpeed.configure(colors["ent"])
        self.entImportStart.configure(colors["ent"])
        self.entImportLength.configure(colors["ent"])
        self.entImportIndex.configure(colors["ent"])
        for cnType in ControlNetType:
            getattr(self, f"chkEnable_{cnType.name}").configure(colors["chk"])
            getattr(self, f"chkPreprocessor_{cnType.name}").configure(colors["chk"])
            getattr(self, f"chkGuessMode_{cnType.name}").configure(colors["chk"])
            getattr(self, f"sliScale_{cnType.name}").configure(colors["sli"])
            getattr(self, f"entScaleList_{cnType.name}").configure(colors["ent"])
            getattr(self, f"sliStart_{cnType.name}").configure(colors["sli"])
            getattr(self, f"sliEnd_{cnType.name}").configure(colors["sli"])
