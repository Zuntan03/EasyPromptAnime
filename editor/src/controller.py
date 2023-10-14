import tkinter as tk
from const import Path
from config import Config
from l10n import L10n
from ctr_menu import MenuController
from ctr_input import InputController
from ctr_preview import PreviewController
from ctr_basic import BasicController
from ctr_generate import GenerateController
from ctr_upscale import UpscaleController
from ctr_ip_adapter import IpAdapterController
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
        self.upscale = UpscaleController(form, model)
        self.ipAdapter = IpAdapterController(form, model)
        self.output = OutputController(form, model)

        self.menu.initEvents()
        self.input.initEvents()
        self.preview.initEvents()

    def updateConfig(self):
        self.model.updateConfig()

    def saveConfig(self):
        L10n.storeConfig()
        self.model.storeConfig()
        self.form.storeConfig()
        Config.save(Path.ini)
