from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionList, Toggle
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class LeagueOfLegendsArchipelagoOptions:
    pass

class LeagueOfLegendsGame(Game):
    name = "League of Legends"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = LeagueOfLegendsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []
        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Play a game.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Perform a Double Kill.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Destroy a tower.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Steal an objective.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ])

        return game_objective_templates

