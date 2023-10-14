from config import Config
from l10n_en import l10nEn
from l10n_ja import l10nJa
import locale


class L10n:
    @classmethod
    def get(cls, key):
        return cls._l10n[key]

    @classmethod
    def format(cls, key, *args):
        return cls._l10n[key].format(*args)

    @classmethod
    def loadConfig(cls):
        lang = Config.get("ui", "lang", fallback=locale.getdefaultlocale()[0][:2])
        cls._l10n = l10nEn
        if lang == "ja":
            cls._l10n = l10nJa

    @classmethod
    def storeConfig(cls):
        Config.set("ui", "lang", cls.get("lang"))
