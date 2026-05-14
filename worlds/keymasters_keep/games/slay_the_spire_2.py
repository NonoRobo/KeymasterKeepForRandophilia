from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class SlayTheSpire2ArchipelagoOptions:
    pass

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
        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        #### Weight details
        # 50 % : Niko & Nono Normal run
        # 50 % : Nono Custom run

        # Custom Runs
        custom_runs_total_weight: int = 1 # init to 1 even if no custom runs to ensure a valid minimum
        if self.randophilia_nono_is_here:
            game_objective_templates.extend(self.custom_objectives())
            custom_runs_total_weight = sum(o.weight for o in game_objective_templates)

        # Normal Runs
        if self.randophilia_niko_is_here or self.randophilia_nono_is_here:
            total_players: int = (1 if self.randophilia_niko_is_here else 0) + (1 if self.randophilia_nono_is_here else 0)
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Meet the Architect with the CHARACTER in Ascension ASCENSION",
                    data={
                        "CHARACTER": (self.characters, 1),
                        "ASCENSION": (self.ascension_levels, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=custom_runs_total_weight * total_players, # Niko doesn't do Customs, so we need extra weight when he's around
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
    def randophilia_nono_is_here(self) -> bool:
        return self.archipelago_options.randophilia_nono_is_here.value
    
    @property
    def randophilia_niko_is_here(self) -> bool:
        return self.archipelago_options.randophilia_niko_is_here.value
    
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