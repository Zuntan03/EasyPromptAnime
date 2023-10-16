import tkinter as tk


class PreviewController:
    def __init__(self, form, model):
        self.form = form
        self.model = model

        mEdit = self.model.editor
        vPrev = self.form.preview
        mEdit.bind("previewShowKeyframe", vPrev.varShowKeyframe)
        mEdit.bind("previewShowHeaderFooter", vPrev.varShowHeaderFooter)
        mEdit.bind("previewShowAnime", vPrev.varShowAnime)

    def initEvents(self):
        self.initPreview()

    def initPreview(self):
        self.model.prompt.subsc("text", self.updatePerview)
        self.model.generate.subsc("length", self.updatePerview)

        mEdit = self.model.editor
        mEdit.subsc("previewShowKeyframe", self.updatePerview)
        mEdit.subsc("previewShowHeaderFooter", self.updatePerview)
        mEdit.subsc("previewShowAnime", self.updatePerview)
        mEdit.subsc("previewStart", self.updatePerview)
        mEdit.subsc("previewLength", self.updatePerview)

    def updatePerview(self, *args):
        mEdit = self.model.editor
        prevTxt = self.model.prompt.getPreview(
            mEdit.previewStart,
            self.model.getPreviewLength(),
            mEdit.previewShowKeyframe,
            mEdit.previewShowHeaderFooter,
            mEdit.previewShowAnime,
        )

        vTxtPrev = self.form.preview.txtPrev
        vTxtPrev.configure(state=tk.NORMAL)
        vTxtPrev.delete("1.0", tk.END)
        vTxtPrev.insert(tk.END, prevTxt)
        vTxtPrev.configure(state=tk.DISABLED)
