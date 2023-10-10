import os, datetime


class Const:
    tile = "tile-upscale"
    refine = "refine"

    schedulerValues = [
        "k_dpmpp_2m_sde",
        "k_dpmpp_sde",
        "k_dpmpp_2m",
        "ddim",
        "euler",
        "euler_a",
    ]
    schedulerNames = [
        "DPM++ 2M SDE Karras",
        "DPM++ SDE Karras",
        "DPM++ 2M Karras",
        "DDIM",
        "Euler",
        "Euler a",
    ]

    @classmethod
    def getSchedulerValue(cls, name):
        return cls.schedulerValues[cls.schedulerNames.index(name)]

    @classmethod
    def getSchedulerName(cls, value):
        return cls.schedulerNames[cls.schedulerValues.index(value)]


class Path:
    cwd = os.getcwd()
    ini = "EasyPromptAnimeEditor.ini"
    output = "output"

    promptTravel = "animatediff-cli-prompt-travel"
    data = os.path.join(promptTravel, "data")
    model = os.path.join(data, "models", "sd")
    motionModule = os.path.join(data, "models", "motion-module")
    vae = os.path.join(data, "vae")
    lora = os.path.join(data, "lora")
    embeddings = os.path.join(data, "embeddings")
    wildcard = os.path.join(promptTravel, "wildcards")
    promptTravelOutput = os.path.join(promptTravel, "output")
    promptTravelUpscaled = os.path.join(promptTravel, "upscaled")
    promptTravelRefined = os.path.join(promptTravel, "refine")
    ipAdapter = os.path.join(data, "ip_adapter_image")

    editor = "editor"
    tmp = os.path.join(editor, "tmp")
    log = os.path.join(editor, "log")
    defaultPrompt = os.path.join(editor, "DefaultPrompt-0_1_0.txt")
    promptTravelTemplate = os.path.join(editor, "PromptTravelTemplate-0_2_0.txt")
    downloadMenu = os.path.join(editor, "DownloadMenu.json")

    @classmethod
    def getYYYYMMDDHHMMSS(cls):
        return datetime.datetime.now().strftime("%Y_%m%d_%H%M_%S")

    @classmethod
    def getYYYYMMDD(cls):
        return datetime.datetime.now().strftime("%Y_%m%d")
