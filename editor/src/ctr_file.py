import os
from tkinter import filedialog
import json
from const import Path
from l10n import L10n
from log import Log
from serializer import Serializer


class FileController:
    def __init__(self, form, model):
        self.form = form
        self.model = model

        self.form.win.bind("<Control-o>", lambda e: self.open())
        self.form.win.bind("<Control-s>", lambda e: self.save())

    # TODO: new

    def open(self):
        os.path.exists(Path.save) or os.makedirs(Path.save)
        initDir = Path.save
        if self.model.editor.savePath != "":
            initDir = os.path.dirname(self.model.editor.savePath)
        openPath = filedialog.askopenfilename(
            filetypes=[(L10n.get("title"), "*.json")],  # TODO: promptTravelConfig
            initialdir=initDir,
        )
        if openPath == "":
            return
        data = None
        with open(openPath, "r") as f:
            data = json.load(f)
        if Serializer.versionKey in data:
            Serializer.deserialize(self.model, data)
            self.model.editor.set("savePath", openPath)
            Log.user(L10n.format("log_file_open", openPath))
        else:
            pass  # TODO: import prompt travel config

    def save(self):
        if self.model.editor.savePath == "":
            self.saveAs()
            return
        data = Serializer.serialize(self.model)
        with open(self.model.editor.savePath, "w") as f:
            json.dump(data, f, indent=4)
        Log.user(L10n.format("log_file_save", self.model.editor.savePath))

    def saveAs(self):
        os.path.exists(Path.save) or os.makedirs(Path.save)
        initDir = Path.save
        if self.model.editor.savePath != "":
            initDir = os.path.dirname(self.model.editor.savePath)
        saveAsPath = filedialog.asksaveasfilename(
            filetypes=[(L10n.get("title"), "*.json")], initialdir=initDir
        )
        if saveAsPath == "":
            return
        if not saveAsPath.endswith(".json"):
            saveAsPath += ".json"
        data = Serializer.serialize(self.model)
        with open(saveAsPath, "w") as f:
            json.dump(data, f, indent=4)
        self.model.editor.set("savePath", saveAsPath)
        Log.user(L10n.format("log_file_save_as", saveAsPath))
