from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class PlateUpArchipelagoOptions:
    pass

class PlateUpGame(Game):
    name = "PlateUp!"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = None
    is_adult_only_or_unrated = False
    options_cls = PlateUpArchipelagoOptions


    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []
        constraints.extend([
            GameObjectiveTemplate(
                label="Cook: PLAYER / Game mode: MODE / Swap: ONOFF / Card mode: MASTER",
                data={
                    "PLAYER": (self.players, 1),
                    "MODE": (self.gamemode, 1),
                    "ONOFF": (self.on_off, 1),
                    "MASTER": (self.master, 1),
                    },
                weight=25, # magic number
            ),
            GameObjectiveTemplate(
                label="Play on one of your franchise.",
                data={},
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Always buy or upgrade APPLIANCE when it appears",
                data={
                    "APPLIANCE": (self.appliances, 1)
                },
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Bring some COLORS in your restaurant (through decoration or clothes).",
                data={
                    "COLORS": (self.colors, 2)
                    },
                weight=sum(o.weight for o in constraints)
            ),

        ])
        return constraints

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        if self.randophilia_noni_is_here:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Reach Day DAYNUMBER with one of these starting dishes: PLATES",
                    data={
                        "DAYNUMBER": (self.day_number, 1),
                        "PLATES": (self.plates, 2),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Reach Day DAYNUMBER on a SIZE room",
                    data={
                        "DAYNUMBER": (self.day_number, 1),
                        "SIZE": (self.room_size, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Play with this restaurant setting : SETTINGS",
                    data={
                        "SETTINGS": (self.settings, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Play the daily run",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        return game_objective_templates

    @property
    def randophilia_noni_is_here(self) -> bool:
        return self.archipelago_options.randophilia_nono_is_here.value and self.archipelago_options.randophilia_niko_is_here.value
    
    @staticmethod
    def plates() -> List[str]:
        return [
            "Black Coffe",
            "Breakfast",
            "Burgers",
            "Cakes",
            "Dumplings",
            "Fish",
            "Hot Dogs",
            "Pies",
            "Pizza",
            "Salad",
            "Sandwich",
            "Spaghetti",
            "Steak",
            "Stir Fry",
            "Sundaes",
            "Tacos",
            "Turkey",
        ]
    
    @staticmethod
    def themes() -> List[str]:
        return [
            "Affordable",
            "Charming",
            "Exclusive",
            "Formal",
        ]
    @staticmethod
    def colors() -> List[str]:
        return [
            "Blue",
            "Green",
            "Red",
            "Orange",
            "Brown",
        ]
    @staticmethod
    def settings() -> List[str]:
        return [
            "City",
            "Country",
            "Alpine",
            "Community",
            "Turbo",
            "Witch Hut",
            "North Pole",
        ]
    @staticmethod
    def room_size() -> List[str]:
        return [
            "Small",
            "Medium",
            "Big",
        ]
    
    @staticmethod
    def appliances() -> List[str]:
        return [
            "Research Desk",
            "Counter",
            "Hob",
            "Dining Table",
            "Bin",
            "Sink",
            "Conveyor",
            "Mixer",
            "Mop",
            "Poritoner",
        ]
    
    @staticmethod
    def day_number() -> List[int]:
        return list(range(4, 12))
    # MASTER MODE:
    #   - Recipe Master : Always pick food card.
    #   - Service Master : Never pick food card.
    @staticmethod
    def master() -> List[str]:
        return [
            "Recipe Master",
            "Service Master",
        ]
    
    # GAME MODE:
    #   - Libre : Comme on veut.
    #   - Strict : Chaque joueur ne peux pas allez dans la zone de l'uatre joueur.
    #   - Swap : Les joueurs échange leur zone a chaque tier de run (Jour 5, jour des décors)
    @staticmethod
    def gamemode() -> List[str]:
        return [
            "Libre",
            "Strict",
        ]
    @staticmethod
    def players() -> List[str]:
        return [
            "Nono",
            "Niko",
            "Free"
        ]
    @staticmethod
    def on_off() -> List[str]:
        return [
            "On",
            "Off",
        ]
    