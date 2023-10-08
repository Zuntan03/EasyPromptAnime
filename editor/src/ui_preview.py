from config import Config
from l10n import L10n
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import scrolledtext
from ui_const import Ui, UiPack


class PreviewForm:
    def __init__(self, parent):
        self.frm = ttk.Frame(parent)

        self.initOptions()

        self.txtPrev = scrolledtext.ScrolledText(self.frm, state=tk.DISABLED)
        self.txtPrev.configure(Ui.cfgTxtArea)
        self.txtPrev.pack(UiPack.txt)

        parent.add(self.frm, text=L10n.get("preview_tab"))

    def initOptions(self):
        self.frmOptions = ttk.Frame(self.frm)

        self.varShowKeyframe = tk.BooleanVar(value=True)
        self.chkShowKeyframe = tk.Checkbutton(
            self.frmOptions,
            text=L10n.get("preview_show_keyframe"),
            variable=self.varShowKeyframe,
        )
        self.chkShowKeyframe.pack(UiPack.chk)

        self.varShowHeaderFooter = tk.BooleanVar(value=True)
        self.chkShowHeaderFooter = tk.Checkbutton(
            self.frmOptions,
            text=L10n.get("preview_show_header_footer"),
            variable=self.varShowHeaderFooter,
        )
        self.chkShowHeaderFooter.pack(UiPack.chk)

        self.varShowKeyframe.trace_add("write", self.updateShowKeyframe)

        self.varShowAnime = tk.BooleanVar(value=True)
        self.chkShowAnime = tk.Checkbutton(
            self.frmOptions,
            text=L10n.get("preview_show_anime"),
            variable=self.varShowAnime,
        )
        self.chkShowAnime.pack(UiPack.chk)

        self.frmOptions.pack(UiPack.frm, side=tk.BOTTOM)

    def updateShowKeyframe(self, *args):
        if self.varShowKeyframe.get():
            self.chkShowHeaderFooter.configure(state=tk.NORMAL)
        else:
            self.chkShowHeaderFooter.configure(state=tk.DISABLED)

    def setDarkTheme(self, colors):
        self.chkShowKeyframe.configure(colors["chk"])
        self.chkShowHeaderFooter.configure(colors["chk"])
        self.chkShowAnime.configure(colors["chk"])
        self.txtPrev.configure(colors["txt"])
