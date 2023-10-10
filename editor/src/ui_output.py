from config import Config
from l10n import L10n
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
from ui_const import Ui, UiPack


class OutputForm:
    initH = 100
    minH = 82

    def __init__(self, parent):
        self.ntb = ttk.Notebook(parent)
        parent.add(
            self.ntb, height=OutputForm.initH, minsize=OutputForm.minH, stretch="never"
        )

        self.txtUser = scrolledtext.ScrolledText(self.ntb, state=tk.DISABLED)
        self.txtUser.configure(Ui.cfgTxtArea)
        self.txtUser.pack(UiPack.txt)
        self.ntb.add(self.txtUser, text=L10n.get("user_log_tab"))

        self.txtSys = scrolledtext.ScrolledText(self.ntb, state=tk.DISABLED)
        self.txtSys.configure(Ui.cfgTxtArea)
        self.txtSys.pack(UiPack.txt)
        self.ntb.add(self.txtSys, text=L10n.get("system_log_tab"))

        # self.ntb.select(1)  # select system log tab

        self.initCtxMenu()

    def initCtxMenu(self):
        self.mnuUser = tk.Menu(self.txtUser, tearoff=False)
        self.mnuUser.add_command(
            label=L10n.get("clear"), command=lambda: self.txtUser.delete("1.0", tk.END)
        )

        self.txtUser.bind("<Button-3>", lambda e: self.mnuUser.post(e.x_root, e.y_root))

        self.mnuSys = tk.Menu(self.txtSys, tearoff=False)
        self.mnuSys.add_command(
            label=L10n.get("clear"), command=lambda: self.txtSys.delete("1.0", tk.END)
        )

        self.txtSys.bind("<Button-3>", lambda e: self.mnuSys.post(e.x_root, e.y_root))

    @classmethod
    def loadConfig(self):
        OutputForm.initH = Config.get("ui_size", "output_h", OutputForm.initH)

    def storeConfig(self):
        output_h = self.ntb.winfo_height()
        if output_h != 1:
            Config.set("ui_size", "output_h", output_h)

    def setDarkTheme(self, colors):
        self.txtUser.configure(colors["selIns"])
        self.txtSys.configure(colors["selIns"])
