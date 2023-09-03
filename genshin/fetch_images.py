import os


class ArtifactSet:
    def __init__(self, img_list):
        self.atlas = img_list[0]
        self.crown = img_list[1]
        self.feather = img_list[2]
        self.flower = img_list[3]
        self.goblet = img_list[4]
        self.sands = img_list[5]


class Character:
    def __init__(self, img_list):
        self.constellation = img_list[0]
        self.constellation_icons = img_list[1]
        self.gacha_card = img_list[2]
        self.gacha_cropped = img_list[3]
        self.gacha_full = img_list[4]
        self.icon = img_list[5]
        self.icon_side = img_list[6]
        self.namecard_icon = img_list[7]
        self.namecard_picture = img_list[8]
        self.portrait = img_list[9]
        self.special_food = img_list[10]
        self.talent_icons = img_list[11]

        self.element_icon = img_list[12]


class Weapon:
    def __init__(self, img_list):
        self.icon = img_list[0]
        self.gacha_icon = img_list[1]
        self.awakened_icon = img_list[2]


def __format_name__(name):
    return str(name).lower().replace(' ', '_').replace("'", '').replace(',', '').replace('!', '')


class GenshinImages:
    """
    A class that fetches images from the assets folder.\n
    """
    empty_image = "assets/general/blank.png"
    base = "assets/genshin/"

    @classmethod
    def artifact(cls, name) -> ArtifactSet:
        """
        Returns an ArtifactSet object with all the images for the artifacts.\n
        If any of the images don't exist, it will be replaced with a blank image.\n
        Also formats the input. EG: "Archaic Petra" = "archaic_petra"
        """
        __artifact_base__ = f"{cls.base}artifacts/{__format_name__(name)}/"
        return ArtifactSet([
            cls.__if_exists__(f"{__artifact_base__}atlas.png"),
            cls.__if_exists__(f"{__artifact_base__}crown.png"),
            cls.__if_exists__(f"{__artifact_base__}feather.png"),
            cls.__if_exists__(f"{__artifact_base__}flower.png"),
            cls.__if_exists__(f"{__artifact_base__}goblet.png"),
            cls.__if_exists__(f"{__artifact_base__}sands.png")
        ])

    @classmethod
    def book(cls, name) -> str:
        """
        Returns the image for the book.\n
        If the image doesn't exist, it will be replaced with a blank image.\n
        Also formats the input. EG: "Freedom" = "freedom"
        """
        return cls.__if_exists__(f"{cls.base}books/{__format_name__(name)}.png")

    @classmethod
    def character(cls, name, element, is_traveler=False, traveler_icon_url=None) -> Character:
        """
        Returns the image for the character.\n
        If the image doesn't exist, it will be replaced with a blank image.\n
        Also formats the input. EG: "Amber" = "amber"
        """
        __character_base__ = f"{cls.base}characters/{__format_name__(element)}/{__format_name__(name)}/"
        if not is_traveler:
            return Character([
                cls.__if_exists__(f"{__character_base__}constellation.png"),
                [cls.__if_exists__(f"{__character_base__}constellation_{i}.png") for i in range(0, 5)],
                cls.__if_exists__(f"{__character_base__}gacha_art_card.png"),
                cls.__if_exists__(f"{__character_base__}gacha_art_cropped.png"),
                cls.__if_exists__(f"{__character_base__}gacha_art_full.png"),
                cls.__if_exists__(f"{__character_base__}icon.png"),
                cls.__if_exists__(f"{__character_base__}icon_side.png"),
                cls.__if_exists__(f"{__character_base__}namecard_icon.png"),
                cls.__if_exists__(f"{__character_base__}namecard_picture.png"),
                cls.__if_exists__(f"{__character_base__}portrait.png"),
                cls.__if_exists__(f"{__character_base__}special_food.png"),
                [cls.__if_exists__(f"{__character_base__}talent_{i}.png") for i in range(0, 6)],
                cls.__if_exists__(f"{cls.base}element_icons/{__format_name__(element)}.png")
            ])

    @classmethod
    def element(cls, name) -> str:
        """
        Returns the image for the element.\n
        """
        return cls.__if_exists__(f"{cls.base}element_icons/{__format_name__(name)}.png")

    @classmethod
    def food(cls, name) -> str:
        """
        Returns the image for the food.\n
        If the image doesn't exist, it will be replaced with a blank image.\n
        Also formats the input. EG: "Adeptus' Temptation" = "adeptus'_temptation"
        """
        return cls.__if_exists__(f"{cls.base}food/{__format_name__(name)}.png")

    @classmethod
    def furniture(cls, name, furniture_type) -> str:
        """
        Returns the image for the furniture.\n
        If the image doesn't exist, it will be replaced with a blank image.\n
        Also formats the input. EG: "Adeptus' Temptation" = "adeptus'_temptation"
        """
        return cls.__if_exists__(f"{cls.base}furniture/{__format_name__(furniture_type)}/{__format_name__(name)}.png")

    @classmethod
    def materials(cls, name, material_type) -> str:
        """
        Returns the image for the materials.\n
        If the image doesn't exist, it will be replaced with a blank image.\n
        Also formats the input. EG: "Adeptus' Temptation" = "adeptus'_temptation"
        """
        return cls.__if_exists__(f"{cls.base}materials/{__format_name__(material_type)}/{__format_name__(name)}.png")

    @classmethod
    def monster(cls, name, material_type):
        """
        Returns the image for the monster.\n
        If the image doesn't exist, it will be replaced with a blank image.\n
        """
        return cls.__if_exists__(f"{cls.base}monsters/{__format_name__(material_type)}/{__format_name__(name)}.png")

    @classmethod
    def weapon(cls, name, weapon_type) -> Weapon:
        """
        Returns the image for the weapon.\n
        If the image doesn't exist, it will be replaced with a blank image.\n
        Also formats the input. EG: "Adeptus' Temptation" = "adeptus'_temptation"
        """
        __weapon_base__ = f"{cls.base}weapons/{__format_name__(weapon_type)}/{__format_name__(name)}/"
        return Weapon([
            cls.__if_exists__(f"{__weapon_base__}icon.png"),
            cls.__if_exists__(f"{__weapon_base__}gacha_icon.png"),
            cls.__if_exists__(f"{__weapon_base__}awakened_icon.png")
        ])

    @classmethod
    def boss_card(cls, name, base_img=False):
        return cls.__if_exists__(f"{cls.base}.other/bosses/{'base/' if base_img else 'generated/'}{__format_name__(name)}.png")

    @classmethod
    def __if_exists__(cls, path: str) -> str:
        if os.path.exists(path):
            return path
        return cls.empty_image

    @staticmethod
    def convert_element(elem):
        return {
            "Wind": "anemo",
            "Fire": "pyro",
            "Water": "hydro",
            "Ice": "cryo",
            "Rock": "geo",
            "Electric": "electro",
            "Grass": "dendro"

        }.get(elem, None)
