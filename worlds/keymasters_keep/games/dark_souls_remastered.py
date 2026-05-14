from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import Toggle
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class DarkSoulsRemasteredArchipelagoOptions:
    niko_dsr_include_aota: DSRNikoIncludeAotA

class DarkSoulsRemasteredGame(Game):
    name = "Dark Souls Remastered"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = DarkSoulsRemasteredArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        # Niko's objectives
        if self.randophilia_niko_is_here:
            nikobjectives: List[GameObjectiveTemplate] = list()
            nikobjectives.extend(self.dsr_objectives(include_aotA=self.niko_dsr_include_aota))
            game_objective_templates.extend(nikobjectives)
        return game_objective_templates

    def dsr_objectives(self, include_aotA: bool) -> List[GameObjectiveTemplate]:
        objectives = []
        objectives.extend([
            GameObjectiveTemplate(
                label="Slain BOSS",
                data={
                    "BOSS": (lambda: self.boss(dlc=include_aotA), 1)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
             GameObjectiveTemplate(
                label="Travel between this two areas : AREA",
                data={
                    "AREA": (lambda: self.areas(dlc=include_aotA), 2)
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
        ])
        return objectives

    # Property
    @property
    def randophilia_niko_is_here(self) -> bool:
        return self.archipelago_options.randophilia_niko_is_here.value
    @property
    def niko_dsr_include_aota(self) -> int:
        return self.archipelago_options.niko_dsr_include_aota.value
    

    def boss(self, dlc:bool) -> List[str]:
        if dlc:
            return self.dsr_vanillabosses + self.dsr_aotabosses
        else:
            return self.dsr_vanillabosses
        
    def areas(self, dlc:bool) -> List[str]:
        if dlc:
            return self.dsr_vanilla_area + self.dsr_aot_areas
        else:
            return self.dsr_vanilla_area

    @functools.cached_property
    def dsr_vanilla_area (self) -> List[str]:
        """Areas in vanilla game"""
        return [
            "Northern Undean Asylum",
            "Firelink Shrine",
            "Undead Burg",
            "Undead Parish",
            "Depths",
            "Blighttown",
            "Quelaag's Domain",
            "Sen's Fortress",
            "Anor Londo",
            "Darkroot Garden",
            "Darkroot Basin",
            "New Londo Ruins",
            "The Duke's Archives",
            "Crystal Cave",
            "Demon Ruins",
            "Lost Izalith",
            "The Catacombs",
            "Tomb of the Giants",
            "Ash Lake",
            "The Painted World of Ariamis",
            "The Great Hollow",
            "The Abyss",
            "The Valley of Drakes",
            "The Kiln of the First Flame"
        ]
    @functools.cached_property
    def dsr_vanillabosses(self) -> List[str]:
        """Boss in vanilla game"""
        return [
            "Asylum Demon",
            "Bell Gargoyles",
            "Ceaseless Discharge",
            "Centipede Demon",
            "Chaos Witch Quelaag",
            "Crossbreed Priscilla",
            "Dark Sun Gwyndolin",
            "Demon Firesage",
            "Four Kings",
            "Gaping Dragon",
            "Great Grey Wolf Sif",
            "Gwyn, Lord of Cinder",
            "Iron Golem",
            "Moonlight Butterfly",
            "Nito, Lord of the Dead",
            "Ornstein and Smough",
            "Pinwheel",
            "Seath the Scaleless",
            "Stray Demon",
            "Taurus Demon",
            "The Bed of Chaos"
        ]
    
    @functools.cached_property
    def dsr_aot_areas(self) -> List[str]:
        """Areas in Artorias of the Abyss DLC game"""
        return [
            "Sanctuary Garden",
            "Oolacile Township",
            "Oolacile Sanctuary",
            "Royal Wood",
            "Chasm of the Abyss"
        ]
    
    @functools.cached_property
    def dsr_aotabosses(self) -> List[str]:
        """Boss in Artorias of the Abyss DLC game"""
        return [
            "Artorias the Abysswalker",
            "Black Dragon Kalameet",
            "Manus, Father of the Abyss",
            "Sanctuary Guardian"
        ]
          
class DSRNikoIncludeAotA(Toggle):
    """
    Niko wants to include Artorias of the Abyss in the Keep.
    """
    display_name = "[Niko] Include AotA"
    default = True