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
        mGenerate.bind("upscaleTileEnable", vUpscale.varTileEnable)
        mGenerate.bind("upscaleTileScale", vUpscale.varTileScale)
        mGenerate.bind("upscaleTileStart", vUpscale.varTileStart)
        mGenerate.bind("upscaleTileEnd", vUpscale.varTileEnd)
        mGenerate.bind("upscaleIp2pEnable", vUpscale.varIp2pEnable)
        mGenerate.bind("upscaleIp2pScale", vUpscale.varIp2pScale)
        mGenerate.bind("upscaleIp2pStart", vUpscale.varIp2pStart)
        mGenerate.bind("upscaleIp2pEnd", vUpscale.varIp2pEnd)
        mGenerate.bind("upscaleLineAnimeEnable", vUpscale.varLineAnimeEnable)
        mGenerate.bind("upscaleLineAnimeScale", vUpscale.varLineAnimeScale)
        mGenerate.bind("upscaleLineAnimeStart", vUpscale.varLineAnimeStart)
        mGenerate.bind("upscaleLineAnimeEnd", vUpscale.varLineAnimeEnd)
        mGenerate.bind("upscaleUseHalfVae", vUpscale.varUseHalfVae)
        mGenerate.bind("upscaleUseXFormers", vUpscale.varUseXFormers)
