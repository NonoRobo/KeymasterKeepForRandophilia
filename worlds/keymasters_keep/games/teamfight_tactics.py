from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionList, Toggle
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class TeamfightTacticsArchipelagoOptions:
    pass

class TeamfightTacticsGame(Game):
    name = "Teamfight Tactics"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = TeamfightTacticsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []
        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Finish a game as Top RANK.",
                data={
                    "RANK": (lambda: range(1, 4), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Play a COST cost reroll comp.",
                data={
                    "COST": (lambda: range(1, 3), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win with a 5 cost 2 stars unit.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ])

        return game_objective_templates

