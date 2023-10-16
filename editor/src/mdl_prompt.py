from const import Path
from mdl_notifier import Notifier
import os
from prompt_perser import PromptPerser


class Prompt(Notifier):
    defaultPrompt = """H: crowds, akihabara
 0: standing, upset
10: waving at viewer, surprised
20: waving at viewer, smile
F: 1girl, maid outfit
N:(worst quality, low quality:1.2)
"""

    def __init__(self):
        super().__init__()
        self.text = ""
        self.data = {
            "header": "",
            "footer": "",
            "negative": "",
            "lora_map": {},
            "prompt_map": {},
            "errors": [],
        }
        self.subsc("text", self.updatePrompts)

    def updatePrompts(self, *args):
        self.data = PromptPerser.persePrompt(self.text)

    def getPreview(self, stert, length, showKeyframe, showHeaderFooter, showAnime):
        return PromptPerser.persePreview(
            self.data, stert, length, showKeyframe, showHeaderFooter, showAnime
        )

    def loadDefaultPrompt(self):
        if os.path.exists(Path.defaultPrompt):
            with open(Path.defaultPrompt, "r", encoding="utf-8-sig") as f:
                self.set("text", f.read())
        else:
            with open(Path.defaultPrompt, "w", encoding="utf-8-sig") as f:
                f.write(Prompt.defaultPrompt)
            self.set("text", Prompt.defaultPrompt)

    def saveDefaultPrompt(self):
        Prompt.defaultPrompt = self.text
        with open(Path.defaultPrompt, "w", encoding="utf-8-sig") as f:
            f.write(Prompt.defaultPrompt.strip() + "\n")

    def getLastPrompt(self):
        frames = sorted(self.data["prompt_map"].keys())
        length = len(frames)
        if length == 0:
            return (0, "")
        maxFrame = frames[length - 1]
        return (maxFrame, self.data["prompt_map"][maxFrame])
