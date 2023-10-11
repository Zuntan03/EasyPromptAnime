import os
from const import Const, Path
from l10n import L10n
from collections import OrderedDict


class PromptTravel:
    defaultTemplate = """{{
    "name": "",
    "path": "{MODEL_PATH}",
    "vae_path": "{VAE_PATH}",
    "motion_module": "{MOTION_MODULE_PATH}",
    "compile": false,
    "seed": [{SEED}],
    "scheduler": "{SCHEDULER}",
    "steps": {STEPS},
    "guidance_scale": {GUIDANCE_SCALE},
    "clip_skip": {CLIP_SKIP},
    "prompt_fixed_ratio": {PROMPT_FIXED_RATIO},
    "head_prompt": "{HEADER_PROMPT}",
    "prompt_map": {{
{PROMPT_MAP}
    }},
    "tail_prompt": "{FOOTER_PROMPT}",
    "n_prompt": ["{NEGATIVE_PROMPT}"],
    "lora_map": {{
{LORA_MAP}
    }},
    "ip_adapter_map": {{
        "enable": {IP_ADAPTER_USE},
        "input_image_dir": "ip_adapter_image/{IP_ADAPTER_IMAGE_DIR}",
        "save_input_image": true,
        "scale": {IP_ADAPTER_SCALE},
        "is_plus_face": {IP_ADAPTER_USE_PLUS_FACE},
        "is_plus": {IP_ADAPTER_USE_PLUS}
    }},
    "upscale_config": {{
        "scheduler": "{UPSCALE_SCHEDULER}",
        "steps": {UPSCALE_STEPS},
        "strength": {UPSCALE_STRENGTH},
        "guidance_scale": {UPSCALE_GUIDANCE_SCALE},
        "controlnet_tile": {{
            "enable": true,
            "use_preprocessor": false,
            "controlnet_conditioning_scale": {UPSACLE_TILE_SCALE},
            "guess_mode": false,
            "control_guidance_start": {UPSACLE_TILE_START},
            "control_guidance_end": {UPSACLE_TILE_END}
        }}
    }},
    "output": {{
        "format": "mp4",
        "fps": {FPS},
        "encode_param": {{
            "crf": 20
        }}
    }}
}}
"""

    modelDir = os.path.join("models", "sd")
    motionModuleDir = os.path.join("models", "motion-module")
    vaeDir = "vae"

    @classmethod
    def loadTemplate(cls):
        if os.path.exists(Path.promptTravelTemplate):
            with open(Path.promptTravelTemplate, "r", encoding="utf-8-sig") as f:
                return f.read()
        else:
            with open(Path.promptTravelTemplate, "w", encoding="utf-8-sig") as f:
                f.write(PromptTravel.defaultTemplate)
            return PromptTravel.defaultTemplate

    @classmethod
    def getConfig(cls, generate, model, upscaleStrength, prompts, fps):
        modelPath = os.path.join(cls.modelDir, model).replace("\\", "/")

        motionModulePath = os.path.join(cls.motionModuleDir, generate.motionModule)
        motionModulePath = motionModulePath.replace("\\", "/")

        vaePath = os.path.join(cls.vaeDir, generate.vae).replace("\\", "/")

        promptMap = ""
        for frame, prompt in prompts["prompt_map"].items():
            if promptMap != "":
                promptMap += ",\n"
            promptMap += f'        "{frame}": "{prompt}"'

        loraMap = ""
        for loraName, loraWeight in prompts["lora_map"].items():
            if loraMap != "":
                loraMap += ",\n"
            loraMap += f'        "lora/{loraName}.safetensors": {loraWeight}'

        replaceDic = {
            "MODEL_PATH": modelPath,
            "VAE_PATH": vaePath,
            "MOTION_MODULE_PATH": motionModulePath,
            "SEED": generate.seed,
            "SCHEDULER": Const.getSchedulerValue(generate.scheduler),
            "STEPS": generate.steps,
            "GUIDANCE_SCALE": generate.guidanceScale,
            "CLIP_SKIP": generate.clipSkip,
            "PROMPT_FIXED_RATIO": generate.promptFixedRatio,
            "HEADER_PROMPT": prompts["header"],
            "PROMPT_MAP": promptMap,
            "FOOTER_PROMPT": prompts["footer"],
            "NEGATIVE_PROMPT": prompts["negative"],
            "LORA_MAP": loraMap,
            "UPSCALE_SCHEDULER": Const.getSchedulerValue(generate.upscaleScheduler),
            "UPSCALE_STEPS": generate.upscaleSteps,
            "UPSCALE_STRENGTH": upscaleStrength,
            "UPSCALE_GUIDANCE_SCALE": generate.upscaleGuidanceScale,
            "UPSACLE_TILE_SCALE": generate.upscaleTileScale,
            "UPSACLE_TILE_START": generate.upscaleTileStart,
            "UPSACLE_TILE_END": generate.upscaleTileEnd,
            "IP_ADAPTER_USE": str(generate.useIpAdapter).lower(),
            "IP_ADAPTER_IMAGE_DIR": generate.ipAdapterImageDir,
            "IP_ADAPTER_SCALE": generate.ipAdapterScale,
            "IP_ADAPTER_USE_PLUS_FACE": str(generate.useIpAdapterPlusFace).lower(),
            "IP_ADAPTER_USE_PLUS": str(generate.useIpAdapterPlus).lower(),
            "FPS": fps,
        }

        return PromptTravel.loadTemplate().format(**replaceDic)

    @classmethod
    def GetConfigFileSuffix(
        cls,
        length,
        context,
        width,
        height,
        useHalfVae,
        useXFormers,
        upscaleUseHalfVae,
        upscaleUseXFormers,
        upscale1Enabled=False,
        upscale1Mode=Const.tile,
        upscale1Height=0,
        upscale2Enabled=False,
        upscale2Mode=Const.tile,
        upscale2Height=0,
    ):
        fileSuffix = f"-L{length}-C{context}-W{width}-H{height}"
        fileSuffix += "-v" if useHalfVae else ""
        fileSuffix += "-x" if useXFormers else ""
        fileSuffix += "-V" if upscaleUseHalfVae else ""
        fileSuffix += "-X" if upscaleUseXFormers else ""
        if upscale1Enabled:
            if upscale1Mode == Const.tile:
                fileSuffix += f"-T{upscale1Height}"
            elif upscale1Mode == Const.refine:
                fileSuffix += f"-R{upscale1Height}"

            if upscale2Enabled:
                if upscale2Mode == Const.tile:
                    fileSuffix += f"-T{upscale2Height}"
                elif upscale2Mode == Const.refine:
                    fileSuffix += f"-R{upscale2Height}"
        return fileSuffix
