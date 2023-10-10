from log import Log
import tkinter as tk


class UpscaleController:
    def __init__(self, form, model):
        self.form = form
        self.model = model
        mGenerate = self.model.generate
        vUpscale = self.form.upscale

        mGenerate.bind("upscaleScheduler", vUpscale.varScheduler)
        mGenerate.bind("upscaleSteps", vUpscale.varSteps)
        mGenerate.bind("upscaleGuidanceScale", vUpscale.varGuidanceScale)
        mGenerate.bind("upscaleStrength", vUpscale.varDenoise)
        mGenerate.bind("upscaleTileScale", vUpscale.varTileScale)
        mGenerate.bind("upscaleTileStart", vUpscale.varTileStart)
        mGenerate.bind("upscaleTileEnd", vUpscale.varTileEnd)
        mGenerate.bind("upscaleUseHalfVae", vUpscale.varUseHalfVae)
        mGenerate.bind("upscaleUseXFormers", vUpscale.varUseXFormers)
