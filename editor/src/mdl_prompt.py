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
        self.original = ""
        self.prompts = {
            "header": "",
            "footer": "",
            "negative": "",
            "lora_map": {},
            "prompt_map": {},
            "errors": [],
        }
        self.subsc("original", self.updatePrompts)

    def updatePrompts(self, *args):
        self.prompts = PromptPerser.persePrompt(self.original)

    def getPreview(self, stert, length, showKeyframe, showHeaderFooter, showAnime):
        return PromptPerser.persePreview(
            self.prompts, stert, length, showKeyframe, showHeaderFooter, showAnime
        )

    def loadDefaultPrompt(self):
        if os.path.exists(Path.defaultPrompt):
            with open(Path.defaultPrompt, "r", encoding="utf-8-sig") as f:
                self.set("original", f.read())
        else:
            with open(Path.defaultPrompt, "w", encoding="utf-8-sig") as f:
                f.write(Prompt.defaultPrompt)
            self.set("original", Prompt.defaultPrompt)

    def saveDefaultPrompt(self):
        Prompt.defaultPrompt = self.original
        with open(Path.defaultPrompt, "w", encoding="utf-8-sig") as f:
            f.write(Prompt.defaultPrompt.strip() + "\n")

    def getLastPrompt(self):
        frames = sorted(self.prompts["prompt_map"].keys())
        length = len(frames)
        if length == 0:
            return (0, "")
        maxFrame = frames[length - 1]
        return (maxFrame, self.prompts["prompt_map"][maxFrame])
