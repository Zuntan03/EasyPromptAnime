from l10n import L10n
from collections import OrderedDict


class PromptPerser:
    @classmethod
    def persePrompt(cls, txt):
        prompts = {
            "header": "",
            "footer": "",
            "negative": "",
            "lora_map": {},
            "prompt_map": {},
            "errors": [],
        }

        for line in txt.splitlines():
            try:
                cls.perseLine(prompts, line)
            except Exception as e:
                prompts["errors"].append(str(e))

        # TODO: apply range prompt
        return prompts

    @classmethod
    def perseLine(cls, prompts, line):
        commentRemoved = line.split("#", 1)[0].strip()
        if commentRemoved == "":
            return
        commentRemovedKvp = commentRemoved.split(":", 1)
        stripedKey = commentRemovedKvp[0].strip()
        if len(commentRemovedKvp) < 2:
            cls.addPrompt(prompts, 0, stripedKey)  # 0 frame prompt
            return
        val = commentRemovedKvp[1].strip()
        if stripedKey == "":
            cls.addPrompt(prompts, 0, val)  # 0 frame prompt
            return
        key = stripedKey.lower()
        if key == "h":
            if prompts["header"] != "":
                prompts["header"] += ", "
            prompts["header"] += val
        elif key == "f":
            if prompts["footer"] != "":
                prompts["footer"] += ", "
            prompts["footer"] += val
        elif key == "n":
            if prompts["negative"] != "":
                prompts["negative"] += ", "
            prompts["negative"] += val
        elif key == "l":
            for lora_def in val.split(","):
                lora_kvp = lora_def.split(":", 1)
                if len(lora_kvp) < 2:
                    prompts["errors"].append(
                        L10n.format("err_inv_lora_def", lora_def, val)
                    )
                    return
                lora_key = lora_kvp[0].strip()
                lora_weight = lora_kvp[1].strip()
                try:
                    lora_weight = float(lora_weight)
                    prompts["lora_map"][lora_key] = lora_weight
                except ValueError:
                    prompts["errors"].append(
                        L10n.format("err_inv_lora_def", lora_def, val)
                    )
                    return
        elif key.isdigit():
            cls.addPrompt(prompts, int(key), val)
        else:
            # TODO: parse range prompt
            prompts["errors"].append(L10n.format("err_inv_line", line))

    @classmethod
    def addPrompt(self, prompts, frame, prompt):
        if not isinstance(frame, int) or frame < 0:
            prompts["errors"].append(L10n.format("err_inv_frame_num", frame, prompt))
            return

        promptMap = prompts["prompt_map"]
        if frame in promptMap:
            promptMap[frame] = f"{promptMap[frame]}, {prompt}"
        else:
            promptMap[frame] = prompt

    @classmethod
    def persePreview(
        cls, prompts, start, length, showKeyframe, showHeaderFooter, showAnime
    ):
        preview = []
        header = prompts["header"]
        header = (header + ", ") if header != "" else header

        footer = prompts["footer"]
        footer = (", " + footer) if footer != "" else footer

        end = start + length
        firstPrompt = ""
        preFrame = -1
        prePrompt = ""
        for frame in range(start, end + 1):
            if frame in prompts["prompt_map"]:
                prompt = prompts["prompt_map"][frame]
                if firstPrompt == "":
                    firstPrompt = prompt
                else:
                    if showAnime:
                        preview.append(
                            f"{preFrame:>3}-{frame:>2}: ({cls.diffPrompt(prePrompt, prompt)}: 0.5)"
                        )
                if showKeyframe:
                    if showHeaderFooter:
                        preview.append(f"{frame:>3}: {header}{prompt}{footer}")
                    else:
                        preview.append(f"{frame:>3}: {prompt}")
                preFrame = frame
                prePrompt = prompt
        if firstPrompt != "" and showAnime:
            preview.append(
                f"{preFrame:>3}-{start:>2}: ({cls.diffPrompt(prePrompt, firstPrompt)}: 0.5)"
            )

        negative = prompts["negative"]
        if negative != "":
            preview.append(f"{L10n.get('negative_prompt')}: {negative}")

        loras = prompts["lora_map"].keys()
        if len(loras) > 0:
            loraDefs = "LoRA: "
            for lora in loras:
                loraDefs += f"<{lora}: {prompts['lora_map'][lora]}> "
            preview.append(loraDefs)

        for err in prompts["errors"]:
            preview.append(f"{L10n.get('error')}: {err}")

        return "\n".join(preview)

    @classmethod
    def diffPrompt(cls, prePrompt, postPrompt):
        preSet = set(map(str.strip, prePrompt.split(",")))
        postSet = set(map(str.strip, postPrompt.split(",")))
        uniqueSet = preSet.symmetric_difference(postSet)
        return ", ".join(uniqueSet)  # + f" | {prePrompt} | {postPrompt}"
