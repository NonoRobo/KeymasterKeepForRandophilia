from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionList, Range, Toggle
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class PathOfExile2ArchipelagoOptions:
    poe2_minmapworth: PoE2MinMapWorth
    poe2_maxmapworth: PoE2MaxMapWorth

class PathOfExile2Game(Game):
    name = "Path of Exile 2"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = True
    options_cls = PathOfExile2ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []
        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Loot worth for WORTH Divine Orbs on one single map .",
                data={
                    "WORTH": (lambda: range(self.poe2_minmapworth, self.poe2_maxmapworth), 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ])
        wunit = sum(o.weight for o in game_objective_templates)

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Loot a Divine Orb.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=wunit,
            ),
            GameObjectiveTemplate(
                label="Play on a 3 tablets map.",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=3*wunit,
            ),
        ])

        return game_objective_templates
    
    
    @property
    def poe2_minmapworth(self) -> int:
        return self.archipelago_options.poe2_minmapworth.value
    
    @property
    def poe2_maxmapworth(self) -> int:
        return self.archipelago_options.poe2_maxmapworth.value


class PoE2MinMapWorth(Range):
    """
    [PoE2] Minimum worth (in Divine Orb count) that can be found in a map.
    """
    display_name = "[PoE2] Min worth in a map"
    range_start = 1
    range_end = 100
    default = 5
    
class PoE2MaxMapWorth(Range):
    """
    [PoE2] Maximum worth (in Divine Orb count) that can be found in a map.
    """
    display_name = "[PoE2] Max worth in a map"
    range_start = 1
    range_end = 100
    default = 10