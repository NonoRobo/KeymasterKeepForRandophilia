from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionList, Toggle
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class TeamfightTacticsArchipelagoOptions:
    tft_includedoubleupmode: TFTIncludeDoubleUpMode

class TeamfightTacticsGame(Game):
    name = "Teamfight Tactics"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = TeamfightTacticsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []

        if self.tft_includedoubleupmode:
            constraints.extend([
                GameObjectiveTemplate(
                    label="Play solo",
                    data={},
                ),
                GameObjectiveTemplate(
                    label="Play Douple Up",
                    data={},
                ),
            ])

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
    
    
    @property
    def tft_includedoubleupmode(self) -> bool:
        return self.archipelago_options.tft_includedoubleupmode.value



class TFTIncludeDoubleUpMode(Toggle):
    """
    [TFT] Include Solo/Double Up Mode as constraints
    """
    display_name = "[TFT] Include solo/duo mode"
    default = False