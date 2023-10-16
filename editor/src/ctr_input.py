import tkinter as tk
from l10n import L10n
from task import Task
from tsk_generate import GenerateTask


class InputController:
    def __init__(self, form, model):
        self.form = form
        self.model = model

        vInput = self.form.input
        self.model.prompt.subsc("text", self.setTxtInput)
        vInput.txtInput.bind("<<Modified>>", self.modifiedTxtInput)
        self.bindKeyboardShortcuts()

        mEdit = self.model.editor
        mEdit.bind("previewUpscale", vInput.varUpscale)
        # mEdit.bind("previewInterpolation", vInput.varInterpolation)
        mEdit.bind("previewStart", vInput.varStart)
        mEdit.bind("previewLength", vInput.varLength)

        mEdit.bind("taskForever", vInput.varForever)
        mEdit.bind("taskPauseByError", vInput.varPauseByError)

        vInput.btnGenerate.configure(command=self.onGenerate)
        vInput.btnSeedGacha.configure(command=self.onSeedGacha)
        vInput.btnPreview.configure(command=self.onPreview)

    def setTxtInput(self, *args):
        vTxtInput = self.form.input.txtInput
        mOriginal = self.model.prompt.text
        if mOriginal == vTxtInput.get("1.0", tk.END):
            return
        vTxtInput.delete("1.0", tk.END)
        vTxtInput.insert(tk.END, mOriginal)

    def modifiedTxtInput(self, *args):
        vTxtInput = self.form.input.txtInput
        self.model.prompt.set("text", vTxtInput.get("1.0", tk.END))
        vTxtInput.edit_modified(False)

    def bindKeyboardShortcuts(self):
        pass  # TODO: txtInput shortcuts

    def onGenerate(self):
        GenerateTask.generate(self.model)

    def onSeedGacha(self):
        GenerateTask.seedGacha(self.model)

    def onPreview(self):
        GenerateTask.preview(self.model)

    def initEvents(self):
        self.model.editor.subsc("previewStart", self.onPreviewStartChanged)
        self.model.editor.subsc("previewLength", self.onPreviewLengthChanged)
        self.model.generate.subsc("length", self.onLengthChanged)

    def onPreviewStartChanged(self, *args):
        lengthTo = self.model.generate.length - self.model.editor.previewStart
        self.form.input.sliLength.configure(to=lengthTo)
        self.updatePreviewLengthLbl()

    def onPreviewLengthChanged(self, *args):
        startTo = self.model.generate.length - self.model.editor.previewLength
        self.form.input.sliStart.configure(to=startTo)
        self.updatePreviewLengthLbl()

    def onLengthChanged(self, *args):
        startTo = self.model.generate.length - self.model.editor.previewLength
        self.form.input.sliStart.configure(to=startTo)
        lengthTo = self.model.generate.length - self.model.editor.previewStart
        self.form.input.sliLength.configure(to=lengthTo)
        self.updatePreviewLengthLbl()

    def updatePreviewLengthLbl(self):
        start = int(self.model.editor.previewStart / 10)
        end = int(self.model.getPreviewEnd() / 10)
        lbl = f"{L10n.get('preview_length')}{start}-{end}{L10n.get('sec')}"
        self.form.input.lblLength.configure(text=lbl)
