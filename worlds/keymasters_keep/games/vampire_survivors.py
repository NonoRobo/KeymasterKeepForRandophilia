from __future__ import annotations

import functools
from typing import List

from dataclasses import dataclass

from Options import OptionSet, Toggle, Range
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class VampireSurvivorsArchipelagoOptions:
    niko_vs_include_dlc: VampireSurvivorsNikoIncludeDLC

class VampireSurvivorsGame(Game):
    name = "Vampire Survivors"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = VampireSurvivorsArchipelagoOptions
    

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()
        
        if self.randophilia_niko_is_here:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Complete a run on STAGE",
                    data={
                        "STAGE": (lambda: self.stages(
                            self.niko_LegacyOfTheMoonspell,
                            self.niko_TidesOfTheFoscari,
                            self.niko_EmergencyMeeting,
                            self.niko_OperationGuns,
                            self.niko_OdeToCastlevania,
                            self.niko_EmeraldDiorama,
                            self.niko_AnteChamber
                            ), 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),  
                GameObjectiveTemplate(
                    label="Complete a challenge on CHALLENGE",
                    data={
                        "CHALLENGE": (lambda: self.vs_challenge_stages, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Complete a run on this BONUS STAGE",
                    data={
                        "BONUS STAGE": (lambda: self.vs_bonus_stages, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Complete a run using CHARACTER",
                    data={
                        "CHARACTER": (lambda: self.characters(
                            self.niko_LegacyOfTheMoonspell,
                            self.niko_TidesOfTheFoscari,
                            self.niko_EmergencyMeeting,
                            self.niko_OperationGuns,
                            self.niko_OdeToCastlevania,
                            self.niko_EmeraldDiorama,
                            self.niko_AnteChamber
                            ), 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Complete a run using CHARACTER on STAGE",
                    data={
                        "CHARACTER": (lambda: self.characters(
                            self.niko_LegacyOfTheMoonspell,
                            self.niko_TidesOfTheFoscari,
                            self.niko_EmergencyMeeting,
                            self.niko_OperationGuns,
                            self.niko_OdeToCastlevania,
                            self.niko_EmeraldDiorama,
                            self.niko_AnteChamber
                            ), 1),
                        "STAGE": (lambda: self.stages(
                            self.niko_LegacyOfTheMoonspell,
                            self.niko_TidesOfTheFoscari,
                            self.niko_EmergencyMeeting,
                            self.niko_OperationGuns,
                            self.niko_OdeToCastlevania,
                            self.niko_EmeraldDiorama,
                            self.niko_AnteChamber
                            ), 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])
        return game_objective_templates
    
#Property
    @property
    def randophilia_niko_is_here(self) -> bool:
        return self.archipelago_options.randophilia_niko_is_here.value
    @property
    def niko_LegacyOfTheMoonspell(self) -> bool:
        return "Legacy of the Moonspell" in self.archipelago_options.niko_vs_include_dlc
    @property
    def niko_TidesOfTheFoscari(self) -> bool:
        return "Tides of the Foscari" in self.archipelago_options.niko_vs_include_dlc
    @property
    def niko_EmergencyMeeting(self) -> bool:
        return "Emergency Meeting" in self.archipelago_options.niko_vs_include_dlc
    @property
    def niko_OperationGuns(self) -> bool:
        return "Operation Guns" in self.archipelago_options.niko_vs_include_dlc
    @property
    def niko_OdeToCastlevania(self) -> bool:
        return "Ode to Castlevania" in self.archipelago_options.niko_vs_include_dlc
    @property
    def niko_EmeraldDiorama(self) -> bool:
        return "Emerald Diorama" in self.archipelago_options.niko_vs_include_dlc
    @property
    def niko_AnteChamber(self) -> bool:
        return "Ante Chamber" in self.archipelago_options.niko_vs_include_dlc

    def stages(self, dlc_moonspell: bool, dlc_foscari: bool, dlc_emergency_meeting: bool, dlc_operation_guns: bool, dlc_castlevania: bool, dlc_emerald_diorama: bool, dlc_ante_chamber: bool) -> List[str]:
        stages = self.vs_vanilla_stages
        if dlc_moonspell:
            stages.extend(self.vs_moonspell_stages)
        if dlc_foscari:
            stages.extend(self.vs_foscari_stages)
        if dlc_emergency_meeting:
            stages.extend(self.vs_emergency_meeting_stages)
        if dlc_operation_guns:
            stages.extend(self.vs_operation_guns_stages)
        if dlc_castlevania:
            stages.extend(self.vs_castlevania_stages)
        if dlc_emerald_diorama:
            stages.extend(self.vs_emerald_diorama_stages)
        if dlc_ante_chamber:
            stages.extend(self.vs_ante_chamber_stages)
        return stages

## STAGES ##
    @functools.cached_property
    def vs_vanilla_stages (self) -> List[str]:
        """Stages in vanilla game"""
        return [
            "Mad Forest",
            "Inlaid Library",
            "Dairy Plant",
            "Gallo Tower",
            "Cappella Magna",
        ]
    @functools.cached_property
    def vs_moonspell_stages (self) -> List[str]:
        """Stages in Legacy Of the moonspell game"""
        return [
            "Mt. Moonspell",
        ]
    @functools.cached_property
    def vs_foscari_stages (self) -> List[str]:
        """Stages in Tides of the Foscari game"""
        return [
            "Lake Foscari",
            "Abyss Foscari",
        ]
    @functools.cached_property
    def vs_emergency_meeting_stages (self) -> List[str]:
        """Stages in Emergency Meeting game"""
        return [
            "Polus Replica",
        ]
    @functools.cached_property
    def vs_operation_guns_stages (self) -> List[str]:
        """Stages in Operation Guns game"""
        return [
            "Neo Galuga",
            "Hectic Highway",
        ]
    @functools.cached_property
    def vs_castlevania_stages (self) -> List[str]:
        """Stages in Ode to Castlevania game"""
        return [
            "Ode To Castlevania",
        ]
    @functools.cached_property
    def vs_emerald_diorama_stages (self) -> List[str]:
        """Stages in Emerald Diorama game"""
        return [
            "Emerald Diorama",
        ]
    @functools.cached_property
    def vs_ante_chamber_stages (self) -> List[str]:
        """Stages in Ante Chamber game"""
        return [
            "Ante Chamber",
        ]
## BONUS STAGE ##
    @functools.cached_property
    def vs_bonus_stages (self) -> List[str]:
        """Bonus stages."""
        return [
            "II Molise",
            "Moongolow",
            "Whiteout",
            "The Coop",
            "Space 54",
            "Carlo Cart",
        ]
## CHALLENGE STAGE ##
    @functools.cached_property
    def vs_challenge_stages (self) -> List[str]:
        """Challenge stages."""
        return [
            "Green Acres",
            "The Bone Zone",
            "Boss Rash",
            "Laborratory",
            "Westwoods",
            "Bat Country",
            "Astral Stair",
            "Mazarella",
            "Tiny Bridge",
        ]
## CHARACTERS ##
    @functools.cached_property
    def vs_base_characters (self) -> List[str]:
        """Base characters."""
        return [
            "Antonio",
            "Imelda",
            "Pasqualina",
            "Gennaro",
            "Arca",
            "Porta",
            "Lama",
            "Poe",
            "Clerici",
            "Dommario",
            "Krochi",
            "Chrisine",
            "Pugnala",
            "Giovanna",
            "Poppea",
            "Concetta",
            "Mortaccio",
            "Cavallo",
            "Ramba",
            "O'Sole",
            "Ambrojoe",
            "Gallo",
            "Divano",
            "Zi'Assunta",
            "Sigma",
            "Robbert",
            "Zi'Appunta",
            "She-Moon",
            "Santa",
            "Gazebo",
            "Chula-Reh",
            "Space Dude",
        ]
    @functools.cached_property
    def vs_secret_base_characters (self) -> List[str]:
        """Secret base characters."""
        return [
            "Exdash",
            "Toastie",
            "Smith IV",
            "Random",
            "Marrabbio",
            "Avatar",
            "Minnah",
            "Leda",
            "Cosmo",
            "Peppino",
            "Trouser",
            "MissingN",
            "Gains",
            "Gyorunton",
            "Red Death",
            "Bats",
            "Rose",
            "Torino",
            "Scorej-Oni",
            "Gyoruntin",
            "Secretino",
            "Space Dette",
        ]
    @functools.cached_property
    def vs_moonspell_characters (self) -> List[str]:
        """Characters in Legacy Of the moonspell game"""
        return [
            "Miang",
            "Menya",
            "Syuuto",
            "Babi-Onna",
            "McCoy-Oni",
            "Megalo Menya",
            "Megalo Syuuto",
            "Gav'Et-Oni",
        ]
    @functools.cached_property
    def vs_foscari_characters (self) -> List[str]:
        """Characters in Tides of the Foscari game"""
        return [
            "Eleanor",
            "Maruto",
            "Keitha",
            "Luminaire",
            "Genevieve",
            "Je-Ne-Viv",
            "Sammy",
            "Rottin'Ghoul",
        ]
    @functools.cached_property
    def vs_emergency_meeting_characters (self) -> List[str]:
        """Characters in Emergency Meeting game"""
        return [
            "Crewmate",
            "Engineer",
            "Ghost",
            "Shapeshifter",
            "Guardian",
            "Impostor",
            "Scientist",
            "Horse",
            "Megalo Impostor",
        ]
    @functools.cached_property
    def vs_operation_guns_characters (self) -> List[str]:
        """Characters in Operation Guns game"""
        return [
            "Bill",
            "Lance",
            "Ariana",
            "Lucia",
            "Brad",
            "Browny",
            "Sheena",
            "Probotector",
            "Stanley",
            "Newt",
            "Bahamut",
            "Simondo",
        ]
    @functools.cached_property
    def vs_castlevania_characters (self) -> List[str]:
        """Characters in Ode to Castlevania game"""
        return [
            "Leon",
            "Sonia",
            "Trevor",
            "Christofer",
            "Simon",
            "Juste",
            "Richter",
            "Julius",
            "Grant",
            "John",
            "Jonathan",
            "Soma",
            "Charlotte",
            "Sypha",
            "Yoko",
            "Alucard",
            "Eric",
            "Hector",
            "Maria",
            "Shanoa",
        #HIDDEN CHARACTER
            "Quincy",
            "Maxim",
            "Henry",
            "Dracula",
            "Julia",
            "Carrie",
            "Rinaldo",
            "Mina",
            "Elizabeth",
            "Reinhardt",
            "Isaac",
            "Sara",
            "Vincent",
            "Albus",
            "Lisa",
            "Shaft",
            "Saint Germain",
            "Nathan",
            "Cornell",
            "Barlowe",
        ]
    @functools.cached_property
    def vs_castlevania_secret_characters (self) -> List[str]:
        """Secret characters in Ode to Castlevania game"""
        return [
            "Young Maria",
            "Familiar",
            "Innocent",
            "Blue Crescent Moon Cornell",
            "Ferryman",
            "Master Librarian",
            "Hammer",
            "Wind",
            "Hugh",
            "Morris",
            "Annette",
            "Tera",
            "Jonathan & Charlotte",
            "Charolotte & Jonathan",
            "Stella & Loretta",
            "Loretta & Stella",
            "Stella",
            "Loretta",
            "Brauner",
            "Soleil",
            "Dario",
            "Dmitrii",
            "Celia",
            "Graham",
            "Genya",
            "Joachim",
            "Walter",
            "Carmilla",
            "Cave Troll",
            "Fleaman",
            "Axe Armor",
            "Frozenshade",
            "Sniper",
            "Stone Skull",
            "Ruler Sword",
            "Persephone",
            "Keremet",
            "Astarte",
            "Droita",
            "Actrise",
            "Shrine Wizard",
            "Succubus",
            "Fake Trio",
            "Slogra and Gaibon",
            "Zephyr",
            "Jiangshi",
            "Blackmore",
            "Olrox",
            "Malphas",
            "Death",
            "Galamoth",
            "Megalo Elizabeth",
            "Megalo Olrox",
            "Megalo Death",
            "Megalo Dracula",
            "Chaos",
        ]
    @functools.cached_property
    def vs_emerald_characters(self) -> List[str]:
        """Characters in Emerald Diorama"""
        return [
            "Tsunanori",
            "Bonnie",
            "Formina",
            "Diva No. 5",
            "Ameya",
            "Siugnas",
            "Final Emperor",
            "Dolores",
            "Macha",
            "Lita",
            "Kugutsu",
            "Mr. S"
        ]
    @functools.cached_property
    def vs_emerald_secret_characters(self) -> List[str]:
        """Secret Character in Emerald Diorama"""
        return [
            "Lolo",
            "Kina",
            "Imakoo",
            "Door",
        ]
    @functools.cached_property
    def vs_ante_characters(self) -> List[str]:
        """Characters in Ante Chamber"""
        return[
            "Jimbo",
            "Canio",
            "Chicot",
            "Perkeo",
        ]
class VampireSurvivorsNikoIncludeDLC(OptionSet):
    """
    The DLC Niko wants to include in the pool.
    The DLCs are:
    - Legacy of the Moonspell
    - Tides of the Foscari
    - Emergency Meeting
    - Operation Guns
    - Ode to Castlevania
    - Emerald Diorama
    - Ante Chamber
    """
    display_name = "[NIKO] Vampire Survivors Included DLCs"
    valid_keys = {
        "Legacy of the Moonspell",
        "Tides of the Foscari",
        "Emergency Meeting",
        "Operation Guns",
        "Ode to Castlevania",
        "Emerald Diorama",
        "Ante Chamber"
    }
    default = valid_keys