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
        "Alistar",
        "Annie",
        "Ashe",
        "Fiddlesticks",
        "Jax",
        "Kayle",
        "Maître Yi",
        "Morgana",
        "Nunu et Willump",
        "Ryze",
        "Sion",
        "Sivir",
        "Soraka",
        "Teemo",
        "Tristana",
        "Twisted Fate",
        "Warwick",
        "Singed",
        "Zilean",
        "Evelynn",
        "Tryndamere",
        "Twitch",
        "Karthus",
        "Amumu",
        "Cho'Gath",
        "Anivia",
        "Rammus",
        "Veigar",
        "Kassadin",
        "Gangplank",
        "Taric",
        "Blitzcrank",
        "Dr. Mundo",
        "Janna",
        "Malphite",
        "Corki",
        "Katarina",
        "Nasus",
        "Heimerdinger",
        "Shaco",
        "Udyr",
        "Nidalee",
        "Poppy",
        "Pantheon",
        "Gragas",
        "Mordekaiser",
        "Ezreal",
        "Shen",
        "Kennen",
        "Garen",
        "Akali",
        "Malzahar",
        "Olaf",
        "Kog'Maw",
        "Xin Zhao",
        "Vladimir",
        "Galio",
        "Urgot",
        "Miss Fortune",
        "Sona",
        "Swain",
        "Lux",
        "LeBlanc",
        "Irelia",
        "Trundle",
        "Cassiopeia",
        "Caitlyn",
        "Renekton",
        "Karma",
        "Maokai",
        "Jarvan IV",
        "Nocturne",
        "Lee Sin",
        "Brand",
        "Rumble",
        "Vayne",
        "Orianna",
        "Yorick",
        "Leona",
        "Wukong",
        "Skarner",
        "Talon",
        "Riven",
        "Xerath",
        "Graves",
        "Shyvana",
        "Fizz",
        "Volibear",
        "Ahri",
        "Viktor",
        "Sejuani",
        "Ziggs",
        "Nautilus",
        "Fiora",
        "Lulu",
        "Hecarim",
        "Varus",
        "Darius",
        "Draven",
        "Jayce",
        "Zyra",
        "Diana",
        "Rengar",
        "Syndra",
        "Kha'Zix",
        "Elise",
        "Zed",
        "Nami",
        "Vi",
        "Thresh",
        "Quinn",
        "Zac",
        "Lissandra",
        "Aatrox",
        "Lucian",
        "Jinx",
        "Yasuo",
        "Vel'Koz",
        "Braum",
        "Gnar",
        "Azir",
        "Kalista",
        "Rek'Sai",
        "Bard",
        "Ekko",
        "Tahm Kench",
        "Kindred",
        "Illaoi",
        "Jhin",
        "Aurelion Sol",
        "Taliyah",
        "Kled",
        "Ivern",
        "Camille",
        "Rakan",
        "Xayah",
        "Kayn",
        "Ornn",
        "Zoe",
        "Kai'Sa",
        "Pyke",
        "Neeko",
        "Sylas",
        "Yuumi",
        "Qiyana",
        "Senna",
        "Aphelios",
        "Sett",
        "Lillia",
        "Yone",
        "Samira",
        "Seraphine",
        "Rell",
        "Viego",
        "Gwen",
        "Akshan",
        "Vex",
        "Zeri",
        "Renata Glasc",
        "Bel'Veth",
        "Nilah",
        "K'Sante",
        "Milio",
        "Naafiri",
        "Briar",
        "Hwei",
        "Smolder",
        "Aurora",
        "Ambessa",
        "Mel",
        "Yunara",
        "Zaahen",
        "Locke",
    }
    default = valid_keys