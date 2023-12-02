from const import ControlNetType


class Serializer:
    versionKey = "easy_prompt_anime_version"
    varsion = "0.4.1"

    @classmethod
    def deserialize(cls, model, data):
        while True:
            version = data[cls.versionKey]
            if version == cls.varsion:
                break
            if version not in cls.updator:
                return False
            data = cls.updator[version](model, data)

        model.prompt.set("text", data["prompt"])
        cls.deserializeGenerate(model.generate, data["generate"])
        cls.deserializeEditor(model.editor, data["editor"])
        return True

    @classmethod
    def deserializeGenerate(cls, generate, data):
        generate.set("length", data["length"])
        generate.set("model", data["model"])
        generate.set("vae", data["vae"])
        generate.set("motionModule", data["motion_module"])
        generate.set("context", data["context"])
        generate.set("scheduler", data["scheduler"])
        generate.set("steps", data["steps"])
        generate.set("guidanceScale", data["guidance_scale"])
        generate.set("clipSkip", data["clip_skip"])
        generate.set("promptFixedRatio", data["prompt_fixed_ratio"])
        generate.set("useLcm", data["use_lcm"])
        generate.set("useHalfVae", data["use_half_vae"])
        generate.set("useXFormers", data["use_x_formers"])
        generate.set("width", data["width"])
        generate.set("height", data["height"])
        generate.set("seed", data["seed"])
        generate.set("controlNetDir", data["control_net_dir"])
        generate.set("controlNetLoop", data["control_net_loop"])

        for cnType in ControlNetType:
            generate.set(f"cnEnable_{cnType.name}", data[f"{cnType.name}_enable"])
            generate.set(
                f"cnUsePreprocessor_{cnType.name}",
                data[f"{cnType.name}_use_preprocessor"],
            )
            generate.set(
                f"cnGuessMode_{cnType.name}", data[f"{cnType.name}_guess_mode"]
            )
            generate.set(f"cnScale_{cnType.name}", data[f"{cnType.name}_scale"])
            generate.set(
                f"cnScaleList_{cnType.name}", data[f"{cnType.name}_scale_list"]
            )
            generate.set(f"cnStart_{cnType.name}", data[f"{cnType.name}_start"])
            generate.set(f"cnEnd_{cnType.name}", data[f"{cnType.name}_end"])

        generate.set("useIpAdapter", data["use_ip_adapter"])
        generate.set("useIpAdapterPlus", data["use_ip_adapter_plus"])
        generate.set("useIpAdapterPlusFace", data["use_ip_adapter_plus_face"])
        generate.set("ipAdapterScale", data["ip_adapter_scale"])
        generate.set("ipAdapterImageDir", data["ip_adapter_image_dir"])

        generate.set("upscale1Enabled", data["upscale1_enabled"])
        generate.set("upscale1Mode", data["upscale1_mode"])
        generate.set("upscale1Scale", data["upscale1_scale"])

        generate.set("upscale2Enabled", data["upscale2_enabled"])
        generate.set("upscale2Mode", data["upscale2_mode"])
        generate.set("upscale2Scale", data["upscale2_scale"])

        generate.set("upscaleScheduler", data["upscale_scheduler"])
        generate.set("upscaleSteps", data["upscale_steps"])
        generate.set("upscaleGuidanceScale", data["upscale_guidance_scale"])
        generate.set("upscaleStrength", data["upscale_strength"])
        generate.set("upscaleTileEnable", data["upscale_tile_enable"])
        generate.set("upscaleTileScale", data["upscale_tile_scale"])
        generate.set("upscaleTileStart", data["upscale_tile_start"])
        generate.set("upscaleTileEnd", data["upscale_tile_end"])
        generate.set("upscaleIp2pEnable", data["upscale_ip2p_enable"])
        generate.set("upscaleIp2pScale", data["upscale_ip2p_scale"])
        generate.set("upscaleIp2pStart", data["upscale_ip2p_start"])
        generate.set("upscaleIp2pEnd", data["upscale_ip2p_end"])
        generate.set("upscaleLineAnimeEnable", data["upscale_line_anime_enable"])
        generate.set("upscaleLineAnimeScale", data["upscale_line_anime_scale"])
        generate.set("upscaleLineAnimeStart", data["upscale_line_anime_start"])
        generate.set("upscaleLineAnimeEnd", data["upscale_line_anime_end"])
        generate.set("upscaleUseHalfVae", data["upscale_use_half_vae"])
        generate.set("upscaleUseXFormers", data["upscale_use_x_formers"])

        generate.set("mosaicEnabled", data["mosaic_enabled"])
        generate.set("mosaicThreshold", data["mosaic_threshold"])
        generate.set("temporalMosaic", data["temporal_mosaic"])
        generate.set("ellipseMosaic", data["ellipse_mosaic"])
        generate.set("mosaicMaskBlur", data["mosaic_mask_blur"])
        generate.set("mosaicFemFace", data["mosaic_fem_face"])
        generate.set("mosaicFemBrst", data["mosaic_fem_brst"])
        generate.set("mosaicFemBrstCov", data["mosaic_fem_brst_cov"])
        generate.set("mosaicFemGntl", data["mosaic_fem_gntl"])
        generate.set("mosaicFemGntlCov", data["mosaic_fem_gntl_cov"])
        generate.set("mosaicMaleFace", data["mosaic_male_face"])
        generate.set("mosaicMaleBrst", data["mosaic_male_brst"])
        generate.set("mosaicMaleGntl", data["mosaic_male_gntl"])
        generate.set("mosaicArmpit", data["mosaic_armpit"])
        generate.set("mosaicArmpitCov", data["mosaic_armpit_cov"])
        generate.set("mosaicBelly", data["mosaic_belly"])
        generate.set("mosaicBellyCov", data["mosaic_belly_cov"])
        generate.set("mosaicHip", data["mosaic_hip"])
        generate.set("mosaicHipCov", data["mosaic_hip_cov"])
        generate.set("mosaicAns", data["mosaic_ans"])
        generate.set("mosaicAnsCov", data["mosaic_ans_cov"])
        generate.set("mosaicFeet", data["mosaic_feet"])
        generate.set("mosaicFeetCov", data["mosaic_feet_cov"])
        generate.set("mosaicScaleTop", data["mosaic_scale_top"])
        generate.set("mosaicScaleBottom", data["mosaic_scale_bottom"])
        generate.set("mosaicScaleLeft", data["mosaic_scale_left"])
        generate.set("mosaicScaleRight", data["mosaic_scale_right"])
        generate.set("mosaicIgnoreTop", data["mosaic_ignore_top"])
        generate.set("mosaicIgnoreBottom", data["mosaic_ignore_bottom"])
        generate.set("mosaicIgnoreLeft", data["mosaic_ignore_left"])
        generate.set("mosaicIgnoreRight", data["mosaic_ignore_right"])

    @classmethod
    def deserializeEditor(cls, editor, data):
        editor.set("previewUpscale", data["upscale"])
        editor.set("previewStart", data["start"])
        editor.set("previewLength", data["length"])
        editor.set("previewShowKeyframe", data["show_keyframe"])
        editor.set("previewShowHeaderFooter", data["show_header_footer"])
        editor.set("previewShowAnime", data["show_anime"])
        editor.set("taskForever", data["taskForever"])
        editor.set("taskPauseByError", data["taskPauseByError"])
        editor.set("importSpeed", data["importSpeed"])
        editor.set("importStart", data["importStart"])
        editor.set("importLength", data["importLength"])
        editor.set("importIndex", data["importIndex"])

    @classmethod
    def serialize(cls, model):
        data = {
            cls.versionKey: cls.varsion,
            "prompt": model.prompt.text,
            "generate": cls.serializeGenerate(model.generate),
            "editor": cls.serializeEditor(model.editor),
        }
        return data

    @classmethod
    def serializeGenerate(cls, generate):
        result = {
            "length": generate.length,
            "model": generate.model,
            "vae": generate.vae,
            "motion_module": generate.motionModule,
            "context": generate.context,
            "scheduler": generate.scheduler,
            "steps": generate.steps,
            "guidance_scale": generate.guidanceScale,
            "clip_skip": generate.clipSkip,
            "prompt_fixed_ratio": generate.promptFixedRatio,
            "use_lcm": generate.useLcm,
            "use_half_vae": generate.useHalfVae,
            "use_x_formers": generate.useXFormers,
            "width": generate.width,
            "height": generate.height,
            "seed": generate.seed,
            "control_net_dir": generate.controlNetDir,
            "control_net_loop": generate.controlNetLoop,
        }

        for cnType in ControlNetType:
            result[f"{cnType.name}_enable"] = getattr(
                generate, f"cnEnable_{cnType.name}"
            )
            result[f"{cnType.name}_use_preprocessor"] = getattr(
                generate, f"cnUsePreprocessor_{cnType.name}"
            )
            result[f"{cnType.name}_guess_mode"] = getattr(
                generate, f"cnGuessMode_{cnType.name}"
            )
            result[f"{cnType.name}_scale"] = getattr(generate, f"cnScale_{cnType.name}")
            result[f"{cnType.name}_scale_list"] = getattr(
                generate, f"cnScaleList_{cnType.name}"
            )
            result[f"{cnType.name}_start"] = getattr(generate, f"cnStart_{cnType.name}")
            result[f"{cnType.name}_end"] = getattr(generate, f"cnEnd_{cnType.name}")

        result["use_ip_adapter"] = generate.useIpAdapter
        result["use_ip_adapter_plus"] = generate.useIpAdapterPlus
        result["use_ip_adapter_plus_face"] = generate.useIpAdapterPlusFace
        result["ip_adapter_scale"] = generate.ipAdapterScale
        result["ip_adapter_image_dir"] = generate.ipAdapterImageDir

        result["upscale1_enabled"] = generate.upscale1Enabled
        result["upscale1_mode"] = generate.upscale1Mode
        result["upscale1_scale"] = generate.upscale1Scale

        result["upscale2_enabled"] = generate.upscale2Enabled
        result["upscale2_mode"] = generate.upscale2Mode
        result["upscale2_scale"] = generate.upscale2Scale

        result["upscale_scheduler"] = generate.upscaleScheduler
        result["upscale_steps"] = generate.upscaleSteps
        result["upscale_guidance_scale"] = generate.upscaleGuidanceScale
        result["upscale_strength"] = generate.upscaleStrength
        result["upscale_tile_enable"] = generate.upscaleTileEnable
        result["upscale_tile_scale"] = generate.upscaleTileScale
        result["upscale_tile_start"] = generate.upscaleTileStart
        result["upscale_tile_end"] = generate.upscaleTileEnd
        result["upscale_ip2p_enable"] = generate.upscaleIp2pEnable
        result["upscale_ip2p_scale"] = generate.upscaleIp2pScale
        result["upscale_ip2p_start"] = generate.upscaleIp2pStart
        result["upscale_ip2p_end"] = generate.upscaleIp2pEnd
        result["upscale_line_anime_enable"] = generate.upscaleLineAnimeEnable
        result["upscale_line_anime_scale"] = generate.upscaleLineAnimeScale
        result["upscale_line_anime_start"] = generate.upscaleLineAnimeStart
        result["upscale_line_anime_end"] = generate.upscaleLineAnimeEnd
        result["upscale_use_half_vae"] = generate.upscaleUseHalfVae
        result["upscale_use_x_formers"] = generate.upscaleUseXFormers

        result["mosaic_enabled"] = generate.mosaicEnabled
        result["mosaic_threshold"] = generate.mosaicThreshold
        result["temporal_mosaic"] = generate.temporalMosaic
        result["ellipse_mosaic"] = generate.ellipseMosaic
        result["mosaic_mask_blur"] = generate.mosaicMaskBlur
        result["mosaic_fem_face"] = generate.mosaicFemFace
        result["mosaic_fem_brst"] = generate.mosaicFemBrst
        result["mosaic_fem_brst_cov"] = generate.mosaicFemBrstCov
        result["mosaic_fem_gntl"] = generate.mosaicFemGntl
        result["mosaic_fem_gntl_cov"] = generate.mosaicFemGntlCov
        result["mosaic_male_face"] = generate.mosaicMaleFace
        result["mosaic_male_brst"] = generate.mosaicMaleBrst
        result["mosaic_male_gntl"] = generate.mosaicMaleGntl
        result["mosaic_armpit"] = generate.mosaicArmpit
        result["mosaic_armpit_cov"] = generate.mosaicArmpitCov
        result["mosaic_belly"] = generate.mosaicBelly
        result["mosaic_belly_cov"] = generate.mosaicBellyCov
        result["mosaic_hip"] = generate.mosaicHip
        result["mosaic_hip_cov"] = generate.mosaicHipCov
        result["mosaic_ans"] = generate.mosaicAns
        result["mosaic_ans_cov"] = generate.mosaicAnsCov
        result["mosaic_feet"] = generate.mosaicFeet
        result["mosaic_feet_cov"] = generate.mosaicFeetCov
        result["mosaic_scale_top"] = generate.mosaicScaleTop
        result["mosaic_scale_bottom"] = generate.mosaicScaleBottom
        result["mosaic_scale_left"] = generate.mosaicScaleLeft
        result["mosaic_scale_right"] = generate.mosaicScaleRight
        result["mosaic_ignore_top"] = generate.mosaicIgnoreTop
        result["mosaic_ignore_bottom"] = generate.mosaicIgnoreBottom
        result["mosaic_ignore_left"] = generate.mosaicIgnoreLeft
        result["mosaic_ignore_right"] = generate.mosaicIgnoreRight

        return result

    @classmethod
    def serializeEditor(cls, editor):
        return {
            "upscale": editor.previewUpscale,
            "start": editor.previewStart,
            "length": editor.previewLength,
            "show_keyframe": editor.previewShowKeyframe,
            "show_header_footer": editor.previewShowHeaderFooter,
            "show_anime": editor.previewShowAnime,
            "taskForever": editor.taskForever,
            "taskPauseByError": editor.taskPauseByError,
            "importSpeed": editor.importSpeed,
            "importStart": editor.importStart,
            "importLength": editor.importLength,
            "importIndex": editor.importIndex,
        }

    @classmethod
    def updateVer0_1_0(cls, model, data):
        data["preview"]["taskForever"] = model.editor.taskForever
        data["preview"]["taskPauseByError"] = model.editor.taskPauseByError
        data[cls.versionKey] = "0.1.1"
        return data

    @classmethod
    def updateVer0_1_1(cls, model, data):
        data["editor"] = data["preview"]
        del data["preview"]

        data["editor"]["importSpeed"] = model.editor.importSpeed
        data["editor"]["importStart"] = model.editor.importStart
        data["editor"]["importLength"] = model.editor.importLength
        data["editor"]["importIndex"] = model.editor.importIndex

        data[cls.versionKey] = "0.2.0"
        return data

    @classmethod
    def updateVer0_2_0(cls, model, data):
        gen = model.generate
        data["generate"]["upscale_tile_enable"] = gen.upscaleTileEnable
        data["generate"]["upscale_ip2p_enable"] = gen.upscaleIp2pEnable
        data["generate"]["upscale_ip2p_scale"] = gen.upscaleIp2pScale
        data["generate"]["upscale_ip2p_start"] = gen.upscaleIp2pStart
        data["generate"]["upscale_ip2p_end"] = gen.upscaleIp2pEnd
        data["generate"]["upscale_line_anime_enable"] = gen.upscaleLineAnimeEnable
        data["generate"]["upscale_line_anime_scale"] = gen.upscaleLineAnimeScale
        data["generate"]["upscale_line_anime_start"] = gen.upscaleLineAnimeStart
        data["generate"]["upscale_line_anime_end"] = gen.upscaleLineAnimeEnd

        data[cls.versionKey] = "0.3.0"
        return data

    @classmethod
    def updateVer0_3_0(cls, model, data):
        gen = model.generate

        data["generate"]["mosaic_enabled"] = gen.mosaicEnabled
        data["generate"]["mosaic_threshold"] = gen.mosaicThreshold
        data["generate"]["temporal_mosaic"] = gen.temporalMosaic
        data["generate"]["ellipse_mosaic"] = gen.ellipseMosaic
        data["generate"]["mosaic_mask_blur"] = gen.mosaicMaskBlur
        data["generate"]["mosaic_fem_face"] = gen.mosaicFemFace
        data["generate"]["mosaic_fem_brst"] = gen.mosaicFemBrst
        data["generate"]["mosaic_fem_brst_cov"] = gen.mosaicFemBrstCov
        data["generate"]["mosaic_fem_gntl"] = gen.mosaicFemGntl
        data["generate"]["mosaic_fem_gntl_cov"] = gen.mosaicFemGntlCov
        data["generate"]["mosaic_male_face"] = gen.mosaicMaleFace
        data["generate"]["mosaic_male_brst"] = gen.mosaicMaleBrst
        data["generate"]["mosaic_male_gntl"] = gen.mosaicMaleGntl
        data["generate"]["mosaic_armpit"] = gen.mosaicArmpit
        data["generate"]["mosaic_armpit_cov"] = gen.mosaicArmpitCov
        data["generate"]["mosaic_belly"] = gen.mosaicBelly
        data["generate"]["mosaic_belly_cov"] = gen.mosaicBellyCov
        data["generate"]["mosaic_hip"] = gen.mosaicHip
        data["generate"]["mosaic_hip_cov"] = gen.mosaicHipCov
        data["generate"]["mosaic_ans"] = gen.mosaicAns
        data["generate"]["mosaic_ans_cov"] = gen.mosaicAnsCov
        data["generate"]["mosaic_feet"] = gen.mosaicFeet
        data["generate"]["mosaic_feet_cov"] = gen.mosaicFeetCov
        data["generate"]["mosaic_scale_top"] = gen.mosaicScaleTop
        data["generate"]["mosaic_scale_bottom"] = gen.mosaicScaleBottom
        data["generate"]["mosaic_scale_left"] = gen.mosaicScaleLeft
        data["generate"]["mosaic_scale_right"] = gen.mosaicScaleRight
        data["generate"]["mosaic_ignore_top"] = gen.mosaicIgnoreTop
        data["generate"]["mosaic_ignore_bottom"] = gen.mosaicIgnoreBottom
        data["generate"]["mosaic_ignore_left"] = gen.mosaicIgnoreLeft
        data["generate"]["mosaic_ignore_right"] = gen.mosaicIgnoreRight

        data[cls.versionKey] = "0.4.0"
        return data

    @classmethod
    def updateVer0_4_0(cls, model, data):
        data["generate"]["use_lcm"] = False

        data[cls.versionKey] = "0.4.1"
        return data


Serializer.updator = {
    "0.1.0": Serializer.updateVer0_1_0,
    "0.1.1": Serializer.updateVer0_1_1,
    "0.2.0": Serializer.updateVer0_2_0,
    "0.3.0": Serializer.updateVer0_3_0,
    "0.4.0": Serializer.updateVer0_4_0,
}
