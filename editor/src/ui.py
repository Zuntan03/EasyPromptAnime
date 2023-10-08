from config import Config
from l10n import L10n
from ui_menu import Menu
from ui_input import InputForm
from ui_preview import PreviewForm
from ui_basic import BasicForm
from ui_generate import GenerateForm
from ui_upscale import UpscaleForm
from ui_output import OutputForm
import tkinter as tk
import tkinter.ttk as ttk
import darkdetect


class Form:
    winMinW = 600
    winMinH = 750
    winInitW = 800
    winInitH = 900
    winInitX = "None"
    winInitY = "40"

    ntbFuncInitH = 400
    ntbFuncMinH = 400

    def __init__(self):
        self.win = tk.Tk()
        self.win.title(L10n.get("title"))
        self.win.minsize(Form.winMinW, Form.winMinH)

        winGeom = f"{Form.winInitW}x{Form.winInitH}"
        if Form.winInitX != "None":
            winGeom += f"+{Form.winInitX}+{Form.winInitY}"
        self.win.geometry(winGeom)

        self.menu = Menu(self.win)

        self.paneWin = tk.PanedWindow(self.win, orient=tk.VERTICAL, sashpad=2)
        self.input = InputForm(self.paneWin)

        self.ntbFunc = ttk.Notebook(self.paneWin)
        self.preview = PreviewForm(self.ntbFunc)
        self.basic = BasicForm(self.ntbFunc)
        self.generate = GenerateForm(self.ntbFunc)
        self.upscale = UpscaleForm(self.ntbFunc)
        self.paneWin.add(
            self.ntbFunc,
            height=self.ntbFuncH,
            minsize=Form.ntbFuncMinH,
            stretch="never",
        )
        self.ntbFunc.select(1)

        self.output = OutputForm(self.paneWin)
        self.paneWin.pack(fill=tk.BOTH, expand=True)

        if Form.invOsCol ^ darkdetect.isDark():
            self.setDarkTheme()

    @classmethod
    def loadConfig(cls):
        Form.winInitW = Config.get("ui_size", "win_width", Form.winInitW)
        Form.winInitH = Config.get("ui_size", "win_height", Form.winInitH)
        Form.winInitX = Config.get("ui_size", "win_x", Form.winInitX)
        Form.winInitY = Config.get("ui_size", "win_y", Form.winInitY)

        InputForm.loadConfig()
        Form.ntbFuncH = Config.get("ui_size", "func_h", Form.ntbFuncInitH)
        BasicForm.loadConfig()
        GenerateForm.loadConfig()
        UpscaleForm.loadConfig()
        OutputForm.loadConfig()

        Form.darkColFg = Config.get("ui_color", "dark_col_fg", "#CCCCCC")
        Form.darkColFgSel = Config.get("ui_color", "dark_col_fg_sel", "#FFFFFF")
        Form.darkColBg = Config.get("ui_color", "dark_col_bg", "#222222")
        Form.darkColBgSel = Config.get("ui_color", "dark_col_bg_sel", "#555555")
        Form.invOsCol = Config.getBool("ui_color", "inv_os_col", False)

    def storeConfig(self):
        Config.set("ui_size", "win_width", self.win.winfo_width())
        Config.set("ui_size", "win_height", self.win.winfo_height())
        Config.set("ui_size", "win_x", self.win.winfo_x())
        Config.set("ui_size", "win_y", self.win.winfo_y())

        self.input.storeConfig()
        Config.set("ui_size", "func_h", self.ntbFunc.winfo_height())
        self.basic.storeConfig()
        self.generate.storeConfig()
        self.output.storeConfig()

        Config.set("ui_color", "dark_col_fg", Form.darkColFg)
        Config.set("ui_color", "dark_col_fg_sel", Form.darkColFgSel)
        Config.set("ui_color", "dark_col_bg", Form.darkColBg)
        Config.set("ui_color", "dark_col_bg_sel", Form.darkColBgSel)
        Config.set("ui_color", "inv_os_col", Form.invOsCol)

    def setDarkTheme(self):
        colFgBg = {"fg": Form.darkColFg, "bg": Form.darkColBg}
        colSel = colFgBg.copy()
        colSel["selectforeground"] = Form.darkColFgSel
        colSel["selectbackground"] = Form.darkColBgSel
        colSelIns = colSel.copy()
        colSelIns["insertbackground"] = Form.darkColFgSel
        colSelHigh = colSel.copy()
        colSelHigh["highlightbackground"] = Form.darkColBgSel

        colAct = colFgBg.copy()
        colAct["activeforeground"] = Form.darkColFgSel
        colAct["activebackground"] = Form.darkColBgSel
        colActChk = colAct.copy()
        colActChk["selectcolor"] = Form.darkColBgSel

        sli = colFgBg.copy()
        sli["activebackground"] = Form.darkColBgSel
        sli["troughcolor"] = Form.darkColBg
        sli["highlightbackground"] = Form.darkColBg

        colors = {
            "fg": Form.darkColFg,
            "bg": Form.darkColBg,
            "fgSel": Form.darkColFgSel,
            "bgSel": Form.darkColBgSel,
            "fgBg": colFgBg,
            "sel": colSel,
            "selIns": colSelIns,
            "act": colAct,
            "actChk": colActChk,
            "txt": colSelIns,
            "chk": colActChk,
            "ent": colSelIns,
            "sli": sli,
            "lst": colSelHigh,
        }

        style = ttk.Style()
        style.theme_use("default")
        style.configure("TFrame", background=colors["bg"])
        style.configure("TLabel", background=colors["bg"], foreground=colors["fg"])

        style.configure(
            "TButton",
            foreground=colors["fg"],
            background=colors["bg"],
        )
        style.map(
            "TButton",
            foreground=[("active", colors["fgSel"])],
            background=[("active", colors["bgSel"])],
        )

        style.configure(
            "TCombobox",
            foreground=colors["fg"],
        )
        style.map(
            "TCombobox",
            fieldbackground=[("readonly", colors["bg"])],
            selectbackground=[
                ("readonly", colors["bg"]),
                ("readonly", "!focus", colors["bg"]),
            ],
        )

        style.configure("TNotebook", background=colors["bg"])
        style.configure("TNotebook.Tab", padding=[6, 8])
        style.map(
            "TNotebook.Tab",
            foreground=[("", colors["fg"]), ("selected", colors["fgSel"])],
            background=[("", colors["bg"]), ("selected", colors["bgSel"])],
        )

        self.input.setDarkTheme(colors)
        self.preview.setDarkTheme(colors)
        self.basic.setDarkTheme(colors)
        self.generate.setDarkTheme(colors)
        self.upscale.setDarkTheme(colors)
        self.output.setDarkTheme(colors)

    def run(self):
        self.win.lift()
        self.win.mainloop()
