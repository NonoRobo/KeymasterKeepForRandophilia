from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle, Range
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class CelesteArchipelagoOptions:
    niko_celeste_include_core: CelesteNikoIncludeCore
    niko_celeste_include_farewell: CelesteNikoIncludeFarewell
    niko_celeste_include_c_side: CelesteNikoIncludeCFace
    niko_celeste_include_b_side: CelesteNikoIncludeBFace

class CelesteGame(Game):
    name = "Celeste"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = CelesteArchipelagoOptions
    
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []
        constraints.extend([
            GameObjectiveTemplate(
                label="Collect between NUMBER1 and NUMBER2 strawberries.",
                data={
                    "NUMBER1": (self.berry_count_range1, 1),
                    "NUMBER2": (self.berry_count_range2, 1),
                },
                weight=10,
            ),
            GameObjectiveTemplate(
                label="None",
                data={},
                weight=90,
            ),
        ])
        return constraints

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()
        
        if self.randophilia_niko_is_here:
            nikobjectives: List[GameObjectiveTemplate] = list()
            nikobjectives.extend(self.celeste_objectives(include_core=self.niko_celeste_include_core, include_farewell=self.niko_celeste_include_farewell))
            game_objective_templates.extend(nikobjectives)
        return game_objective_templates
 
    def celeste_objectives(self, include_core: bool, include_farewell: bool) -> List[GameObjectiveTemplate]:
        celeste_objectives: List[GameObjectiveTemplate] = list()
        celeste_objectives.append(
            GameObjectiveTemplate(
                label="Complete the CHAPTER on FACE",
                data={
                    "CHAPTER": (lambda: self.get_celeste_chapters(include_core=include_core, include_farewell=include_farewell), 1),
                    "FACE": (lambda: self.get_celeste_face(include_b=self.niko_celeste_include_b_side, include_c=self.niko_celeste_include_c_side), 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            )
        )
        
        return celeste_objectives   
    
    def get_celeste_chapters(self, include_core: bool, include_farewell: bool) -> List[str]:
        chapters = self.celeste_vanillachapters
        if include_core:
            chapters.extend(["Chapter 8: Core"])
        if include_farewell:
            chapters.extend(["Chapter 9: Farewell"])
        return chapters
    
    def get_celeste_face(self, include_b: bool, include_c: bool) -> List[str]:
        face: List[str] = ["Face A"]
        if include_b:
            face.extend(["Face B"])
        if include_c:
            face.extend(["Face C"])
        return face
    
    @staticmethod
    def berry_count_range1() -> range:
        return range(0, 3)
    @staticmethod
    def berry_count_range2() -> range:
        return range(5, 15)
    
    #Property
    @property
    def randophilia_niko_is_here(self) -> bool:
        return self.archipelago_options.randophilia_niko_is_here.value
    @property
    def niko_celeste_include_core(self) -> int:
        return self.archipelago_options.niko_celeste_include_core.value
    @property
    def niko_celeste_include_b_side(self) -> int:
        return self.archipelago_options.niko_celeste_include_b_side.value
    @property
    def niko_celeste_include_c_side(self) -> int:
        return self.archipelago_options.niko_celeste_include_c_side.value
    @property
    def niko_celeste_include_farewell(self) -> int:
        return self.archipelago_options.niko_celeste_include_farewell.value
             
    @functools.cached_property
    def celeste_vanillachapters(self) -> List[str]:
        """Chapters from the base game, excluding the Core and Farewell."""
        return [
            "Chapter 1: Forsaken City",
            "Chapter 2: Old Site",
            "Chapter 3: Celestial Resort",
            "Chapter 4: Golden Ridge",
            "Chapter 5: Mirror Temple",
            "Chapter 6: Reflection",
            "Chapter 7: The Summit"
        ]
    

class CelesteNikoIncludeCore(Toggle):
    """
    Niko wants to include the eighth chapter, the Core, in the Keep.
    """
    display_name = "[Niko] Include The Core"
    default = False

class CelesteNikoIncludeFarewell(Toggle):
    """
    Niko wants to include the farewell chapter in the Keep.
    """
    display_name = "[Niko] Include Farewell"
    default = False

class CelesteNikoIncludeBFace(Toggle):
    """
    Niko wants to include the B-side remixes of the main chapters in the Keep.
    """
    display_name = "[Niko] Include B-Face"
    default = False

class CelesteNikoIncludeCFace(Toggle):
    """
    Niko wants to include the C-side remixes of the main chapters in the Keep. Note that the C-sides are generally much more difficult than the B-sides, so enabling this option will add a lot of difficult objectives to the pool.
    """
    display_name = "[Niko] Include C-Face"
    default = False
    
 