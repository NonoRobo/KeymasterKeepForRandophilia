from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionList, Toggle
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate


@dataclass
class Hades2ArchipelagoOptions:
    pass

class Hades2Game(Game):
    name = "Hades 2"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = True
    options_cls = Hades2ArchipelagoOptions

    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Reach DESTINATION.",
                data={
                    "DESTINATION": (lambda: self.destination(), 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Kill one final boss with WEAPON.",
                data={
                    "WEAPON": (lambda: self.weapons(), 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Spend one night with WEAPON.",
                data={
                    "WEAPON": (lambda: self.aspect_weapons(), 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
             GameObjectiveTemplate(
                label="Play one chaos trial.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
             GameObjectiveTemplate(
                label="Do one Dream dive with Hypnos.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ])
       
        return game_objective_templates
    

    @staticmethod
    def destination() -> List[str]:
        return [
            "Mount Olympus", "House of Hades"
        ]

    @staticmethod
    def weapons() -> List[str]:
        return [
            "Argent Skull","Moonstone Axe","Sister Blades","Umbral flames","Witch's Staff","Black Coat"
        ]

    @staticmethod
    def aspect_weapons() -> List[str]:
        return [
            "Argent Skull, Aspect of Melinoë",
            "Argent Skull, Aspect of Medea",
            "Argent Skull, Aspect of Persephone",
            "Argent Skull, Aspect of Hel",
            "Moonstone Axe, Aspect of Melinoë",
            "Moonstone Axe, Aspect of Charon",
            "Moonstone Axe, Aspect of Thanatos",
            "Moonstone Axe, Aspect of Nergal",
            "Sister Blades, Aspect of Melinoë",
            "Sister Blades, Aspect of Artemis",
            "Sister Blades, Aspect of Pan",
            "Sister Blades, Aspect of Morrigan",
            "Umbral flames, Aspect of Melinoë",
            "Umbral flames, Aspect of Moros",
            "Umbral flames, Aspect of Eos",
            "Umbral flames, Aspect of Supay",
            "Witch's Staff, Aspect of Melinoë",
            "Witch's Staff, Aspect of Circe",
            "Witch's Staff, Aspect of Momus",
            "Witch's Staff, Aspect of Anubis",
            "Black Coat, Aspect of Melinoë",
            "Black Coat, Aspect of Selene",
            "Black Coat, Aspect of Nyx",
            "Black Coat, Aspect of Shiva",
        ]
