from log import Log
import tkinter as tk


class GenerateController:
    def __init__(self, form, model):
        self.form = form
        self.model = model

        mGenerate = self.model.generate
        vGenerate = self.form.generate

        mGenerate.bind("motionModule", vGenerate.varMotionModule)
        mGenerate.bind("context", vGenerate.varContext)
        mGenerate.bind("scheduler", vGenerate.varScheduler)
        mGenerate.bind("steps", vGenerate.varSteps)
        mGenerate.bind("guidanceScale", vGenerate.varGuidanceScale)
        mGenerate.bind("clipSkip", vGenerate.varClipSkip)
        mGenerate.bind("promptFixedRatio", vGenerate.varPromptFixedRatio)
        mGenerate.bind("useLcm", vGenerate.varUseLcm)
        mGenerate.bind("useHalfVae", vGenerate.varUseHalfVae)
        mGenerate.bind("useXFormers", vGenerate.varUseXFormers)
