import os
import random


def __replace_all__(text, replacements):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def __format_name__(name):
    """Formats the name to be lowercase. Replace ' ' with '_' and ' with ."""
    return __replace_all__(
        str(
            name
        ).lower(),
        {
            " ": "_",
            "'": ""
        }
    )


def __format_map_name__(name):
    """Formats the map name and removes () and (payload)"""
    return __replace_all__(
        __format_name__(
            name
        ),
        {
            "_(payload)": "",
            "(": "",
            ")": ""
        }
    )


class MatchCustomisationImages:
    def __init__(self, base: str):
        self.background = f"{base}background.png"
        self.defeat = f"{base}defeat.png"
        self.dont_touch = f"{base}donttouch.png"
        self.info_text = f"{base}infotext.png"
        self.not_selected = f"{base}notselected.png"
        self.selected = f"{base}selected.png"
        self.snippet_1 = f"{base}snippet1.png"
        self.snippet_2 = f"{base}snippet2.png"
        self.victory = f"{base}victory.png"


class MatchImages:
    def __init__(self, base: str):
        self.base_image = f"{base}base_image.png"
        self.base_image_ranked = f"{base}base_image_ranked.png"
        self.base_image = f"{base}base_image_1.png"
        self.alt_image = f"{base}base_image_2.png"

        self.item_pane_0 = f"{base}item_pane_0.png"
        self.item_pane_1 = f"{base}item_pane_1.png"
        self.item_pane_2 = f"{base}item_pane_2.png"
        self.item_pane_3 = f"{base}item_pane_3.png"

        self.loadout_pane = f"{base}loadout_pane.png"
        self.player_sliver = f"{base}player_sliver.png"
        self.squire_sliver = f"{base}squire_sliver.png"

        self.stat_text_casual = f"{base}stat_text_casual.png"
        self.stat_text = f"{base}stat_text.png"


class ChampionIcon:
    def __init__(self, base: str, champion: str):
        if "omen" in champion and random.randint(0, 5) == 1:
            self.no_bg = f"{base}no_background/{champion}_goofy.png"
            self.bg = f"{base}background/{champion}_goofy.png"
            self.url = f"https://raw.githubusercontent.com/FuriaPaladins/Itto-Bot-Data/main/paladins_images/champion_icons/{champion.replace(' ', '%20')}_goofy.png"
        else:
            self.no_bg = f"{base}no_background/{champion}.png"
            self.bg = f"{base}background/{champion}.png"
            self.url = f"https://raw.githubusercontent.com/FuriaPaladins/Itto-Bot-Data/main/paladins_images/champion_icons/{champion.replace(' ', '%20')}.png"


class Talent:
    def __init__(self, if_exists, base, champion, talent):
        self.full = if_exists(f"{base}full/{champion}/{talent}.png")
        self.flat = if_exists(f"{base}flat/{champion}/{talent}.png")


class Passive:
    def __init__(self, if_exists, base, passive):
        self.full = if_exists(f"{base}full/{passive}.png")
        self.flat = if_exists(f"{base}flat/{passive}.png")


class PaladinsImages:
    """
    A class that fetches images from the assets folder.\n
    """

    empty_image = "assets/general/blank.png"
    base = "assets/paladins/"

    @classmethod
    def match_image_customisation(cls):
        return MatchCustomisationImages(f"{cls.base}.match_images/base_customisation_images/layer_")

    @classmethod
    def match_image_base(cls):
        return MatchImages(f"{cls.base}.match_images/")

    @classmethod
    def card(cls, champion, card=None):
        """Returns all the cards for a champion. If a card is provided, it will return that card instead"""
        if card is None:
            return cls.__if_exists__(f"{cls.base}cards/{__format_name__(champion)}/")
        return cls.__if_exists__(f"{cls.base}cards/{__format_name__(champion)}/{__format_name__(card)}.png")

    @classmethod
    def background(cls, champion):
        """Returns the background for a champion"""
        return cls.__if_exists__(f"{cls.base}champion_backgrounds/{__format_name__(champion)}.png")

    @classmethod
    def champion(cls, champion):
        """Returns the champion icon for a champion"""
        return ChampionIcon(f"{cls.base}champion_icons/", __format_name__(champion))

    @classmethod
    def item(cls, item):
        """Returns the item icon for an item"""
        return cls.__if_exists__(f"{cls.base}items/{__format_name__(item)}.png")

    @classmethod
    def map(cls, map_name):
        """Returns the map icons"""
        return cls.__if_exists__(f"{cls.base}maps/{__format_map_name__(map_name)}.png")

    @classmethod
    def talent(cls, champion, talent):
        """Returns the talent icon for a talent"""
        return Talent(cls.__if_exists__, f"{cls.base}talents/", __format_name__(champion), __format_name__(talent))

    @classmethod
    def passive(cls, passive):
        """Returns the passive icon for a passive"""
        return Passive(cls.__if_exists__, f"{cls.base}passives/", __format_name__(passive))

    @classmethod
    def platform(cls, platform):
        """Returns the platform icon for a platform"""
        return cls.__if_exists__(f"{cls.base}platforms/{__format_name__(platform)}.png")

    @classmethod
    def rank(cls, rank, centered=True):
        """Returns the rank icon for a rank"""
        return cls.__if_exists__(f"{cls.base}ranks/{'centered' if centered else 'default'}/{__format_name__(rank)}.png")

    @classmethod
    def __if_exists__(cls, path: str) -> str:
        if os.path.exists(path):
            return path
        return cls.empty_image
