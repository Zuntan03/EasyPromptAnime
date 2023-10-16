from l10n import L10n
from collections import OrderedDict


class PromptPerser:
    @classmethod
    def persePrompt(cls, txt):
        data = {
            "header": "",
            "footer": "",
            "negative": "",
            "lora_map": {},
            "prompt_map": {},
            "errors": [],
        }

        for line in txt.splitlines():
            try:
                cls.perseLine(data, line)
            except Exception as e:
                data["errors"].append(str(e))

        # TODO: apply range prompt
        return data

    @classmethod
    def perseLine(cls, data, line):
        commentRemoved = line.split("#", 1)[0].strip()
        if commentRemoved == "":
            return
        commentRemovedKvp = commentRemoved.split(":", 1)
        stripedKey = commentRemovedKvp[0].strip()
        if len(commentRemovedKvp) < 2:
            cls.addPrompt(data, 0, stripedKey)  # 0 frame prompt
            return
        val = commentRemovedKvp[1].strip()
        if stripedKey == "":
            cls.addPrompt(data, 0, val)  # 0 frame prompt
            return
        key = stripedKey.lower()
        if key == "h":
            if data["header"] != "":
                data["header"] += ", "
            data["header"] += val
        elif key == "f":
            if data["footer"] != "":
                data["footer"] += ", "
            data["footer"] += val
        elif key == "n":
            if data["negative"] != "":
                data["negative"] += ", "
            data["negative"] += val
        elif key == "l":
            for lora_def in val.split(","):
                lora_kvp = lora_def.split(":", 1)
                if len(lora_kvp) < 2:
                    data["errors"].append(
                        L10n.format("err_inv_lora_def", lora_def, val)
                    )
                    return
                lora_key = lora_kvp[0].strip()
                lora_weight = lora_kvp[1].strip()
                try:
                    lora_weight = float(lora_weight)
                    data["lora_map"][lora_key] = lora_weight
                except ValueError:
                    data["errors"].append(
                        L10n.format("err_inv_lora_def", lora_def, val)
                    )
                    return
        elif key.isdigit():
            cls.addPrompt(data, int(key), val)
        else:
            # TODO: parse range prompt
            data["errors"].append(L10n.format("err_inv_line", line))

    @classmethod
    def addPrompt(self, data, frame, prompt):
        if not isinstance(frame, int) or frame < 0:
            data["errors"].append(L10n.format("err_inv_frame_num", frame, prompt))
            return

        promptMap = data["prompt_map"]
        if frame in promptMap:
            promptMap[frame] = f"{promptMap[frame]}, {prompt}"
        else:
            promptMap[frame] = prompt

    @classmethod
    def persePreview(
        cls, data, start, length, showKeyframe, showHeaderFooter, showAnime
    ):
        preview = []
        header = data["header"]
        header = (header + ", ") if header != "" else header

        footer = data["footer"]
        footer = (", " + footer) if footer != "" else footer

        end = start + length
        firstPrompt = ""
        preFrame = -1
        prePrompt = ""
        for frame in range(start, end + 1):
            if frame in data["prompt_map"]:
                prompt = data["prompt_map"][frame]
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

        negative = data["negative"]
        if negative != "":
            preview.append(f"{L10n.get('negative_prompt')}: {negative}")

        loras = data["lora_map"].keys()
        if len(loras) > 0:
            loraDefs = "LoRA: "
            for lora in loras:
                loraDefs += f"<{lora}: {data['lora_map'][lora]}> "
            preview.append(loraDefs)

        for err in data["errors"]:
            preview.append(f"{L10n.get('error')}: {err}")

        return "\n".join(preview)

    @classmethod
    def diffPrompt(cls, prePrompt, postPrompt):
        preSet = set(map(str.strip, prePrompt.split(",")))
        postSet = set(map(str.strip, postPrompt.split(",")))
        uniqueSet = preSet.symmetric_difference(postSet)
        return ", ".join(uniqueSet)  # + f" | {prePrompt} | {postPrompt}"
