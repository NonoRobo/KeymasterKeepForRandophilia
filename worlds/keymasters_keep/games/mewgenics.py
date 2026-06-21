from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionList, Toggle
from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

@dataclass
class MewgenicsArchipelagoOptions:
    mewgenics_unlocked_classes: MewgenicsUnlockedClasses

class MewgenicsGame(Game):
    name = "Mewgenics"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = True
    options_cls = MewgenicsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []

        constraints.extend([
            GameObjectiveTemplate(
                label="Have at least one CLASS cat in your team.",
                data={"CLASS": (lambda: self.mewgenics_unlocked_classes, 1)},
            ),
        ])

        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        for class_count in range(1, 4+1):
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Win a run with a team containing CLASS cats.",
                    data={
                        "CLASS": (lambda: self.mewgenics_unlocked_classes, class_count),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=class_count,
                ),
            ])

        return game_objective_templates
    
    
    @property
    def mewgenics_unlocked_classes(self) -> List[str]:
        return self.archipelago_options.mewgenics_unlocked_classes.value
    
class MewgenicsUnlockedClasses(OptionList):
    """
    [Mewgenics] Unlocked cat classes.
    Classes are:
    - Collarless
    - Fighter
    - Hunter
    - Mage
    - Tank
    - Cleric
    - Thief
    - Necromancer
    - Tinkerer
    - Butcher
    - Druid
    - Psychic
    - Monk
    - Jester
    """
    display_name = "[Mewgenics] Unlocked classes"
    valid_keys = {
        "Collarless",
        "Fighter",
        "Hunter",
        "Mage",
        "Tank",
        "Cleric",
        "Thief",
        "Necromancer",
        "Tinkerer",
        "Butcher",
        "Druid",
        "Psychic",
        "Monk",
        "Jester",
    }
    default = valid_keys