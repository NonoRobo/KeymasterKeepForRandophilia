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
    mewgenics_include_enddayevents: MewgenicsIncludeEndDayEvents
    mewgenics_accessible_chapters: MewgenicsAccessibleChapters

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
                    label="Run an adventure with a team containing CLASS cats.",
                    data={
                        "CLASS": (lambda: self.mewgenics_unlocked_classes, class_count),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=class_count,
                ),
            ])

        if self.mewgenics_include_enddayevents:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Witness ENDOFDAY at the end of day.",
                    data={
                        "ENDOFDAY": (self.endofdayevents, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=10,
                )
            ])

        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Bring your team through LEVEL.",
                data={
                    "LEVEL": (lambda: self.mewgenics_accessible_chapters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            )
        ])

        return game_objective_templates
    
    
    @property
    def mewgenics_unlocked_classes(self) -> List[str]:
        return self.archipelago_options.mewgenics_unlocked_classes.value
    
    @property
    def mewgenics_include_enddayevents(self) -> bool:
        return self.archipelago_options.mewgenics_include_enddayevents.value
    
    @property
    def mewgenics_accessible_chapters(self) -> bool:
        return self.archipelago_options.mewgenics_accessible_chapters.value
    

    @staticmethod
    def endofdayevents() -> List[str]:
        return [
            # breeding
            "the birth of a kitten",
            "the birth of two kittens",
            "a cat dying",
            "a cat eating something it should not",
            "two cats fighting",
            "a cat changing (health or age)",
        ]
    
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

class MewgenicsIncludeEndDayEvents(Toggle):
    """
    [Mewgenics] Includes events at the End of Day (be warned of the randomness!)
    """
    display_name = "[Mewgenics] Include End of Day Events"
    default = False

class MewgenicsAccessibleChapters(OptionList):
    """
    [Mewgenics] Accessible chapters
    Chapters are:
    - Act 1
    -- Chapter 1: Alley
    -- Chapter 2: Sewers, Junkyard
    -- Chapter 3: Boneyard
    -- Chapter 4: Throbbing Domain
    - Act 2
    -- Chapter 1: Desert
    -- Chapter 2: Bunker, The Crater
    -- Chapter 3: The Core, The Moon
    -- Chapter 4: The Rift
    - Act 3
    -- Chapter 1: The Lab
    -- Chapter 2: Ice Age, The Future
    -- Chapter 3: Jurassic, The End
    -- Chapter 4: The Infinite
    """
    display_name = "[Mewgenics] Accessible chapters ([Act][Chapter]Path)"
    valid_keys = {
        "[A1][C1] Alley",
        "[A1][C2] Sewers",
        "[A1][C2] Junkyard",
        "[A1][C3] Caves",
        "[A1][C3] Boneyard",
        "[A1][C4] Throbbing Domain",
        "[A2][C1] Desert",
        "[A2][C2] Bunker",
        "[A2][C2] The Crater",
        "[A2][C3] The Core",
        "[A2][C3] The Moon",
        "[A2][C4] The Rift",
        "[A3][C1] The Lab",
        "[A3][C2] Ice Age",
        "[A3][C2] The Future",
        "[A3][C3] Jurassic",
        "[A3][C3] The End",
        "[A3][C4] The Infinite",
    }
    default = valid_keys