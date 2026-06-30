from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionList, Range, Toggle
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class LordOfTheRingsOnlineArchipelagoOptions:
    lotro_minfestivaltokens: LoTROMinFestivalTokens
    lotro_maxfestivaltokens: LoTROMaxFestivalTokens

class LordOfTheRingsOnlineGame(Game):
    name = "Lord of the Rings Online"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = LordOfTheRingsOnlineArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []

        constraints.extend([
            GameObjectiveTemplate(
                label="Favor quest given by GIVER.",
                data={
                    "GIVER": (lambda: self.quest_givers(), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ])

        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Obtain TOKENS festival tokens.",
                data={
                    "TOKENS": (lambda: range(self.lotro_minfestivaltokens, self.lotro_maxfestivaltokens), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ])
        wunit = sum(o.weight for o in game_objective_templates)

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Complete a daily quest.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=wunit,
            ),
            GameObjectiveTemplate(
                label="Complete a side quest.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=2*wunit,
            ),
            GameObjectiveTemplate(
                label="Complete a main quest.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=wunit,
            ),
            GameObjectiveTemplate(
                label="Do some craft.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=wunit,
            ),
            GameObjectiveTemplate(
                label="Send a mail.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=wunit,
            ),
        ])

        return game_objective_templates
    

    @property
    def lotro_minfestivaltokens(self) -> int:
        return self.archipelago_options.lotro_minfestivaltokens.value
    
    @property
    def lotro_maxfestivaltokens(self) -> int:
        return self.archipelago_options.lotro_maxfestivaltokens.value
    
    @staticmethod
    def quest_givers() -> List[str]:
        return ["a Dwarf","an Elf","a Hobbit","a Man"]
    


class LoTROMinFestivalTokens(Range):
    """
    [LoTRO] Minimum festival tokens to earn.
    """
    display_name = "[LoTRO] Min festival tokens"
    range_start = 1
    range_end = 100
    default = 5
    
class LoTROMaxFestivalTokens(Range):
    """
    [LoTRO] Maximum festival tokens to earn.
    """
    display_name = "[LoTRO] Max festival tokens"
    range_start = 1
    range_end = 100
    default = 10