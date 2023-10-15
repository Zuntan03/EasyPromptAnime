import os
from tkinter import filedialog
from const import Path
from config import Config
from l10n import L10n
from serializer import Serializer
from ctr_menu import MenuController
from ctr_input import InputController
from ctr_preview import PreviewController
from ctr_basic import BasicController
from ctr_generate import GenerateController
from ctr_control_net import ControlNetController
from ctr_ip_adapter import IpAdapterController
from ctr_upscale import UpscaleController
from ctr_output import OutputController


class Controller:
    def __init__(self, form, model):
        self.form = form
        self.model = model

        self.menu = MenuController(self, form, model)
        self.input = InputController(form, model)
        self.preview = PreviewController(form, model)
        self.basic = BasicController(form, model)
        self.generate = GenerateController(form, model)
        self.controlNet = ControlNetController(form, model)
        self.ipAdapter = IpAdapterController(form, model)
        self.upscale = UpscaleController(form, model)
        self.output = OutputController(form, model)

        self.menu.initEvents()
        self.input.initEvents()
        self.preview.initEvents()
        self.controlNet.initEvents()

    def saveAs(self):
        os.path.exists(Path.save) or os.makedirs(Path.save)  # TODO:
        saveAsPath = filedialog.asksaveasfilename(
            filetypes=[(L10n.get("title"), "*.json")],
            initialdir=Path.save,  # TODO:
        )
        print(saveAsPath)
        if saveAsPath == "":
            return
        if not saveAsPath.endswith(".json"):
            saveAsPath += ".json"
        saved = Serializer.save(self.model, self.form, saveAsPath)
        if saved:
            print(f"Set savePath: {saveAsPath}")

    def updateConfig(self):
        self.model.updateConfig()

    def saveConfig(self):
        L10n.storeConfig()
        self.model.storeConfig()
        self.form.storeConfig()
        Config.save(Path.ini)
