from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class OuterWildsArchipelagoOptions:
    pass

class OuterWildsGame(Game):
    name = "Outer Wilds"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = OuterWildsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []
        return constraints
    
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        if self.randophilia_nono_is_here:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Talk to CHARACTER.",
                    data={
                        "CHARACTER": (self.characters, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1
                ),
                GameObjectiveTemplate(
                    label="Reach the 'ENDING' ending.",
                    data={
                        "ENDING": (self.endings, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1
                ),
            ])

        return game_objective_templates
    
    def all_planets_objectives(self) -> List[GameObjectiveTemplate]:
        return (
            self.planet_picture_objective("(Timber Hearth)", self.timber_hearth_places)
            + self.planet_walk_objective("(Timber Hearth)", self.timber_hearth_places)
            + self.planet_picture_objective("(Attlerock)", self.attlerock_places)
            + self.planet_walk_objective("(Attlerock)", self.attlerock_places)
            + self.planet_picture_objective("(Brittle Hollow)", self.brittle_hollow_places)
            + self.planet_walk_objective("(Brittle Hollow)", self.brittle_hollow_places)
            + self.planet_picture_objective("(Dark Bramble)", self.dark_bramble_places)
            + self.planet_walk_objective("(Dark Bramble)", self.dark_bramble_places)
            + self.planet_picture_objective("(Giant's Deep)", self.giants_deep_places)
            + self.planet_walk_objective("(Giant's Deep)", self.giants_deep_places)
            + self.planet_picture_objective("(Ember Twin)", self.ember_twin_places)
            + self.planet_walk_objective("(Ember Twin)", self.ember_twin_places)
            + self.planet_picture_objective("(Ash Twin)", self.ash_twin_places)
            + self.planet_walk_objective("(Ash Twin)", self.ash_twin_places)
            + self.planet_picture_objective("(Interloper)", self.interloper_places)
            + self.planet_walk_objective("(Interloper)", self.interloper_places)
            + self.planet_picture_objective("(Quantum Moon)", self.quantum_moon_places)
            + self.planet_walk_objective("(Quantum Moon)", self.quantum_moon_places)
            + self.planet_picture_objective("", self.other_places)
        )

    def planet_picture_objective(planet_name, places) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label=f"Take a picture of/from PLACE {planet_name}",
                data={
                    "PLACE": (places, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1
            ),
        ]
    
    def planet_walk_objective(planet_name, places) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label=f"Walk between these two places: PLACES {planet_name}",
                data={
                    "PLACES": (places, 2),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=1
            )
        ]
    
    @property
    def randophilia_nono_is_here(self) -> bool:
        return self.archipelago_options.randophilia_nono_is_here.value
    
    @staticmethod
    def characters() -> List[str]:
        return [
            # Travelers
            "Chert (Chail)",
            "Esker",
            "Feldspar (Feldspath)",
            "Gabbro",
            "Riebeck",
            # Friends
            "Solanum",
            "The Prisoner (le Prisonnier)",
            # Hearthians
            "Arkose",
            "Galena (Galène)",
            "Gneiss",
            "Gossan",
            "Hal",
            "Hornfels (Cornée)",
            "Marl (Marn)",
            "Mica",
            "Moraine",
            "Porphy (Porph)",
            "Rutile",
            "Slate (Ardoise)",
            "Spinel (Spinelle)",
            "Tektite (Tectite)",
            "Tephra",
            "Tuff (Tuf)",
        ]
    
    @staticmethod
    def endings() -> List[str]:
        return [
            "Eye of the Universe",
            "You are dead",
            "Isolation",
            "Quantum Moon",
            "Broken Space and Time",
            "Meet Yourself",
        ]
    
    @staticmethod
    def timber_hearth_places() -> List[str]:
        return [
            # in the village
            "Launch Tower",
            "Observatory",
            "Slate's Campfire",
            "Fenced-Off Ghost Matter",
            "Geyser Cave",
            "Mica's Model Ship Station",
            "Scout Launcher Platform",
            "Zero-G Cave"
            # outside the village
            "Geyser Moutain",
            "Nomai Ruins",
            "First Encounter Mural",
            "Mining Site 2b",
            "Backers Graveyard",
            "Quantum Grove Crater",
            "Bramble Seed Crater",
            "Radio Tower",
            "Radio Tower Campfire",
        ]
    
    @staticmethod
    def attlerock_places() -> List[str]:
        return [
            "Lunar Outpost",
            "Lunar Lookout",
            "Eye Signal Locator",
            "Chert's Recorder",
        ]
    
    @staticmethod
    def brittle_hollow_places() -> List[str]:
        return [
            "Northern Glacier",
            "Hanging City's Forge Button",
            "Hanging City's School",
            "Hanging City's Eye Shrine",
            "Gravity Crystal Worhshop",
            "Crossroads",
            "Gravity Cannon",
            "Escape Pod 1",
            "Old Settlement",
            "Gravity Crystal Highway",
            "Under the Tower of Quantum Knowledge",
            "Above the Tower of Quantum Knowledge",
            "Inside the Southern Laboratory",
            "Riebeck's Ship",
        ]
    
    @staticmethod
    def dark_bramble_places() -> List[str]:
        return [
            "Dead Jellyfish",
            "Escape Pod 3",
            "Nomai Grave",
            "Feldspar's Campfire",
            "Feldspar's Ship",
            "Eggs Nest",
            "The Vessel",
        ]

    @staticmethod
    def giants_deep_places() -> List[str]:
        return [
            "Gabbro's Ship",
            "Bramble Island",
            "Feldspar's Campfire",
            "Gabbro's Hamac",
            "Gabbro's Campfire",
            "Cannon Construction Site",
            "Statue Island Village Ruins",
            "Statue Workshop",
            "Ocean Depths",
            "Planet's Core",
            "Orbital Probe Cannon's Tracking Module",
        ]
    
    @staticmethod
    def ember_twin_places() -> List[str]:
        return [
            "Escape Pod 2",
            "Sunless City's Anglerfish Overlook",
            "Sunless City's Anglerfish Fossil",
            "Sunless City's Bottom",
            "Sunless City's Eye Shrine",
            "High Energy Lab",
            "Gravity Cannon",
            "Chert's Campfire",
            "Quantum Cave",
            "Lakebed Cave",
            "Quantum Moon Locator",
        ]
    
    @staticmethod
    def ash_twin_places() -> List[str]:
        return [
            "Inside the Sun Station Tower",
            "Outside the Sun Station Tower",
            "Brittle Hollow Tower",
            "Giant's Deep Tower",
            "Timber Hearth Tower",
            "Hourglass Twins Tower",
            "Ash Twin Project",
        ]
    
    @staticmethod
    def interloper_places() -> List[str]:
        return [
            "Frozen Side",
            "Sunny Side",
            "Frozen Nomai Shuttle",
            "Ruptured Core",
        ]
    
    @staticmethod
    def quantum_moon_places() -> List[str]:
        return [
            "Hourglass Twins Ambiance",
            "Timber Hearth Ambiance",
            "Brittle Hollow Ambiance",
            "Giant's Deep Ambiance",
            "Dark Bramble Ambiance",
            "Eye of the Universe Ambiance",
            "North Pole",
            "Dead Solanum",
            "Living Solanum",
            "Quantum Shrine",
            "Solanum's Ship",
        ]
    
    @staticmethod
    def other_places() -> List[str]:
        return [
            "Inside the Lantern",
            "Black Hole Forge",
            "Sun Station",
            "The Eye of the Universe",
            "Orbital Probe Cannon's Control Module",
            "Orbital Probe Cannon's Launch Module",
            "Tower of Quantum Trials",
            "White Hole",
            "White Hole Station",
            "Deep Space Satellite",
            "Nomai Probe",
        ]