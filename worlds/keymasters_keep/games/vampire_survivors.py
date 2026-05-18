from __future__ import annotations

import functools
import logging
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

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []
        constraints.extend([
            GameObjectiveTemplate(
                label="Don't take this passives : PASSIVE",
                data={
                    "PASSIVE": (lambda: self.passives(
                            self.niko_LegacyOfTheMoonspell,
                            self.niko_TidesOfTheFoscari,
                            self.niko_EmergencyMeeting,
                            self.niko_OperationGuns,
                            self.niko_OdeToCastlevania,
                            self.niko_EmeraldDiorama,
                            self.niko_AnteChamber
                            ), 2),
                },
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Start with this Arcana : ARCANA",
                data={
                    "ARCANA": (self.vs_arcana, 1),
                },
                weight=1,
            ),
            GameObjectiveTemplate(
                label="None",
                data={},
                weight=sum(o.weight for o in constraints) * 10,
            ),
        ])
        return constraints    

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
                    weight=2,
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
                    label="Complete a run on BONUS STAGE",
                    data={
                        "BONUS STAGE": (lambda: self.vs_bonus_stages, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Complete a run playing CHARACTER",
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
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Complete a run playing CHARACTER on STAGE",
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
                    weight=4,
                ),
                GameObjectiveTemplate(
                    label="Complete a run with this weapon: WEAPON_EVOLUTION",
                    data={
                        "WEAPON_EVOLUTION": (lambda: self.weapons_evolution(
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
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Complete a run with this weapon: WEAPON_UNION",
                    data={
                        "WEAPON_UNION": (lambda: self.weapons_union(
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
                    label="Complete a run playing CHARACTER with this weapon: WEAPON_EVOLUTION",
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
                        "WEAPON_EVOLUTION": (lambda: self.weapons_evolution(
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
                    weight=4,
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
        stages = list(self.vs_vanilla_stages)
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
    def characters(self, dlc_moonspell: bool, dlc_foscari: bool, dlc_emergency_meeting: bool, dlc_operation_guns: bool, dlc_castlevania: bool, dlc_emerald_diorama: bool, dlc_ante_chamber: bool) -> List[str]:
        charact = list(self.vs_base_characters)
        if dlc_moonspell:
            charact.extend(self.vs_moonspell_characters)
        if dlc_foscari:
            charact.extend(self.vs_foscari_characters)
        if dlc_emergency_meeting:
            charact.extend(self.vs_emergency_meeting_characters)
        if dlc_operation_guns:
            charact.extend(self.vs_operation_guns_characters)
        if dlc_castlevania:
            charact.extend(self.vs_castlevania_characters)
        if dlc_emerald_diorama:
            charact.extend(self.vs_emerald_characters)
        if dlc_ante_chamber:
            charact.extend(self.vs_ante_characters)
        return charact
    def weapons_evolution(self, dlc_moonspell: bool, dlc_foscari: bool, dlc_emergency_meeting: bool, dlc_operation_guns: bool, dlc_castlevania: bool, dlc_emerald_diorama: bool, dlc_ante_chamber: bool) -> List[str]:
        weapon = list(self.vs_vanilla_weapons_evolution)
        if dlc_moonspell:
            weapon.extend(self.vs_moonspell_weapons_evolution)
        if dlc_foscari:
            weapon.extend(self.vs_foscari_weapons_evolution)
        if dlc_emergency_meeting:
            weapon.extend(self.vs_meeting_weapons_evolution)
        if dlc_operation_guns:
            weapon.extend(self.vs_guns_weapons_evolution)
        if dlc_castlevania:
            weapon.extend(self.vs_castlevania_weapons_evolution)
        if dlc_emerald_diorama:
            weapon.extend(self.vs_diorama_weapons_evolution)
        if dlc_ante_chamber:
            weapon.extend(self.vs_chamber_weapons_evolution)
        return weapon
    def weapons_union(self, dlc_moonspell: bool, dlc_foscari: bool, dlc_emergency_meeting: bool, dlc_operation_guns: bool, dlc_castlevania: bool, dlc_emerald_diorama: bool, dlc_ante_chamber: bool) -> List[str]:
        union = list(self.vs_vanilla_weapons_union)
        if dlc_foscari:
            union.extend(self.vs_foscari_weapons_union)
        if dlc_castlevania:
            union.extend(self.vs_castlevania_weapons_union)
        return union
    def passives(self, dlc_moonspell: bool, dlc_foscari: bool, dlc_emergency_meeting: bool, dlc_operation_guns: bool, dlc_castlevania: bool, dlc_emerald_diorama: bool, dlc_ante_chamber: bool) -> List[str]:
        passive = list(self.vs_vanilla_passive)
        if dlc_foscari:
            passive.extend(self.vs_foscari_passive)
        if dlc_emergency_meeting:
            passive.extend(self.vs_meeting_passive)
        if dlc_operation_guns:
            passive.extend(self.vs_guns_passive)
        if dlc_ante_chamber:
            passive.extend(self.vs_ante_passive)
        return passive

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
## WEAPONS EVOLUTION
    @functools.cached_property
    def vs_vanilla_weapons_evolution(self) -> List[str]:
        """Vanilla weapons"""
        return[
            "Bloody Tear",
            "Holy Wand",
            "Thousand Edge",
            "Death Spiral",
            "Heaven Sword",
            "Unholy Vespers",
            "Hellfire",
            "Soul Eater",
            "La Borra",
            "NO FUTURE",
            "Thunder Loop",
            "Gorgeous Moon",
            "Vicious Hunger",
            "Mannajja",
            "Valkyrie Turner",
            "Infinite Corridor",
            "Crimsons Shroud",
            "Bi-Bracelet",
            "Tri-Bracelet",
            "Ashes Muspell",
            ## EXTRA
            "Anima of Mortaccio",
            "Yatta Daikarin",
            "Carozza!",
            "Pofusione D'Amore",
            "Mazo Familiar",
            "Gunastrophe",
            "Celestial Voulge",
            "Seraphic Cry",
            "Embrace of Gaea",
            "Kyra-Stones",
            "Photonstorm",
            "Wicked Ruler",
        ]
    @functools.cached_property
    def vs_moonspell_weapons_evolution(self) -> List[str]:
        """Evolution in Legacy of Moonspell"""
        return[
            "Festive Winds",
            "Godai Shuffle",
            "Echo Night",
            "J'Odore",
            "Muramasa",
            "Boo Roo Boolle",
        ]
    @functools.cached_property
    def vs_foscari_weapons_evolution(self) -> List[str]:
        """Evolution in Tides of the Foscari"""
        return[
            "Legionnaire",
            "Millionaire",
            "Luminaire",
            "Ophion",
        ]
    @functools.cached_property
    def vs_meeting_weapons_evolution(self) -> List[str]:
        """Evolution in Emergency Meetinf"""
        return[
            "Emergency Meeting",
            "Crossed Wires",
            "Paranormal Scan",
            "Unjust Ejection", 
            "Clear Asteroids",
            "Impostongue",
            "Rocket Science",
        ]
    @functools.cached_property
    def vs_guns_weapons_evolution(self) -> List[str]:
        """Evolution in Operation Guns"""
        return[
            "Prototype A",
            "Prototype B",
            "Prototype C",
            "Pronto Beam",
            "Fire-L3GS",
            "Wave Beam",
            "MultiStage Missiles",
            "Atmo-Torpedo",
            "BFC2000-AD",
            "Time Warp",
            "Big Fuzzy Fist",
        ]
    @functools.cached_property
    def vs_castlevania_weapons_evolution(self) -> List[str]:
        """Evolution in Ode To Castlevania"""
        return[
            "Vampire Killer",
            "Spirit Tornatdo Tip",
            "Cross Crasher Tip",
            "Hydrostormer Tip",
            "Crissaegrim Tip",
            "Mormegil Tip",
            "Daybreaker Tip",
            "Aurablaster Tip",
            "Yagyu Shuriken",
            "Bwaka Knife",
            "Long Inus",
            "Stellar Blade",
            "Wrecking Ball",
            "Jewel Gun",
            "The TPG",
            "Meal Ticket",
            "Salamander",
            "Cocytus",
            "Pneuma Tempestas",
            "Gemma Torpor",
            "Tenebris Tonitrus",
            "Keremet Morbus",
            "Nightmare",
            "Sanctuary",
            "Stamazza",
            "Moon Rod",
            "Thunderbolt Spear",
            "Gungnir-Souris",
            "Dark Iron Shield",
            "Sacred Beasts Tower Shield",
            "Rune Sword",
            "Alucard Swords",
            "Vol Confodere",
            "Melio Confodere",
            "Nitesco",
            "Acerbatus",
            "Rapidus Fio",
            "Vol Luminato",
            "Vol Umbra",
            "Claimh Solais",
        ]
    @functools.cached_property
    def vs_diorama_weapons_evolution(self) -> List[str]:
        """Evolution in Emerald Diorama"""
        return[
            "Dress Sword",
            "Espada Ropera",
            "Lordstar",
            "Dayblade",
            "Pursuant Blades",
            "Zweihander",
            "Galatyn",
            "Pressure Point",
            "Gilded Hand",
            "Triangle Kick",
            "Hecaton Machine Gun",
            "Divergence",
            "Hydra Cannon",
            "Hyperion Bazooka",
            "Pendragon",
            "Jetstream",
            "Gekkabijin",
            "Falconwind",
            "Blood Chalice",
            "Feather Spear",
            "Lohengrin",
            "Rings of Calamity",
            "Emerald Wave",
        ]
    @functools.cached_property
    def vs_chamber_weapons_evolution(self) -> List[str]:
        """Evolution in Ante Chamber"""
        return[
            "NaneInferno",
            "Cavendish",
            "Royal Flush",
            "Negative Space",
        ]
## Union
    @functools.cached_property
    def vs_vanilla_weapons_union(self) -> List[str]:
        """Union Weapons in base game"""
        return[
            "Vandalier",
            "Phieraggi",
            "Fuwalafuwaloo",
        ]
    @functools.cached_property
    def vs_foscari_weapons_union(self) -> List[str]:
        """Union Weapons in Tides of the Foscari"""
        return[
            "SpellStrom",
        ]
    @functools.cached_property
    def vs_castlevania_weapons_union(self) -> List[str]:
        """Union Weapons in Ode to Castlevania"""
        return[
            "Trinum Custodem",
            "Power of Sire",
            "Million Cut",
            "Ninth Circle",
            "Dies Irae",
            "Kardia Phlegeton",
            "Lapiste Tepisto",
            "Darkness Illusion",
            "Carnage Heart",
            "Hydro Pump Climax",
            "Arch Angle",
            "Spirit of Light",
            "Power of Lire",
            "Legacy of Death: Soul River",
            "Vjaya Sisters",
            "Venus Crescent",
            "Dark Frogamorphosis",
            "Clock Tower",
        ]
## PASIVE
    @functools.cached_property
    def vs_vanilla_passive(self) -> List[str]:
        """Passive in XBase game"""
        return[
            "Spinach",
            "Armor",
            "Hollow Heart",
            "Pummarola",
            "Empty Tome",
            "Candelabrador",
            "Bracer",
            "Spellbinder",
            "Duplicator",
            "Wings",
            "Attractorb",
            "Clover",
            "Crown",
            "Stone Mask",
            "Skull O'Maniac",
            "Tirajisù",
            "Torrona's Box",
            "Silber Ring",
            "Gold Ring",
            "Metaglio Left",
            "Metaglio Right",
            ## EXTRA
            "Parm Aegis",
            "Karoma's Mana",
        ]
    @functools.cached_property
    def vs_foscari_passive(self) -> List[str]:
        """Passive in Tides of the Foscari"""
        return[
            "Academy Badge",
        ]
    @functools.cached_property
    def vs_meeting_passive(self) -> List[str]:
        """Passive in Emergency Meeting"""
        return[
            "Mini Crewmate",
            "Mini Engineer",
            "Mini Ghost",
            "Mini Shapeshifter",
            "Mini Guardian",
            "Mini Impostor",
            "Mini Scientist",
            "Mini Horse",
        ]
    @functools.cached_property
    def vs_guns_passive(self) -> List[str]:
        """Passive in Operation Guns"""
        return[
            "Weapon Powers-Up",
        ]
    @functools.cached_property
    def vs_ante_passive(self) -> List[str]:
        """Passive in Ante Chamber"""
        return[
            "Outer Saboter",
        ]
## ARCANA
    @staticmethod
    def vs_arcana() -> List[str]:
        return[
            "0 - Game Killer",
            "I - Gemini",
            "II - Twilight Requiem",
            "III - Tragic Princess",
            "IV - Awake",
            "V - Chaos in the Dark Night",
            "VI - Sarabande of Healing",
            "VII - Iron Blue Will",
            "VIII- Mad Groove",
            "IX - Divine Bloodline",
            "X - Begenning",
            "XI - Walts of Pearls",
            "XII - Out of Bounds",
            "XIII - Wicked Season",
            "XIV - Jail of Crystal",
            "XV - Disco of Gold",
            "XVI - Slash",
            "XVII - Lost & Found Painting",
            "XVIII - Boogaloo of Illusions",
            "XIX - Heart of Fire",
            "XX - Silent Old Sanctuary",
            "XXI - Blood Astronomia",
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