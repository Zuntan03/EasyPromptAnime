from const import Const, ControlNetType
from config import Config
from mdl_notifier import Notifier


class Generate(Notifier):
    defLength = 30
    defModel = "real_model_N.safetensors"
    defVae = "kl-f8-anime2.ckpt"
    defMotionModule = "mm_sd_v15_v2.ckpt"
    defContext = 16
    defScheduler = "DPM++ SDE Karras"
    defSteps = 20
    defGuidanceScale = 8.0
    defClipSkip = 2
    defPromptFixedRatio = 0.7
    defUseHalfVae = False
    defUseXFormers = False
    defWidth = 384  # TODO: Out of Sdene
    defHeight = 512  # TODO: Out of Sdene
    defSeed = -1

    defControlNetDir = "test"
    defControlNetLoop = True

    defCnEnable = False
    defCnUsePreprocessor = True
    defCnGuessMode = False
    defCnScale = 1.0
    defCnScaleList = ""
    defCnStart = 0.0
    defCnEnd = 1.0

    defUseIpAdapter = False
    defUseIpAdapterPlus = True
    defUseIpAdapterPlusFace = True
    defIpAdapterScale = 0.5
    defIpAdapterImageDir = "test"

    defUpscale1Enabled = True  # TODO: Out of Sdene
    defUpscale1Mode = Const.tile
    defUpscale1Scale = 2.0  # TODO: Out of Sdene

    defUpscale2Enabled = False  # TODO: Out of Sdene
    defUpscale2Mode = Const.tile
    defUpscale2Scale = 1.5  # TODO: Out of Sdene

    defUpscaleScheduler = "DPM++ SDE Karras"
    defUpscaleSteps = 15
    defUpscaleGuidanceScale = 8.0
    defUpscaleStrength = 0.6
    defUpscaleTileEnable = True
    defUpscaleTileScale = 1.0
    defUpscaleTileStart = 0.0
    defUpscaleTileEnd = 1.0
    defUpscaleIp2pEnable = False
    defUpscaleIp2pScale = 1.0
    defUpscaleIp2pStart = 0.0
    defUpscaleIp2pEnd = 1.0
    defUpscaleLineAnimeEnable = False
    defUpscaleLineAnimeScale = 1.0
    defUpscaleLineAnimeStart = 0.0
    defUpscaleLineAnimeEnd = 1.0
    defUpscaleUseHalfVae = False
    defUpscaleUseXFormers = False

    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.length = Generate.defLength
        self.model = Generate.defModel
        self.vae = Generate.defVae
        self.motionModule = Generate.defMotionModule
        self.context = Generate.defContext
        self.scheduler = Generate.defScheduler
        self.steps = Generate.defSteps
        self.guidanceScale = Generate.defGuidanceScale
        self.clipSkip = Generate.defClipSkip
        self.promptFixedRatio = Generate.defPromptFixedRatio
        self.useHalfVae = Generate.defUseHalfVae
        self.useXFormers = Generate.defUseXFormers
        self.width = Generate.defWidth
        self.height = Generate.defHeight
        self.seed = Generate.defSeed

        self.controlNetDir = Generate.defControlNetDir
        self.controlNetLoop = Generate.defControlNetLoop

        for cnType in ControlNetType:
            setattr(
                self,
                f"cnEnable_{cnType.name}",
                getattr(Generate, f"defCnEnable_{cnType.name}"),
            )
            setattr(
                self,
                f"cnUsePreprocessor_{cnType.name}",
                getattr(Generate, f"defCnUsePreprocessor_{cnType.name}"),
            )
            setattr(
                self,
                f"cnGuessMode_{cnType.name}",
                getattr(Generate, f"defCnGuessMode_{cnType.name}"),
            )
            setattr(
                self,
                f"cnScale_{cnType.name}",
                getattr(Generate, f"defCnScale_{cnType.name}"),
            )
            setattr(
                self,
                f"cnScaleList_{cnType.name}",
                getattr(Generate, f"defCnScaleList_{cnType.name}"),
            )
            setattr(
                self,
                f"cnStart_{cnType.name}",
                getattr(Generate, f"defCnStart_{cnType.name}"),
            )
            setattr(
                self,
                f"cnEnd_{cnType.name}",
                getattr(Generate, f"defCnEnd_{cnType.name}"),
            )

        self.useIpAdapter = Generate.defUseIpAdapter
        self.useIpAdapterPlus = Generate.defUseIpAdapterPlus
        self.useIpAdapterPlusFace = Generate.defUseIpAdapterPlusFace
        self.ipAdapterScale = Generate.defIpAdapterScale
        self.ipAdapterImageDir = Generate.defIpAdapterImageDir

        self.upscale1Enabled = Generate.defUpscale1Enabled
        self.upscale1Mode = Generate.defUpscale1Mode
        self.upscale1Scale = Generate.defUpscale1Scale

        self.upscale2Enabled = Generate.defUpscale2Enabled
        self.upscale2Mode = Generate.defUpscale2Mode
        self.upscale2Scale = Generate.defUpscale2Scale

        self.upscaleScheduler = Generate.defUpscaleScheduler
        self.upscaleSteps = Generate.defUpscaleSteps
        self.upscaleGuidanceScale = Generate.defUpscaleGuidanceScale
        self.upscaleStrength = Generate.defUpscaleStrength
        self.upscaleTileEnable = Generate.defUpscaleTileEnable
        self.upscaleTileScale = Generate.defUpscaleTileScale
        self.upscaleTileStart = Generate.defUpscaleTileStart
        self.upscaleTileEnd = Generate.defUpscaleTileEnd
        self.upscaleIp2pEnable = Generate.defUpscaleIp2pEnable
        self.upscaleIp2pScale = Generate.defUpscaleIp2pScale
        self.upscaleIp2pStart = Generate.defUpscaleIp2pStart
        self.upscaleIp2pEnd = Generate.defUpscaleIp2pEnd
        self.upscaleLineAnimeEnable = Generate.defUpscaleLineAnimeEnable
        self.upscaleLineAnimeScale = Generate.defUpscaleLineAnimeScale
        self.upscaleLineAnimeStart = Generate.defUpscaleLineAnimeStart
        self.upscaleLineAnimeEnd = Generate.defUpscaleLineAnimeEnd
        self.upscaleUseHalfVae = Generate.defUpscaleUseHalfVae
        self.upscaleUseXFormers = Generate.defUpscaleUseXFormers

        self.isChanged = True

    def set(self, memberName, value):
        result = super().set(memberName, value)
        if result:
            self.isChanged = True
        return result

    def getUpscale1Height(self):
        return int(self.height * self.upscale1Scale)

    def getUpscale1Width(self):
        return int(self.width * self.upscale1Scale)

    def getUpscale2Height(self):
        return int(self.getUpscale1Height() * self.upscale2Scale)

    def getUpscale2Width(self):
        return int(self.getUpscale1Width() * self.upscale2Scale)

    @classmethod
    def loadConfig(cls):
        Generate.defLength = Config.getInt("default", "length", Generate.defLength)
        Generate.defModel = Config.get("default", "model", Generate.defModel)
        Generate.defVae = Config.get("default", "vae", Generate.defVae)
        Generate.defMotionModule = Config.get(
            "default", "motion_module", Generate.defMotionModule
        )
        Generate.defContext = Config.getInt("default", "context", Generate.defContext)
        Generate.defScheduler = Config.get(
            "default", "scheduler", Generate.defScheduler
        )
        Generate.defSteps = Config.getInt("default", "steps", Generate.defSteps)
        Generate.defGuidanceScale = Config.getFloat(
            "default", "guidance_scale", Generate.defGuidanceScale
        )
        Generate.defClipSkip = Config.getInt(
            "default", "clip_skip", Generate.defClipSkip
        )
        Generate.defPromptFixedRatio = Config.getFloat(
            "default", "prompt_fixed_ratio", Generate.defPromptFixedRatio
        )
        Generate.defUseHalfVae = Config.getBool(
            "default", "use_half_vae", Generate.defUseHalfVae
        )
        Generate.defUseXFormers = Config.getBool(
            "default", "use_x_formers", Generate.defUseXFormers
        )
        Generate.defWidth = Config.getInt("default", "width", Generate.defWidth)
        Generate.defHeight = Config.getInt("default", "height", Generate.defHeight)
        Generate.defSeed = Config.getInt("default", "seed", Generate.defSeed)

        Generate.defControlNetDir = Config.get(
            "default", "control_net_dir", Generate.defControlNetDir
        )
        Generate.defControlNetLoop = Config.getBool(
            "default", "control_net_loop", Generate.defControlNetLoop
        )

        for cnType in ControlNetType:
            setattr(
                Generate,
                f"defCnEnable_{cnType.name}",
                Config.getBool(
                    "default_controlnet",
                    f"{cnType.name}_enable",
                    getattr(Generate, f"defCnEnable_{cnType.name}"),
                ),
            )
            setattr(
                Generate,
                f"defCnUsePreprocessor_{cnType.name}",
                Config.getBool(
                    "default_controlnet",
                    f"{cnType.name}_use_preprocessor",
                    getattr(Generate, f"defCnUsePreprocessor_{cnType.name}"),
                ),
            )
            setattr(
                Generate,
                f"defCnGuessMode_{cnType.name}",
                Config.getBool(
                    "default_controlnet",
                    f"{cnType.name}_guess_mode",
                    getattr(Generate, f"defCnGuessMode_{cnType.name}"),
                ),
            )
            setattr(
                Generate,
                f"defCnScale_{cnType.name}",
                Config.getFloat(
                    "default_controlnet",
                    f"{cnType.name}_scale",
                    getattr(Generate, f"defCnScale_{cnType.name}"),
                ),
            )
            setattr(
                Generate,
                f"defCnScaleList_{cnType.name}",
                Config.get(
                    "default_controlnet",
                    f"{cnType.name}_scale_list",
                    getattr(Generate, f"defCnScaleList_{cnType.name}"),
                ),
            )
            setattr(
                Generate,
                f"defCnStart_{cnType.name}",
                Config.getFloat(
                    "default_controlnet",
                    f"{cnType.name}_start",
                    getattr(Generate, f"defCnStart_{cnType.name}"),
                ),
            )
            setattr(
                Generate,
                f"defCnEnd_{cnType.name}",
                Config.getFloat(
                    "default_controlnet",
                    f"{cnType.name}_end",
                    getattr(Generate, f"defCnEnd_{cnType.name}"),
                ),
            )

        Generate.defUseIpAdapter = Config.getBool(
            "default", "use_ip_adapter", Generate.defUseIpAdapter
        )
        Generate.defUseIpAdapterPlus = Config.getBool(
            "default", "use_ip_adapter_plus", Generate.defUseIpAdapterPlus
        )
        Generate.defUseIpAdapterPlusFace = Config.getBool(
            "default", "use_ip_adapter_plus_face", Generate.defUseIpAdapterPlusFace
        )
        Generate.defIpAdapterScale = Config.getFloat(
            "default", "ip_adapter_scale", Generate.defIpAdapterScale
        )
        Generate.defIpAdapterImageDir = Config.get(
            "default", "ip_adapter_image_dir", Generate.defIpAdapterImageDir
        )

        Generate.defUpscale1Enabled = Config.getBool(
            "default", "upscale1_enabled", Generate.defUpscale1Enabled
        )
        Generate.defUpscale1Mode = Config.get(
            "default", "upscale1_mode", Generate.defUpscale1Mode
        )
        Generate.defUpscale1Scale = Config.getFloat(
            "default", "upscale1_scale", Generate.defUpscale1Scale
        )

        Generate.defUpscale2Enabled = Config.getBool(
            "default", "upscale2_enabled", Generate.defUpscale2Enabled
        )
        Generate.defUpscale2Mode = Config.get(
            "default", "upscale2_mode", Generate.defUpscale2Mode
        )
        Generate.defUpscale2Scale = Config.getFloat(
            "default", "upscale2_scale", Generate.defUpscale2Scale
        )

        Generate.defUpscaleScheduler = Config.get(
            "default", "upscale_scheduler", Generate.defUpscaleScheduler
        )
        Generate.defUpscaleSteps = Config.getInt(
            "default", "upscale_steps", Generate.defUpscaleSteps
        )
        Generate.defUpscaleGuidanceScale = Config.getFloat(
            "default", "upscale_guidance_scale", Generate.defUpscaleGuidanceScale
        )
        Generate.defUpscaleStrength = Config.getFloat(
            "default", "upscale_strength", Generate.defUpscaleStrength
        )
        Generate.defUpscaleTileEnable = Config.getBool(
            "default", "upscale_tile_enable", Generate.defUpscaleTileEnable
        )
        Generate.defUpscaleTileScale = Config.getFloat(
            "default", "upscale_tile_scale", Generate.defUpscaleTileScale
        )
        Generate.defUpscaleTileStart = Config.getFloat(
            "default", "upscale_tile_start", Generate.defUpscaleTileStart
        )
        Generate.defUpscaleTileEnd = Config.getFloat(
            "default", "upscale_tile_end", Generate.defUpscaleTileEnd
        )
        Generate.defUpscaleIp2pEnable = Config.getBool(
            "default", "upscale_ip2p_enable", Generate.defUpscaleIp2pEnable
        )
        Generate.defUpscaleIp2pScale = Config.getFloat(
            "default", "upscale_ip2p_scale", Generate.defUpscaleIp2pScale
        )
        Generate.defUpscaleIp2pStart = Config.getFloat(
            "default", "upscale_ip2p_start", Generate.defUpscaleIp2pStart
        )
        Generate.defUpscaleIp2pEnd = Config.getFloat(
            "default", "upscale_ip2p_end", Generate.defUpscaleIp2pEnd
        )
        Generate.defUpscaleLineAnimeEnable = Config.getBool(
            "default", "upscale_line_anime_enable", Generate.defUpscaleLineAnimeEnable
        )
        Generate.defUpscaleLineAnimeScale = Config.getFloat(
            "default", "upscale_line_anime_scale", Generate.defUpscaleLineAnimeScale
        )
        Generate.defUpscaleLineAnimeStart = Config.getFloat(
            "default", "upscale_line_anime_start", Generate.defUpscaleLineAnimeStart
        )
        Generate.defUpscaleLineAnimeEnd = Config.getFloat(
            "default", "upscale_line_anime_end", Generate.defUpscaleLineAnimeEnd
        )
        Generate.defUpscaleUseHalfVae = Config.getBool(
            "default", "upscale_use_half_vae", Generate.defUpscaleUseHalfVae
        )
        Generate.defUpscaleUseXFormers = Config.getBool(
            "default", "upscale_use_x_formers", Generate.defUpscaleUseXFormers
        )

    def updateConfig(self):
        Generate.defLength = self.length
        Generate.defModel = self.model
        Generate.defVae = self.vae
        Generate.defMotionModule = self.motionModule
        Generate.defContext = self.context
        Generate.defScheduler = self.scheduler
        Generate.defSteps = self.steps
        Generate.defGuidanceScale = self.guidanceScale
        Generate.defClipSkip = self.clipSkip
        Generate.defPromptFixedRatio = self.promptFixedRatio
        Generate.defUseHalfVae = self.useHalfVae
        Generate.defUseXFormers = self.useXFormers
        Generate.defWidth = self.width
        Generate.defHeight = self.height
        Generate.defSeed = self.seed

        Generate.defControlNetDir = self.controlNetDir
        Generate.defControlNetLoop = self.controlNetLoop

        for cnType in ControlNetType:
            setattr(
                Generate,
                f"defCnEnable_{cnType.name}",
                getattr(self, f"cnEnable_{cnType.name}"),
            )
            setattr(
                Generate,
                f"defCnUsePreprocessor_{cnType.name}",
                getattr(self, f"cnUsePreprocessor_{cnType.name}"),
            )
            setattr(
                Generate,
                f"defCnGuessMode_{cnType.name}",
                getattr(self, f"cnGuessMode_{cnType.name}"),
            )
            setattr(
                Generate,
                f"defCnScale_{cnType.name}",
                getattr(self, f"cnScale_{cnType.name}"),
            )
            setattr(
                Generate,
                f"defCnScaleList_{cnType.name}",
                getattr(self, f"cnScaleList_{cnType.name}"),
            )
            setattr(
                Generate,
                f"defCnStart_{cnType.name}",
                getattr(self, f"cnStart_{cnType.name}"),
            )
            setattr(
                Generate,
                f"defCnEnd_{cnType.name}",
                getattr(self, f"cnEnd_{cnType.name}"),
            )

        Generate.defUseIpAdapter = self.useIpAdapter
        Generate.defUseIpAdapterPlus = self.useIpAdapterPlus
        Generate.defUseIpAdapterPlusFace = self.useIpAdapterPlusFace
        Generate.defIpAdapterScale = self.ipAdapterScale
        Generate.defIpAdapterImageDir = self.ipAdapterImageDir

        Generate.defUpscale1Enabled = self.upscale1Enabled
        Generate.defUpscale1Mode = self.upscale1Mode
        Generate.defUpscale1Scale = self.upscale1Scale

        Generate.defUpscale2Enabled = self.upscale2Enabled
        Generate.defUpscale2Mode = self.upscale2Mode
        Generate.defUpscale2Scale = self.upscale2Scale

        Generate.defUpscaleScheduler = self.upscaleScheduler
        Generate.defUpscaleSteps = self.upscaleSteps
        Generate.defUpscaleGuidanceScale = self.upscaleGuidanceScale
        Generate.defUpscaleStrength = self.upscaleStrength
        Generate.defUpscaleTileEnable = self.upscaleTileEnable
        Generate.defUpscaleTileScale = self.upscaleTileScale
        Generate.defUpscaleTileStart = self.upscaleTileStart
        Generate.defUpscaleTileEnd = self.upscaleTileEnd
        Generate.defUpscaleIp2pEnable = self.upscaleIp2pEnable
        Generate.defUpscaleIp2pScale = self.upscaleIp2pScale
        Generate.defUpscaleIp2pStart = self.upscaleIp2pStart
        Generate.defUpscaleIp2pEnd = self.upscaleIp2pEnd
        Generate.defUpscaleLineAnimeEnable = self.upscaleLineAnimeEnable
        Generate.defUpscaleLineAnimeScale = self.upscaleLineAnimeScale
        Generate.defUpscaleLineAnimeStart = self.upscaleLineAnimeStart
        Generate.defUpscaleLineAnimeEnd = self.upscaleLineAnimeEnd
        Generate.defUpscaleUseHalfVae = self.upscaleUseHalfVae
        Generate.defUpscaleUseXFormers = self.upscaleUseXFormers

    def storeConfig(self):
        Config.set("default", "length", Generate.defLength)
        Config.set("default", "model", Generate.defModel)
        Config.set("default", "vae", Generate.defVae)
        Config.set("default", "motion_module", Generate.defMotionModule)
        Config.set("default", "context", Generate.defContext)
        Config.set("default", "scheduler", Generate.defScheduler)
        Config.set("default", "steps", Generate.defSteps)
        Config.set("default", "guidance_scale", Generate.defGuidanceScale)
        Config.set("default", "clip_skip", Generate.defClipSkip)
        Config.set("default", "prompt_fixed_ratio", Generate.defPromptFixedRatio)
        Config.set("default", "use_half_vae", Generate.defUseHalfVae)
        Config.set("default", "use_x_formers", Generate.defUseXFormers)
        Config.set("default", "width", Generate.defWidth)
        Config.set("default", "height", Generate.defHeight)
        Config.set("default", "seed", Generate.defSeed)

        Config.set("default", "control_net_dir", Generate.defControlNetDir)
        Config.set("default", "control_net_loop", Generate.defControlNetLoop)

        for cnType in ControlNetType:
            Config.set(
                "default_controlnet",
                f"{cnType.name}_enable",
                getattr(Generate, f"defCnEnable_{cnType.name}"),
            )
            Config.set(
                "default_controlnet",
                f"{cnType.name}_use_preprocessor",
                getattr(Generate, f"defCnUsePreprocessor_{cnType.name}"),
            )
            Config.set(
                "default_controlnet",
                f"{cnType.name}_guess_mode",
                getattr(Generate, f"defCnGuessMode_{cnType.name}"),
            )
            Config.set(
                "default_controlnet",
                f"{cnType.name}_scale",
                getattr(Generate, f"defCnScale_{cnType.name}"),
            )
            Config.set(
                "default_controlnet",
                f"{cnType.name}_scale_list",
                getattr(Generate, f"defCnScaleList_{cnType.name}"),
            )
            Config.set(
                "default_controlnet",
                f"{cnType.name}_start",
                getattr(Generate, f"defCnStart_{cnType.name}"),
            )
            Config.set(
                "default_controlnet",
                f"{cnType.name}_end",
                getattr(Generate, f"defCnEnd_{cnType.name}"),
            )

        Config.set("default", "use_ip_adapter", Generate.defUseIpAdapter)
        Config.set("default", "use_ip_adapter_plus", Generate.defUseIpAdapterPlus)
        Config.set(
            "default", "use_ip_adapter_plus_face", Generate.defUseIpAdapterPlusFace
        )
        Config.set("default", "ip_adapter_scale", Generate.defIpAdapterScale)
        Config.set("default", "ip_adapter_image_dir", Generate.defIpAdapterImageDir)

        Config.set("default", "upscale1_enabled", Generate.defUpscale1Enabled)
        Config.set("default", "upscale1_mode", Generate.defUpscale1Mode)
        Config.set("default", "upscale1_scale", Generate.defUpscale1Scale)

        Config.set("default", "upscale2_enabled", Generate.defUpscale2Enabled)
        Config.set("default", "upscale2_mode", Generate.defUpscale2Mode)
        Config.set("default", "upscale2_scale", Generate.defUpscale2Scale)

        Config.set("default", "upscale_scheduler", Generate.defUpscaleScheduler)
        Config.set("default", "upscale_steps", Generate.defUpscaleSteps)
        Config.set(
            "default", "upscale_guidance_scale", Generate.defUpscaleGuidanceScale
        )
        Config.set("default", "upscale_strength", Generate.defUpscaleStrength)
        Config.set("default", "upscale_tile_enable", Generate.defUpscaleTileEnable)
        Config.set("default", "upscale_tile_scale", Generate.defUpscaleTileScale)
        Config.set("default", "upscale_tile_start", Generate.defUpscaleTileStart)
        Config.set("default", "upscale_tile_end", Generate.defUpscaleTileEnd)
        Config.set("default", "upscale_ip2p_enable", Generate.defUpscaleIp2pEnable)
        Config.set("default", "upscale_ip2p_scale", Generate.defUpscaleIp2pScale)
        Config.set("default", "upscale_ip2p_start", Generate.defUpscaleIp2pStart)
        Config.set("default", "upscale_ip2p_end", Generate.defUpscaleIp2pEnd)
        Config.set(
            "default", "upscale_line_anime_enable", Generate.defUpscaleLineAnimeEnable
        )
        Config.set(
            "default", "upscale_line_anime_scale", Generate.defUpscaleLineAnimeScale
        )
        Config.set(
            "default", "upscale_line_anime_start", Generate.defUpscaleLineAnimeStart
        )
        Config.set("default", "upscale_line_anime_end", Generate.defUpscaleLineAnimeEnd)
        Config.set("default", "upscale_use_half_vae", Generate.defUpscaleUseHalfVae)
        Config.set("default", "upscale_use_x_formers", Generate.defUpscaleUseXFormers)


for cnType in ControlNetType:
    setattr(Generate, f"defCnEnable_{cnType.name}", Generate.defCnEnable)
    setattr(
        Generate, f"defCnUsePreprocessor_{cnType.name}", Generate.defCnUsePreprocessor
    )
    setattr(Generate, f"defCnGuessMode_{cnType.name}", Generate.defCnGuessMode)
    setattr(Generate, f"defCnScale_{cnType.name}", Generate.defCnScale)
    setattr(Generate, f"defCnScaleList_{cnType.name}", Generate.defCnScaleList)
    setattr(Generate, f"defCnStart_{cnType.name}", Generate.defCnStart)
    setattr(Generate, f"defCnEnd_{cnType.name}", Generate.defCnEnd)
