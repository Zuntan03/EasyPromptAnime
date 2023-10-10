import os, subprocess
import tkinter as tk
import tkinter.ttk as ttk
from const import Path
from l10n import L10n
from config import Config
from ui_const import UiPack


class IpAdapterForm:
    def __init__(self, parent):
        self.frm = ttk.Frame(parent)

        self.initFlags()
        self.initScale()
        self.initImageDir()
        self.initInfo()

        parent.add(self.frm, text=L10n.get("ip_adapter_tab"))

    def initFlags(self):
        self.frmFlags = ttk.Frame(self.frm)

        self.varUse = tk.BooleanVar()
        self.chkUse = tk.Checkbutton(
            self.frmFlags,
            text=L10n.get("ip_adapter_use"),
            variable=self.varUse,
        )
        self.chkUse.pack(UiPack.chk)

        self.varUsePlus = tk.BooleanVar()
        self.chkUsePlus = tk.Checkbutton(
            self.frmFlags,
            text=L10n.get("ip_adapter_use_plus"),
            variable=self.varUsePlus,
        )
        self.chkUsePlus.pack(UiPack.chk)

        self.varUsePlusFace = tk.BooleanVar()
        self.chkUsePlusFace = tk.Checkbutton(
            self.frmFlags,
            text=L10n.get("ip_adapter_use_plus_face"),
            variable=self.varUsePlusFace,
        )
        self.chkUsePlusFace.pack(UiPack.chk)

        self.frmFlags.pack(UiPack.frm)

    def initScale(self):
        self.frmScale = ttk.Frame(self.frm)

        self.lblScale = ttk.Label(self.frmScale, text=L10n.get("ip_adapter_scale"))
        self.lblScale.pack(UiPack.lbl)

        self.varScale = tk.DoubleVar(value=0.5)
        self.sliScale = tk.Scale(
            self.frmScale,
            from_=0.0,
            to=1.0,
            resolution=0.05,
            orient=tk.HORIZONTAL,
            variable=self.varScale,
            takefocus=True,
        )
        self.sliScale.pack(UiPack.sli)

        self.frmScale.pack(UiPack.frm)

    def initImageDir(self):
        self.frmImageDir = ttk.Frame(self.frm)

        self.lblImageDir = ttk.Label(
            self.frmImageDir, text=L10n.get("ip_adapter_image_dir")
        )
        self.lblImageDir.pack(UiPack.lbl)

        self.varImageDir = tk.StringVar()
        self.cmbImageDir = ttk.Combobox(
            self.frmImageDir,
            textvariable=self.varImageDir,
            state="readonly",
            postcommand=self.listImageDirValues,
            width=20,
            height=20,
        )
        self.cmbImageDir.pack(UiPack.cmb, fill=tk.X, expand=True)

        self.btnImageDirExplorer = ttk.Button(
            self.frmImageDir,
            text=L10n.get("ip_adapter_image_dir_explorer"),
            command=lambda: subprocess.run(["explorer", Path.ipAdapter]),
        )
        self.btnImageDirExplorer.pack(UiPack.btn)

        self.frmImageDir.pack(UiPack.frm)

    def listImageDirValues(self):
        subDirs = [f.name for f in os.scandir(Path.ipAdapter) if f.is_dir()]
        self.cmbImageDir.configure(values=subDirs)

    def initInfo(self):
        self.frmInfo = ttk.Frame(self.frm)

        self.lblIpAdapterInfo = ttk.Label(
            self.frmInfo, text=L10n.get("ip_adapter_info")
        )
        self.lblIpAdapterInfo.pack(UiPack.lbl)

        self.frmInfo.pack(UiPack.frm)

    def setDarkTheme(self, colors):
        self.chkUse.configure(colors["chk"])
        self.chkUsePlus.configure(colors["chk"])
        self.chkUsePlusFace.configure(colors["chk"])
        self.sliScale.configure(colors["sli"])
