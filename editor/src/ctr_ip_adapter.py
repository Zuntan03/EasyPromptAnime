from log import Log
import tkinter as tk


class IpAdapterController:
    def __init__(self, form, model):
        self.form = form
        self.model = model
        mGenerate = self.model.generate
        vIpAdapter = self.form.ipAdapter

        mGenerate.bind("useIpAdapter", vIpAdapter.varUse)
        mGenerate.bind("useIpAdapterPlus", vIpAdapter.varUsePlus)
        mGenerate.bind("useIpAdapterPlusFace", vIpAdapter.varUsePlusFace)
        mGenerate.bind("ipAdapterScale", vIpAdapter.varScale)
        mGenerate.bind("ipAdapterImageDir", vIpAdapter.varImageDir)
