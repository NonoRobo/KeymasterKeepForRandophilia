from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionList, Toggle
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class SlayTheSpire2ArchipelagoOptions:
    sts2_include_custom: STS2IncludeCustom
    sts2_include_duo: STS2IncludeDuo
    sts2_players_reserving_rooms: STS2PlayersReservingRoom

class SlayTheSpire2Game(Game):
    name = "Slay the Spire 2"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = SlayTheSpire2ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []
        constraints.extend([
            GameObjectiveTemplate(
                label="Complete with Ascension ASCENSION unless indicated otherwise.",
                data={"ASCENSION": (self.ascension_levels, 1)},
            ),
        ])

        if self.sts2_players_reserving_rooms.count > 0:
            constraints.extend([
                GameObjectiveTemplate(
                    label="This room can only be entered by PLAYER.",
                    data={"PLAYER": {self.sts2_players_reserving_rooms, 1}},
                )
            ])

        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        #### Weight details
        # 50 % : Normal run
        # 50 % : Custom run

        # Custom Runs
        custom_runs_total_weight: int = 1 # init to 1 even if no custom runs to ensure a valid minimum
        if self.sts2_include_custom:
            game_objective_templates.extend(self.custom_objectives())
            custom_runs_total_weight = sum(o.weight for o in game_objective_templates)

        # Normal Runs
        game_objective_templates.extend([
            GameObjectiveTemplate(
                label="Meet the Architect with the CHARACTER in Ascension ASCENSION",
                data={
                    "CHARACTER": (self.characters, 1),
                    "ASCENSION": (self.ascension_levels, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=custom_runs_total_weight,
            ),
        ])

        # Duo Runs
        if self.sts2_include_duo:
            game_objective_templates.extends([
                GameObjectiveTemplate(
                    label="Meet the Architect as a Duo with the CHAR1 and the CHAR2 in Ascension ASCENSION",
                    data={
                        "CHAR1": (self.characters, 1),
                        "CHAR2": (self.characters, 1),
                        "ASCENSION": (self.ascension_levels, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=custom_runs_total_weight,
                ),
            ])

        return game_objective_templates
    
    def custom_objectives(self) -> List[GameObjectiveTemplate]:
        """ Based on the configuration, generates a list of objective templates for Custom mode. """
        objectives: List[GameObjectiveTemplate] = list()
        objectives.extend([
            GameObjectiveTemplate(
                label="Win a custom run with CHARACTER, with modifier BAD_MODIFIER, in Ascension ASCENSION",
                data={
                    "CHARACTER": (self.characters, 1),
                    "BAD_MODIFIER": (self.bad_modifiers, 1),
                    "ASCENSION": (self.ascension_levels, 1)
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
        ])
        for good_modifier_count in range(1, 2 + 1):
            objectives.extend([
                GameObjectiveTemplate(
                    label="Win a custom run with CHARACTER, with modifiers MODIFIERS and BAD_MODIFIER, in Ascension ASCENSION",
                    data={
                        "CHARACTER": (self.characters, 1),
                        "MODIFIERS": (self.all_good_modifiers, good_modifier_count),
                        "BAD_MODIFIER": (self.bad_modifiers, 1),
                        "ASCENSION": (self.ascension_levels, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight = 1 + good_modifier_count,
                ),
            ])
        return objectives
    

    @property
    def sts2_include_custom(self) -> bool:
        return self.archipelago_options.sts2_include_custom.value
    
    @property
    def sts2_include_duo(self) -> bool:
        return self.archipelago_options.sts2_include_duo.value
    
    @property
    def sts2_players_reserving_rooms(self) -> List[str]:
        return self.archipelago_options.sts2_players_reserving_rooms.value
    

    @staticmethod
    def ascension_levels() -> range:
        return range(0, 10+1, 1)

    @staticmethod
    def characters() -> List[str]:
        return ["Iron Clad","Silent","Regent","Necrobinder","Defect"]
  
    def all_good_modifiers(self) -> List[str]:
        return self.except_bicolor_modifiers() + self.bicolor_modifiers()

    @staticmethod
    def except_bicolor_modifiers() -> List[str]:
        return ["Draft","Sealed Deck","Hoarder","Specialized","Insanity","All Star","Flight","Vintage"]
    
    @staticmethod
    def bicolor_modifiers() -> List[str]:
        return ["Ironclad Cards","Silent Cards","Regent Cards","Necrobinder Cards","Defect Cards"]

    @staticmethod
    def bad_modifiers() -> List[str]:
        return ["Deadly Events","Cursed Run","Bug Game Hunter","Midas","Murderous","Night Terrors","Terminal"]
    

#
# OPTIONS
#

class STS2IncludeCustom(Toggle):
    """
    [STS2] Include Custom Runs in trials
    """
    display_name = "STS2 Include Custom"
    default = True

class STS2IncludeDuo(Toggle):
    """
    [STS2] Include Duo Runs in trials
    """
    display_name = "STS2 Include Duo"
    default = False

class STS2PlayersReservingRoom(OptionList):
    """
    [STS2] Players who can have their name in room restriction
    """
    display_name = "STS2 Players Reserving Room"
    default = {}