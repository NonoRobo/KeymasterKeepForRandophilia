from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionList, Toggle
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class LeagueOfLegendsArchipelagoOptions:
    lol_unlocked_champions: LoLUnlockedChampions

class LeagueOfLegendsGame(Game):
    name = "League of Legends"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = LeagueOfLegendsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []

        constraints.extend([
            GameObjectiveTemplate(
                label="Play as ROLE role.",
                data={
                    "ROLE": (lambda: self.lol_roles(), 1)
                },
            ),
        ])

        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Play a game with CHAMPION.",
                data={
                    "CHAMPION": (lambda: self.lol_unlocked_champions, 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ])
        wunit = sum(o.weight for o in game_objective_templates)

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Play a game.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3*wunit,
            ),
            GameObjectiveTemplate(
                label="Perform a Double Kill.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=wunit,
            ),
            GameObjectiveTemplate(
                label="Destroy a tower.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=wunit,
            ),
            GameObjectiveTemplate(
                label="Steal an objective.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=wunit,
            ),
        ])

        return game_objective_templates
    
    
    @property
    def lol_unlocked_champions(self) -> List[str]:
        return self.archipelago_options.lol_unlocked_champions.value
    
    
    @staticmethod
    def lol_roles() -> List[str]:
        return ["Top","Jungle","Mid","ADC","Support","Random"]


class LoLUnlockedChampions(OptionList):
    display_name = "[LoL] Unlocked champions"
    valid_keys = {
        "Aatrox",
        "Ahri",
        "Akali",
        "Akshan",
        "Alistar",
        "Amumu",
        "Anivia",
        "Annie",
        "Aphelios",
        "Ashe",
        "Aurelion Sol",
        "Aurora",
        "Azir",
        "Bard",
        "Bel'Veth",
        "Blitzcrank",
        "Brand",
        "Braum",
        "Briar",
        "Caitlyn",
        "Camille",
        "Cassiopeia",
        "Cho'Gath",
        "Corki",
        "Darius",
        "Diana",
        "Dr. Mundo",
        "Draven",
        "Ekko",
        "Elise",
        "Evelynn",
        "Ezreal",
        "Fiddlesticks",
        "Fiora",
        "Fizz",
        "Galio",
        "Gangplank",
        "Garen",
        "Gnar",
        "Gragas",
        "Graves",
        "Gwen",
        "Hecarim",
        "Heimerdinger",
        "Hwei",
        "Illaoi",
        "Irelia",
        "Ivern",
        "Janna",
        "Jarvan IV",
        "Jax",
        "Jayce",
        "Jhin",
        "Jinx",
        "K'Sante",
        "Kai'Sa",
        "Kalista",
        "Karma",
        "Karthus",
        "Kassadin",
        "Katarina",
        "Kayle",
        "Kayn",
        "Kennen",
        "Kha'Zix",
        "Kindred",
        "Kled",
        "Kog'Maw",
        "LeBlanc",
        "Lee Sin",
        "Leona",
        "Lillia",
        "Lissandra",
        "Lucian",
        "Lulu",
        "Lux",
        "Malphite",
        "Malzahar",
        "Maokai",
        "Master Yi",
        "Milio",
        "Miss Fortune",
        "Mordekaiser",
        "Morgana",
        "Naafiri",
        "Nami",
        "Nasus",
        "Nautilus",
        "Neeko",
        "Nidalee",
        "Nilah",
        "Nocturne",
        "Nunu",
        "Olaf",
        "Orianna",
        "Ornn",
        "Pantheon",
        "Poppy",
        "Pyke",
        "Qiyana",
        "Quinn",
        "Rakan",
        "Rammus",
        "Rek'Sai",
        "Rell",
        "Renata Glasc",
        "Renekton",
        "Rengar",
        "Riven",
        "Rumble",
        "Ryze",
        "Samira",
        "Sejuani",
        "Senna",
        "Seraphine",
        "Sett",
        "Shaco",
        "Shen",
        "Shyvana",
        "Singed",
        "Sion",
        "Sivir",
        "Skarner",
        "Smolder",
        "Sona",
        "Soraka",
        "Swain",
        "Sylas",
        "Syndra",
        "Tahm Kench",
        "Taliyah",
        "Talon",
        "Taric",
        "Teemo",
        "Thresh",
        "Tristana",
        "Trundle",
        "Tryndamere",
        "Twisted Fate",
        "Twitch",
        "Udyr",
        "Urgot",
        "Varus",
        "Vayne",
        "Veigar",
        "Vel'Koz",
        "Vex",
        "Vi",
        "Viego",
        "Viktor",
        "Vladimir",
        "Volibear",
        "Warwick",
        "Wukong",
        "Xayah",
        "Xerath",
        "Xin Zhao",
        "Yasuo",
        "Yone",
        "Yorick",
        "Yuumi",
        "Zac",
        "Zed",
        "Zeri",
        "Ziggs",
        "Zilean",
        "Zoe",
        "Zyra",
    }
    default = valid_keys