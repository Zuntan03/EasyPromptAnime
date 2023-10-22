from configparser import ConfigParser


class Config:
    @classmethod
    def get(cls, cateroty, key, fallback):
        return cls._config.get(cateroty, key, fallback=str(fallback))

    @classmethod
    def getBool(cls, cateroty, key, fallback):
        return cls._config.getboolean(cateroty, key, fallback=fallback)

    @classmethod
    def getInt(cls, cateroty, key, fallback):
        return cls._config.getint(cateroty, key, fallback=fallback)

    @classmethod
    def getFloat(cls, cateroty, key, fallback):
        return cls._config.getfloat(cateroty, key, fallback=fallback)

    @classmethod
    def set(cls, cateroty, key, value):
        cls._config[cateroty][key] = str(value)

    @classmethod
    def load(cls, path, sections):
        cls._config = ConfigParser(interpolation=None)
        [cls._config.add_section(section) for section in sections]
        cls._config.read(path, encoding="utf-8-sig")

    @classmethod
    def save(cls, path):
        with open(path, "w", encoding="utf-8-sig") as cfgfile:
            cls._config.write(cfgfile)
