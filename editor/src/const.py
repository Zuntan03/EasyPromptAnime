import os, datetime
from enum import Enum


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
        "lcm",
        # "dpm_2_a",
        # "k_dpm_2_a",
    ]
    schedulerNames = [
        "DPM++ 2M SDE Karras",
        "DPM++ SDE Karras",
        "DPM++ 2M Karras",
        "DDIM",
        "Euler",
        "Euler a",
        "LCM",
        # "DPM2 a",
        # "DPM2 a Karras",
    ]

    @classmethod
    def getSchedulerValue(cls, name):
        return cls.schedulerValues[cls.schedulerNames.index(name)]

    @classmethod
    def getSchedulerName(cls, value):
        return cls.schedulerNames[cls.schedulerValues.index(value)]


class ControlNetType(Enum):
    canny = 0
    depth = 1
    inpaint = 2
    ip2p = 3
    lineart = 4
    lineart_anime = 5
    mlsd = 6
    normalbae = 7
    openpose = 8
    scribble = 9
    seg = 10
    shuffle = 11
    softedge = 12
    tile = 13


class Path:
    cwd = os.getcwd()
    ini = "EasyPromptAnimeEditor.ini"
    output = "output"
    save = "save"

    promptTravel = "animatediff-cli-prompt-travel"
    data = os.path.join(promptTravel, "data")
    model = os.path.join(data, "models", "sd")
    motionModule = os.path.join(data, "models", "motion-module")
    motionLora = os.path.join(data, "models", "motion_lora")
    vae = os.path.join(data, "vae")
    lora = os.path.join(data, "lora")
    embeddings = os.path.join(data, "embeddings")
    wildcard = os.path.join(promptTravel, "wildcards")
    promptTravelOutput = os.path.join(promptTravel, "output")
    promptTravelUpscaled = os.path.join(promptTravel, "upscaled")
    promptTravelRefined = os.path.join(promptTravel, "refine")
    controlNet = os.path.join(data, "controlnet_image")
    ipAdapter = os.path.join(data, "ip_adapter_image")

    editor = "editor"
    temp = os.path.join(editor, "temp")
    log = os.path.join(editor, "log")
    defaultPrompt = os.path.join(editor, "DefaultPrompt-0_1_0.txt")
    promptTravelTemplate = os.path.join(editor, "PromptTravelTemplate-0_6_0.txt")
    downloadMenu = os.path.join(editor, "DownloadMenu.json")

    @classmethod
    def getYYYYMMDDHHMMSS(cls):
        return datetime.datetime.now().strftime("%Y_%m%d_%H%M_%S")

    @classmethod
    def getYYYYMMDD(cls):
        return datetime.datetime.now().strftime("%Y_%m%d")

    @classmethod
    def getControlNet(cls, dirName, type):
        return os.path.join(cls.controlNet, dirName, f"controlnet_{type.name}")
