from mdl_prompt import Prompt
from mdl_generate import Generate
from mdl_editor import Editor


class Model:
    def __init__(self):
        self.prompt = Prompt()
        self.generate = Generate()
        self.editor = Editor()

    def notifyAll(self):
        self.prompt.notifyAll()
        self.generate.notifyAll()
        self.editor.notifyAll()

    @classmethod
    def loadConfig(cls):
        Generate.loadConfig()
        Editor.loadConfig()

    def storeConfig(self):
        self.generate.storeConfig()
        self.editor.storeConfig()

    def getPreviewLength(self):
        if self.editor.previewLength == 0:
            return self.generate.length - self.editor.previewStart
        else:
            return self.editor.previewLength

    def getPreviewEnd(self):
        if self.editor.previewLength == 0:
            return self.generate.length
        else:
            return self.editor.previewStart + self.editor.previewLength
