import os
from const import Const, Path, ControlNetType
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
    "controlnet_map": {{
        "input_image_dir" : "controlnet_image/{CONTROLNET_DIR}",
        "max_samples_on_vram" : 2,
        "max_models_on_vram" : 1,
        "save_detectmap" : true,
        "preprocess_on_gpu": true,
        "is_loop": {CONTROLNET_IS_LOOP},
        "controlnet_canny": {{
            "enable": {canny_ENABLE},
            "use_preprocessor": {canny_USE_PREPROCESSOR},
            "guess_mode": {canny_GUESS_MODE},
            "controlnet_conditioning_scale": {canny_SCALE},
            "control_guidance_start": {canny_START},
            "control_guidance_end": {canny_END},
            "control_scale_list": [{canny_SCALE_LIST}]
        }},
        "controlnet_depth": {{
            "enable": {depth_ENABLE},
            "use_preprocessor": {depth_USE_PREPROCESSOR},
            "guess_mode": {depth_GUESS_MODE},
            "controlnet_conditioning_scale": {depth_SCALE},
            "control_guidance_start": {depth_START},
            "control_guidance_end": {depth_END},
            "control_scale_list": [{depth_SCALE_LIST}]
        }},
        "controlnet_inpaint": {{
            "enable": {inpaint_ENABLE},
            "use_preprocessor": {inpaint_USE_PREPROCESSOR},
            "guess_mode": {inpaint_GUESS_MODE},
            "controlnet_conditioning_scale": {inpaint_SCALE},
            "control_guidance_start": {inpaint_START},
            "control_guidance_end": {inpaint_END},
            "control_scale_list": [{inpaint_SCALE_LIST}]
        }},
        "controlnet_ip2p": {{
            "enable": {ip2p_ENABLE},
            "use_preprocessor": {ip2p_USE_PREPROCESSOR},
            "guess_mode": {ip2p_GUESS_MODE},
            "controlnet_conditioning_scale": {ip2p_SCALE},
            "control_guidance_start": {ip2p_START},
            "control_guidance_end": {ip2p_END},
            "control_scale_list": [{ip2p_SCALE_LIST}]
        }},
        "controlnet_lineart": {{
            "enable": {lineart_ENABLE},
            "use_preprocessor": {lineart_USE_PREPROCESSOR},
            "guess_mode": {lineart_GUESS_MODE},
            "controlnet_conditioning_scale": {lineart_SCALE},
            "control_guidance_start": {lineart_START},
            "control_guidance_end": {lineart_END},
            "control_scale_list": [{lineart_SCALE_LIST}]
        }},
        "controlnet_lineart_anime": {{
            "enable": {lineart_anime_ENABLE},
            "use_preprocessor": {lineart_anime_USE_PREPROCESSOR},
            "guess_mode": {lineart_anime_GUESS_MODE},
            "controlnet_conditioning_scale": {lineart_anime_SCALE},
            "control_guidance_start": {lineart_anime_START},
            "control_guidance_end": {lineart_anime_END},
            "control_scale_list": [{lineart_anime_SCALE_LIST}]
        }},
        "controlnet_mlsd": {{
            "enable": {mlsd_ENABLE},
            "use_preprocessor": {mlsd_USE_PREPROCESSOR},
            "guess_mode": {mlsd_GUESS_MODE},
            "controlnet_conditioning_scale": {mlsd_SCALE},
            "control_guidance_start": {mlsd_START},
            "control_guidance_end": {mlsd_END},
            "control_scale_list": [{mlsd_SCALE_LIST}]
        }},
        "controlnet_normalbae": {{
            "enable": {normalbae_ENABLE},
            "use_preprocessor": {normalbae_USE_PREPROCESSOR},
            "guess_mode": {normalbae_GUESS_MODE},
            "controlnet_conditioning_scale": {normalbae_SCALE},
            "control_guidance_start": {normalbae_START},
            "control_guidance_end": {normalbae_END},
            "control_scale_list": [{normalbae_SCALE_LIST}]
        }},
        "controlnet_openpose": {{
            "enable": {openpose_ENABLE},
            "use_preprocessor": {openpose_USE_PREPROCESSOR},
            "guess_mode": {openpose_GUESS_MODE},
            "controlnet_conditioning_scale": {openpose_SCALE},
            "control_guidance_start": {openpose_START},
            "control_guidance_end": {openpose_END},
            "control_scale_list": [{openpose_SCALE_LIST}]
        }},
        "controlnet_scribble": {{
            "enable": {scribble_ENABLE},
            "use_preprocessor": {scribble_USE_PREPROCESSOR},
            "guess_mode": {scribble_GUESS_MODE},
            "controlnet_conditioning_scale": {scribble_SCALE},
            "control_guidance_start": {scribble_START},
            "control_guidance_end": {scribble_END},
            "control_scale_list": [{scribble_SCALE_LIST}]
        }},
        "controlnet_seg": {{
            "enable": {seg_ENABLE},
            "use_preprocessor": {seg_USE_PREPROCESSOR},
            "guess_mode": {seg_GUESS_MODE},
            "controlnet_conditioning_scale": {seg_SCALE},
            "control_guidance_start": {seg_START},
            "control_guidance_end": {seg_END},
            "control_scale_list": [{seg_SCALE_LIST}]
        }},
        "controlnet_shuffle": {{
            "enable": {shuffle_ENABLE},
            "use_preprocessor": {shuffle_USE_PREPROCESSOR},
            "guess_mode": {shuffle_GUESS_MODE},
            "controlnet_conditioning_scale": {shuffle_SCALE},
            "control_guidance_start": {shuffle_START},
            "control_guidance_end": {shuffle_END},
            "control_scale_list": [{shuffle_SCALE_LIST}]
        }},
        "controlnet_softedge": {{
            "enable": {softedge_ENABLE},
            "use_preprocessor": {softedge_USE_PREPROCESSOR},
            "guess_mode": {softedge_GUESS_MODE},
            "controlnet_conditioning_scale": {softedge_SCALE},
            "control_guidance_start": {softedge_START},
            "control_guidance_end": {softedge_END},
            "control_scale_list": [{softedge_SCALE_LIST}]
        }},
        "controlnet_tile": {{
            "enable": {tile_ENABLE},
            "use_preprocessor": {tile_USE_PREPROCESSOR},
            "guess_mode": {tile_GUESS_MODE},
            "controlnet_conditioning_scale": {tile_SCALE},
            "control_guidance_start": {tile_START},
            "control_guidance_end": {tile_END},
            "control_scale_list": [{tile_SCALE_LIST}]
        }}
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
    def getConfig(cls, generate, model, upscaleStrength, promptData, fps):
        modelPath = os.path.join(cls.modelDir, model).replace("\\", "/")

        motionModulePath = os.path.join(cls.motionModuleDir, generate.motionModule)
        motionModulePath = motionModulePath.replace("\\", "/")

        vaePath = os.path.join(cls.vaeDir, generate.vae).replace("\\", "/")

        promptMap = ""
        for frame, prompt in promptData["prompt_map"].items():
            if promptMap != "":
                promptMap += ",\n"
            promptMap += f'        "{frame}": "{prompt}"'

        loraMap = ""
        for loraName, loraWeight in promptData["lora_map"].items():
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
            "HEADER_PROMPT": promptData["header"],
            "PROMPT_MAP": promptMap,
            "FOOTER_PROMPT": promptData["footer"],
            "NEGATIVE_PROMPT": promptData["negative"],
            "LORA_MAP": loraMap,
            "CONTROLNET_IS_LOOP": str(generate.controlNetLoop).lower(),
            "CONTROLNET_DIR": generate.controlNetDir,
            "IP_ADAPTER_USE": str(generate.useIpAdapter).lower(),
            "IP_ADAPTER_IMAGE_DIR": generate.ipAdapterImageDir,
            "IP_ADAPTER_SCALE": generate.ipAdapterScale,
            "IP_ADAPTER_USE_PLUS_FACE": str(generate.useIpAdapterPlusFace).lower(),
            "IP_ADAPTER_USE_PLUS": str(generate.useIpAdapterPlus).lower(),
            "UPSCALE_SCHEDULER": Const.getSchedulerValue(generate.upscaleScheduler),
            "UPSCALE_STEPS": generate.upscaleSteps,
            "UPSCALE_STRENGTH": upscaleStrength,
            "UPSCALE_GUIDANCE_SCALE": generate.upscaleGuidanceScale,
            "UPSACLE_TILE_SCALE": generate.upscaleTileScale,
            "UPSACLE_TILE_START": generate.upscaleTileStart,
            "UPSACLE_TILE_END": generate.upscaleTileEnd,
            "FPS": fps,
        }

        for cnType in ControlNetType:
            replaceDic[f"{cnType.name}_ENABLE"] = str(
                getattr(generate, f"cnEnable_{cnType.name}")
            ).lower()
            replaceDic[f"{cnType.name}_USE_PREPROCESSOR"] = str(
                getattr(generate, f"cnUsePreprocessor_{cnType.name}")
            ).lower()
            replaceDic[f"{cnType.name}_GUESS_MODE"] = str(
                getattr(generate, f"cnGuessMode_{cnType.name}")
            ).lower()
            replaceDic[f"{cnType.name}_SCALE"] = getattr(
                generate, f"cnScale_{cnType.name}"
            )
            replaceDic[f"{cnType.name}_START"] = getattr(
                generate, f"cnStart_{cnType.name}"
            )
            replaceDic[f"{cnType.name}_END"] = getattr(generate, f"cnEnd_{cnType.name}")
            replaceDic[f"{cnType.name}_SCALE_LIST"] = getattr(
                generate, f"cnScaleList_{cnType.name}"
            )

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
