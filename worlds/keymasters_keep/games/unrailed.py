from __future__ import annotations

import functools
from typing import List, Dict

from dataclasses import dataclass
from Options import Range, Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class UnrailedArchipelagoOptions:
    pass

class UnrailedGame(Game):
    name = "Unrailed!"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = UnrailedArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []
        constraints.extend([
            GameObjectiveTemplate(
                label="Complete with WAGON fully upgraded.",
                data={"WAGON": (self.wagons, 1)},
            ),
        ])
        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        if self.randophilia_niko_is_here and self.randophilia_nono_is_here:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Reach biome BIOME in Endless Mode.",
                    data={
                        "BIOME": (self.biomes, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Reach a distance of DISTANCE in Endless Mode.",
                    data={
                        "DISTANCE": (self.endless_track_distances, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Win a Quick Mode game in DIFFICULTY.",
                    data={
                        "DIFFICULTY": (self.difficulties, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Reach the second biome in Time Mode.",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        return game_objective_templates
    

    @property
    def randophilia_niko_is_here(self) -> bool:
        return self.archipelago_options.randophilia_niko_is_here.value
    @property
    def randophilia_nono_is_here(self) -> bool:
        return self.archipelago_options.randophilia_nono_is_here.value
    

    @staticmethod
    def biomes() -> List[str]:
        return [
            "Plains",
            "Desert",
            "Snow",
            "Underwater",
            "Hell",
            "Space",
            "Mars",
            "Final Biome"
        ]
    
    @staticmethod
    def wagons() -> List[str]:
        return [
            "Brake",
            "Backinator",
            #"Cannon", # Versus Mode only
            "Collector",
            "Compass",
            "TWO Crafters",
            "Dynamite",
            "Ghost",
            "Light",
            "Milk",
            "Miner",
            "Slot Machine",
            "TWO Storages",
            "Supercharger",
            "TWO Tanks",
            "Transformer"
        ]
    
    @staticmethod
    def endless_track_distances() -> List[str]:
        return [
            "200m",
            "300m",
            "400m",
            "500m",
            "600m",
            "700m",
        ]
    
    @staticmethod
    def difficulties() -> List[str]:
        return [
            "Easy",
            "Medium",
            "Hard",
            #"Extreme",
        ]