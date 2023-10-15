import json


class Serializer:
    varsion = "0.1.0"

    @classmethod
    def save(cls, model, savePath):
        data = cls.serialize(model)
        with open(savePath, "w") as f:
            json.dump(data, f, indent=4)
        return True

    @classmethod
    def serialize(cls, model):
        data = {"easy_prompt_anime_version": cls.varsion}
        return data

    @classmethod
    def deserialize(cls):
        pass
