from const import Const
from log import Log
import tkinter as tk


class BasicController:
    def __init__(self, form, model):
        self.form = form
        self.model = model

        mGenerate = self.model.generate
        vBasic = self.form.basic
        mGenerate.bind("length", vBasic.varLength)
        mGenerate.bind("model", vBasic.varModel)
        mGenerate.bind("vae", vBasic.varVae)
        mGenerate.bind("seed", vBasic.varSeed)
        mGenerate.bind("width", vBasic.varWidth)
        mGenerate.bind("height", vBasic.varHeight)

        mGenerate.bind("upscale1Enabled", vBasic.varUpscale1Enabled)
        mGenerate.bind("upscale1Mode", vBasic.varUpscale1Mode)
        mGenerate.bind("upscale1Scale", vBasic.varUpscale1Scale)

        mGenerate.bind("upscale2Enabled", vBasic.varUpscale2Enabled)
        mGenerate.bind("upscale2Mode", vBasic.varUpscale1Mode)
        mGenerate.bind("upscale2Scale", vBasic.varUpscale2Scale)
