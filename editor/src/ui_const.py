import tkinter as tk


class Ui:
    padX = 4
    padY = 2
    cfgTxtArea = {"spacing1": 4, "spacing2": 4, "spacing3": 4, "wrap": tk.WORD}


class UiPack:
    txt = {"side": tk.LEFT, "fill": tk.BOTH, "expand": True}
    frm = {
        "padx": Ui.padX,
        "pady": Ui.padY,
        "fill": tk.X,
    }
    sli = {
        "padx": Ui.padX,
        "pady": Ui.padY,
        "side": tk.LEFT,
        "fill": tk.X,
        "expand": True,
    }
    sep = {"padx": Ui.padX, "pady": Ui.padY, "fill": tk.X}
    lbl = {"padx": Ui.padX, "pady": Ui.padY, "side": tk.LEFT}
    btn = {"padx": Ui.padX, "pady": Ui.padY, "side": tk.LEFT}
    chk = {"padx": Ui.padX, "pady": Ui.padY, "side": tk.LEFT}
    cmb = {"padx": Ui.padX, "pady": Ui.padY, "side": tk.LEFT}
    ent = {"padx": Ui.padX, "pady": Ui.padY, "side": tk.LEFT}
