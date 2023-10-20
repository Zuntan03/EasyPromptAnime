import os
from tkinter import filedialog, messagebox
import json
from const import Path
from l10n import L10n
from log import Log
from serializer import Serializer


class FileController:
    def __init__(self, form, model):
        self.form = form
        self.model = model

        self.form.win.bind("<Control-n>", lambda e: self.new())
        self.form.win.bind("<Control-o>", lambda e: self.open())
        self.form.win.bind("<Control-s>", lambda e: self.save())

    # TODO: new
    def new(self):
        if not self.askSave():
            return False
        self.model.reset()
        self.model.notifyAll()
        self.form.win.after(0, self.resetChanged)
        self.form.win.title(L10n.get("title"))

        Log.user(L10n.get("log_file_new"))
        return True

    def open(self):
        if not self.askSave():
            return False
        os.path.exists(Path.save) or os.makedirs(Path.save)
        initDir = Path.save
        if self.model.editor.savePath != "":
            initDir = os.path.dirname(self.model.editor.savePath)
        openPath = filedialog.askopenfilename(
            filetypes=[(L10n.get("title"), "*.json")],  # TODO: promptTravelConfig
            initialdir=initDir,
        )
        if openPath == "":
            return False
        data = None
        with open(openPath, "r", encoding="utf-8-sig") as f:
            data = json.load(f)
        if Serializer.versionKey in data:
            if Serializer.deserialize(self.model, data):
                self.model.editor.set("savePath", openPath)
                self.form.win.title(L10n.get("title") + openPath)
                self.resetChanged()
                Log.user(L10n.format("log_file_open", openPath))
                return True
            else:
                Log.user(L10n.format("log_file_open_failed", openPath))
                return False
        else:
            return False  # TODO: import prompt travel config

    def save(self):
        if self.model.editor.savePath == "":
            return self.saveAs()
        data = Serializer.serialize(self.model)
        with open(self.model.editor.savePath, "w", encoding="utf-8-sig") as f:
            json.dump(data, f, indent=4)
        self.resetChanged()
        Log.user(L10n.format("log_file_save", self.model.editor.savePath))
        return True

    def saveAs(self):
        os.path.exists(Path.save) or os.makedirs(Path.save)
        initDir = Path.save
        if self.model.editor.savePath != "":
            initDir = os.path.dirname(self.model.editor.savePath)
        saveAsPath = filedialog.asksaveasfilename(
            filetypes=[(L10n.get("title"), "*.json")], initialdir=initDir
        )
        if saveAsPath == "":
            return False
        if not saveAsPath.endswith(".json"):
            saveAsPath += ".json"
        data = Serializer.serialize(self.model)
        with open(saveAsPath, "w") as f:
            json.dump(data, f, indent=4, encoding="utf-8-sig")
        self.model.editor.set("savePath", saveAsPath)
        self.form.win.title(L10n.get("title") + saveAsPath)
        self.resetChanged()
        Log.user(L10n.format("log_file_save_as", saveAsPath))
        return True

    def askSave(self):
        if not self.isChanged():
            return True
        result = messagebox.askyesnocancel(L10n.get("title"), L10n.get("dlg_ask_save"))
        if result is None:
            return False
        if result:
            return self.save()
        return True

    def isChanged(self):
        return (
            self.model.prompt.isChanged
            or self.model.generate.isChanged
            or self.model.editor.isChanged
        )

    def resetChanged(self):
        self.model.prompt.isChanged = False
        self.model.generate.isChanged = False
        self.model.editor.isChanged = False
