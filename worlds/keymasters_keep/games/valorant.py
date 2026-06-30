from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionList, Range, Toggle
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class ValorantArchipelagoOptions:
    valo_maxkillinround: ValoMaxKillInRound

class ValorantGame(Game):
    name = "Valorant"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = ValorantArchipelagoOptions

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
                label="Kill KILLS times in a single round.",
                data={
                    "KILLS": (lambda: range(2, self.valo_maxkillinround), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Kill twice with one skill or bullet.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Plant the Spike.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Defuse the Spike.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ])

        return game_objective_templates
    

    @property
    def valo_maxkillinround(self) -> int:
        return self.archipelago_options.valo_maxkillinround.value


class ValoMaxKillInRound(Range):
    """
    [Valorant] Max Kills in a single round.
    """
    display_name = "[Valo] Max Kills in a Round"
    range_start = 2
    range_end = 10
    default = 3