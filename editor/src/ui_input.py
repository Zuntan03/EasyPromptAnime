from config import Config
from l10n import L10n
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
from ui_const import Ui, UiPack
from task import Task


class InputForm:
    initH = 300
    minH = 250

    def __init__(self, parent):
        self.frm = ttk.Frame(parent)

        self.frmTool = ttk.Frame(self.frm)

        self.initGenerate(self.frmTool)
        self.sep0 = ttk.Separator(self.frmTool)
        self.sep0.pack(UiPack.sep)

        self.initPreview(self.frmTool)
        self.sep1 = ttk.Separator(self.frmTool)
        self.sep1.pack(UiPack.sep)

        self.initTask(self.frmTool)

        self.frmTool.pack(fill=tk.Y, side=tk.RIGHT)

        self.txtInput = scrolledtext.ScrolledText(self.frm)
        self.txtInput.configure(Ui.cfgTxtArea)
        self.txtInput.pack(UiPack.txt)

        self.frm.pack(fill=tk.BOTH, expand=True)

        parent.add(
            self.frm, height=InputForm.initH, minsize=InputForm.minH, stretch="always"
        )

        self.initCtxMenu()

    def initGenerate(self, parent):
        self.frmGenerate = ttk.Frame(parent)
        self.btnGenerate = ttk.Button(self.frmGenerate, text=L10n.get("generate_anime"))
        self.btnGenerate.pack(UiPack.btn, fill=tk.X, expand=True)

        self.btnSeedGacha = ttk.Button(self.frmGenerate, text=L10n.get("seed_gacha"))
        self.btnSeedGacha.pack(UiPack.btn, fill=tk.X, expand=True)

        self.frmGenerate.pack(UiPack.frm)

    def initPreview(self, parent):
        self.frmPreview = ttk.Frame(parent)
        self.btnPreview = ttk.Button(self.frmPreview, text=L10n.get("preview"))
        self.btnPreview.pack(UiPack.btn)

        self.varUpscale = tk.BooleanVar(value=True)
        self.chkUpscale = tk.Checkbutton(
            self.frmPreview, text=L10n.get("preview_upscale"), variable=self.varUpscale
        )
        self.chkUpscale.pack(UiPack.chk)

        # self.varInterpolation = tk.BooleanVar(value=True)
        # self.chkInterpolation = tk.Checkbutton(
        #     self.frmPreview,
        #     text=L10n.get("preview_interpolation"),
        #     variable=self.varInterpolation,
        # )
        # self.chkInterpolation.pack(UiPack.chk)

        self.frmPreview.pack(UiPack.frm)

        self.frmStart = ttk.Frame(parent)
        self.varStart = tk.IntVar(value=0)
        self.lblStart = ttk.Label(self.frmStart, text=L10n.get("preview_start_frame"))
        self.lblStart.pack(UiPack.lbl)
        self.sliStart = tk.Scale(
            self.frmStart,
            from_=0,
            to=600,
            resolution=10,
            orient=tk.HORIZONTAL,
            variable=self.varStart,
            takefocus=True,
        )
        self.sliStart.pack(UiPack.sli)
        self.frmStart.pack(UiPack.frm)

        self.frmLength = ttk.Frame(parent)
        self.varLength = tk.IntVar(value=0)
        self.lblLength = ttk.Label(self.frmLength, text=L10n.get("preview_length"))
        self.lblLength.pack(UiPack.lbl)
        self.sliLength = tk.Scale(
            self.frmLength,
            from_=0,
            to=600,
            resolution=10,
            orient=tk.HORIZONTAL,
            variable=self.varLength,
            takefocus=True,
        )
        self.sliLength.pack(UiPack.sli)
        self.frmLength.pack(UiPack.frm)

    def initTask(self, parent):
        self.frmTask = ttk.Frame(parent)

        self.varForever = tk.BooleanVar(value=False)
        self.chkForever = tk.Checkbutton(
            self.frmTask, text=L10n.get("task_forever"), variable=self.varForever
        )
        self.chkForever.pack(UiPack.chk)

        self.varPauseByError = tk.BooleanVar(value=True)
        self.chkPauseByError = tk.Checkbutton(
            self.frmTask,
            text=L10n.get("task_pause_by_error"),
            variable=self.varPauseByError,
        )
        self.chkPauseByError.pack(UiPack.chk)

        self.frmTask.pack(UiPack.frm)

        self.varTask = tk.StringVar()
        Task.queueInfoChangedEvent.append(lambda queue: self.varTask.set(queue))
        self.lstTask = tk.Listbox(self.frmTool, listvariable=self.varTask)
        self.lstTask.pack(fill=tk.BOTH, expand=True, padx=Ui.padX, pady=Ui.padY)

    def initCtxMenu(self):
        self.mnuInTxt = tk.Menu(self.txtInput, tearoff=False)
        self.mnuInTxt.add_command(
            label=L10n.get("clear"),
            command=lambda: self.txtInput.delete("1.0", tk.END),
        )
        self.txtInput.bind(
            "<Button-3>", lambda e: self.mnuInTxt.post(e.x_root, e.y_root)
        )

    @classmethod
    def loadConfig(cls):
        InputForm.initH = Config.get("ui_size", "input_h", fallback=InputForm.initH)

    def storeConfig(self):
        input_h = self.frm.winfo_height()
        if input_h != 1:
            Config.set("ui_size", "input_h", input_h)

    def setDarkTheme(self, colors):
        self.txtInput.configure(colors["txt"])
        self.chkUpscale.configure(colors["chk"])
        # self.chkInterpolation.configure(colors["chk"])
        self.sliStart.configure(colors["sli"])
        self.sliLength.configure(colors["sli"])
        self.lstTask.configure(colors["lst"])
        self.chkForever.configure(colors["chk"])
        self.chkPauseByError.configure(colors["chk"])
