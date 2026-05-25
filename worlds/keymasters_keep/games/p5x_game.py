from __future__ import annotations

import functools
from dataclasses import dataclass
from typing import Dict, List, Set, Tuple

from Options import OptionSet, Range, Toggle

from ..enums import KeymastersKeepGamePlatforms
from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

OBJECTIVE_TECHNICIAN = "Technician"
OBJECTIVE_OTHER_VELVET_TRIAL = "Other Velvet Trial"
OBJECTIVE_METRO_OF_DESIRE = "Metro of Desire"
OBJECTIVE_RECOLLECTION_BOSS = "Recollection Boss"

DIFFICULTY_EASY = "Easy"
DIFFICULTY_MEDIUM = "Medium"
DIFFICULTY_HARD = "Hard"

CONSTRAINT_NONE = "None"
CONSTRAINT_THREE_STARS = "3 Stars"
CONSTRAINT_ROLE_EXCLUSION = "Role Exclusion"
CONSTRAINT_ELEMENT_TEAM = "Element Team"
CONSTRAINT_TEAM_SIZE = "Team Size"

TemplateData = Dict[str, Tuple[List[str], int]]


class OptionIncludedBaseObjectives(OptionSet):
    """
    Indicates which base objectives can be used when generating templates.
    """

    display_name = "Included Base Objectives"
    valid_keys = [
        OBJECTIVE_TECHNICIAN,
        OBJECTIVE_OTHER_VELVET_TRIAL,
        OBJECTIVE_METRO_OF_DESIRE,
        OBJECTIVE_RECOLLECTION_BOSS,
    ]
    default = set(valid_keys)


class OptionIncludedDifficulties(OptionSet):
    """
    Indicates which objective difficulties can be used when generating templates.
    Affects Velvet Trials objectives.
    Technician: Easy: 1-15, Medium: 16-30, Hard: 31-40
    Other Velvet Trial: Easy: 1-15, Medium: 16-25
    """

    display_name = "Included Difficulties"
    valid_keys = [DIFFICULTY_EASY, DIFFICULTY_MEDIUM, DIFFICULTY_HARD]
    default = set(valid_keys)


class OptionIncludedConstraints(OptionSet):
    """
    Indicates which optional constraints can be combined with eligible objectives.
    None: No added constraints
    Three Stars: Must complete objective with three stars (Only affects Velvet Trials)
    Role Exclusion: Must complete objective without specified role
    Element Team: Must complete objective using specified element team (at least two members beside Wonder)
    Team Size: Must complete objective with a limited number of characters (Wonder and Navigator included)
    (Note that removing None from the selection will remove the non-constrained objectives)
    """

    display_name = "Included Constraints"
    valid_keys = [
        CONSTRAINT_NONE,
        CONSTRAINT_THREE_STARS,
        CONSTRAINT_ROLE_EXCLUSION,
        CONSTRAINT_ELEMENT_TEAM,
        CONSTRAINT_TEAM_SIZE,
    ]
    default = set(valid_keys)


class OptionRoleExclusionIncludeDPS(Toggle):
    """
    Whether to include DPS roles in the role exclusion challenges.
    Removing DPS roles can significantly increase the difficulty of the challenges.
    DPS Roles: Assassin, Sweeper
    """

    display_name = "Include DPS Roles in Role Exclusion"


class OptionRoleExclusionIncludeNavigator(Toggle):
    """
    Whether to include the Navigator role in the role exclusion challenges.
    Along with removing their buffs, removing the Navigator also force the team to be smaller since they can't be replaced.
    Navigator Role: Navigator
    """

    display_name = "Include Navigator Role in Role Exclusion"


class OptionMaxRoleExclusionCount(Range):
    """
    The maximum number of roles that can be excluded in the role exclusion challenges. (1-5)
    Support Roles: Strategist, Saboteur, Guardian, Medic
    DPS Roles: Assassin, Sweeper
    Navigator Role: Navigator
    """

    display_name = "Max Role Exclusion Count"
    range_start = 1
    range_end = 5
    default = 1


class OptionMinTeamSizeCap(Range):
    """
    The smallest team-size cap that the Team Size constraint can randomly pick.
    The constraint limits the player's team to a maximum of X characters (Wonder and Navigator included);
    This option sets the lowest possible X. This option does not apply to Velvet Trials.
    Lower values allow harder challenges to appear; higher values keep the cap
    looser and easier.
    """

    display_name = "Minimum Team Size Cap"
    range_start = 1
    range_end = 5
    default = 1


class OptionOwnedElementTeams(OptionSet):
    """
    Indicates which element teams the player has access to and can be used for objectives that require using an element team.
    Valid keys: Fire, Ice, Electric, Wind, Bless, Curse, Psychokinesis, Nuke, Physical, Gun
    """

    display_name = "Owned Element Teams"
    valid_keys = [
        "Fire",
        "Ice",
        "Electric",
        "Wind",
        "Bless",
        "Curse",
        "Psychokinesis",
        "Nuke",
        "Physical",
        "Gun",
    ]
    default = set(valid_keys)


@dataclass
class ObjectiveVariantDefinition:
    difficulty: str | None
    label: str
    data: TemplateData
    is_time_consuming: bool
    is_difficult: bool
    weight: int


@dataclass
class ObjectiveDefinition:
    key: str
    compatible_constraints: Set[str]
    variants: List[ObjectiveVariantDefinition]


@dataclass
class ConstraintDefinition:
    key: str
    label_suffix: str
    data: TemplateData


@dataclass
class P5XArchipelagoOptions:
    included_base_objectives: OptionIncludedBaseObjectives
    included_difficulties: OptionIncludedDifficulties
    included_constraints: OptionIncludedConstraints
    role_exclusion_include_dps_roles: OptionRoleExclusionIncludeDPS
    role_exclusion_include_navigator_role: OptionRoleExclusionIncludeNavigator
    max_role_exclusion_count: OptionMaxRoleExclusionCount
    min_team_size_cap: OptionMinTeamSizeCap
    owned_element_teams: OptionOwnedElementTeams


class P5XGame(Game):
    name = "Persona 5: The Phantom X"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [KeymastersKeepGamePlatforms.AND, KeymastersKeepGamePlatforms.IOS]
    is_adult_only_or_unrated = False
    options_cls = P5XArchipelagoOptions

    @property
    def owned_element_teams(self) -> Set[str]:
        return set(self.archipelago_options.owned_element_teams.value)

    def elements(self) -> List[str]:
        return sorted(self.owned_element_teams)

    @property
    def included_base_objectives(self) -> Set[str]:
        return set(self.archipelago_options.included_base_objectives.value)

    @property
    def included_difficulties(self) -> Set[str]:
        return set(self.archipelago_options.included_difficulties.value)

    @staticmethod
    def easy_technician_levels() -> List[str]:
        return [str(i) for i in range(1, 16)]

    @staticmethod
    def medium_technician_levels() -> List[str]:
        return [str(i) for i in range(16, 31)]

    @staticmethod
    def hard_technician_levels() -> List[str]:
        return [str(i) for i in range(31, 41)]

    @staticmethod
    def othervelvet_trials() -> List[str]:
        return [
            "Lair of Arcane Flame",
            "Nuclear Winter",
            "Thunderous Blessing",
            "An Ill Wind",
        ]

    @staticmethod
    def easy_other_velvet_trials_levels() -> List[str]:
        return [str(i) for i in range(1, 16)]

    @staticmethod
    def medium_other_velvet_trials_levels() -> List[str]:
        return [str(i) for i in range(16, 26)]

    @functools.cached_property
    def support_roles(self) -> List[str]:
        return ["Stategist", "Saboteur", "Guardian", "Medic"]

    @functools.cached_property
    def dps_roles(self) -> List[str]:
        return ["Assassin", "Sweeper"]

    @functools.cached_property
    def navigator_roles(self) -> List[str]:
        return ["Navigator"]

    @property
    def include_dps_roles_in_role_exclusion(self) -> bool:
        return bool(self.archipelago_options.role_exclusion_include_dps_roles.value)

    @property
    def include_navigator_role_in_role_exclusion(self) -> bool:
        return bool(
            self.archipelago_options.role_exclusion_include_navigator_role.value
        )

    def roles_for_role_exclusion(self) -> List[str]:
        roles = List(self.support_roles)
        if self.include_dps_roles_in_role_exclusion:
            roles.extend(self.dps_roles)
        if self.include_navigator_role_in_role_exclusion:
            roles.extend(self.navigator_roles)
        return roles

    @staticmethod
    def metro_of_desire_lines() -> List[str]:
        return ["Dream", "Hope", "Wish"]

    @staticmethod
    def metro_of_desire_terminal_stations() -> List[str]:
        return [str(i) for i in range(1, 5)]

    @staticmethod
    def recollection_bosses() -> List[str]:
        return [
            "Shadow of Kiuchi",
            "Shadow of Miyazawa",
            "Shadow of Katayama",
            "Shadow of Akachi",
        ]

    @property
    def included_constraints(self) -> Set[str]:
        constraints = set(self.archipelago_options.included_constraints.value)
        if len(self.elements()) == 0:
            constraints.discard(CONSTRAINT_ELEMENT_TEAM)
        return constraints

    @property
    def max_role_exclusion_count(self) -> int:
        return int(self.archipelago_options.max_role_exclusion_count.value)

    @property
    def min_team_size_cap(self) -> int:
        return int(self.archipelago_options.min_team_size_cap.value)

    def team_sizes(self) -> List[str]:
        return [str(i) for i in range(self.min_team_size_cap, 6)]

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return List()

    def objective_definitions(self) -> List[ObjectiveDefinition]:
        standard_constraints = {
            CONSTRAINT_NONE,
            CONSTRAINT_ROLE_EXCLUSION,
            CONSTRAINT_ELEMENT_TEAM,
            CONSTRAINT_TEAM_SIZE,
        }
        velvet_constraints = {
            CONSTRAINT_NONE,
            CONSTRAINT_THREE_STARS,
            CONSTRAINT_ROLE_EXCLUSION,
            CONSTRAINT_ELEMENT_TEAM,
        }

        return [
            ObjectiveDefinition(
                key=OBJECTIVE_TECHNICIAN,
                compatible_constraints=velvet_constraints,
                variants=[
                    ObjectiveVariantDefinition(
                        difficulty=DIFFICULTY_EASY,
                        label="Beat Technician EASY_TECHNICIAN_LEVEL",
                        data={
                            "EASY_TECHNICIAN_LEVEL": (self.easy_technician_levels(), 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=15,
                    ),
                    ObjectiveVariantDefinition(
                        difficulty=DIFFICULTY_MEDIUM,
                        label="Beat Technician MEDIUM_TECHNICIAN_LEVEL",
                        data={
                            "MEDIUM_TECHNICIAN_LEVEL": (
                                self.medium_technician_levels(),
                                1,
                            ),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=15,
                    ),
                    ObjectiveVariantDefinition(
                        difficulty=DIFFICULTY_HARD,
                        label="Beat Technician HARD_TECHNICIAN_LEVEL",
                        data={
                            "HARD_TECHNICIAN_LEVEL": (self.hard_technician_levels(), 1),
                        },
                        is_time_consuming=False,
                        is_difficult=True,
                        weight=10,
                    ),
                ],
            ),
            ObjectiveDefinition(
                key=OBJECTIVE_OTHER_VELVET_TRIAL,
                compatible_constraints=velvet_constraints,
                variants=[
                    ObjectiveVariantDefinition(
                        difficulty=DIFFICULTY_EASY,
                        label="Beat OTHER_VELVET_TRIAL OVT_EASY_LEVEL",
                        data={
                            "OTHER_VELVET_TRIAL": (self.othervelvet_trials(), 1),
                            "OVT_EASY_LEVEL": (
                                self.easy_other_velvet_trials_levels(),
                                1,
                            ),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=15,
                    ),
                    ObjectiveVariantDefinition(
                        difficulty=DIFFICULTY_MEDIUM,
                        label="Beat OTHER_VELVET_TRIAL OVT_MEDIUM_LEVEL",
                        data={
                            "OTHER_VELVET_TRIAL": (self.othervelvet_trials(), 1),
                            "OVT_MEDIUM_LEVEL": (
                                self.medium_other_velvet_trials_levels(),
                                1,
                            ),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=10,
                    ),
                ],
            ),
            ObjectiveDefinition(
                key=OBJECTIVE_METRO_OF_DESIRE,
                compatible_constraints=standard_constraints,
                variants=[
                    ObjectiveVariantDefinition(
                        difficulty=None,
                        label="Beat Metro of Desire MOD_LINE line station MOD_STATION",
                        data={
                            "MOD_LINE": (self.metro_of_desire_lines(), 1),
                            "MOD_STATION": (
                                self.metro_of_desire_terminal_stations(),
                                1,
                            ),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=5,
                    ),
                ],
            ),
            ObjectiveDefinition(
                key=OBJECTIVE_RECOLLECTION_BOSS,
                compatible_constraints=standard_constraints,
                variants=[
                    ObjectiveVariantDefinition(
                        difficulty=None,
                        label="Beat RECOLLECTION_BOSS",
                        data={
                            "RECOLLECTION_BOSS": (self.recollection_bosses(), 1),
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=5,
                    ),
                ],
            ),
        ]

    def constraint_definitions(self) -> List[ConstraintDefinition]:
        return [
            ConstraintDefinition(
                key=CONSTRAINT_NONE,
                label_suffix="",
                data={},
            ),
            ConstraintDefinition(
                key=CONSTRAINT_THREE_STARS,
                label_suffix=" with 3 stars",
                data={},
            ),
            ConstraintDefinition(
                key=CONSTRAINT_ROLE_EXCLUSION,
                label_suffix=" without using any ROLE character or persona",
                data={
                    "ROLE": (
                        self.roles_for_role_exclusion(),
                        self.max_role_exclusion_count,
                    ),
                },
            ),
            ConstraintDefinition(
                key=CONSTRAINT_ELEMENT_TEAM,
                label_suffix=" with a ELEMENT team (at least 2 members beside Wonder)",
                data={
                    "ELEMENT": (self.elements(), 1),
                },
            ),
            ConstraintDefinition(
                key=CONSTRAINT_TEAM_SIZE,
                label_suffix=" with a TEAM_SIZE-characters team (Wonder and Navigator included)",
                data={
                    "TEAM_SIZE": (self.team_sizes(), 1),
                },
            ),
        ]

    @staticmethod
    def compose_objective_template(
        objective_variant: ObjectiveVariantDefinition,
        constraint: ConstraintDefinition,
    ) -> GameObjectiveTemplate:
        data = dict(objective_variant.data)
        data.update(constraint.data)
        return GameObjectiveTemplate(
            label=f"{objective_variant.label}{constraint.label_suffix}",
            data=data,
            is_time_consuming=objective_variant.is_time_consuming,
            is_difficult=objective_variant.is_difficult,
            weight=objective_variant.weight,
        )

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        included_base_objectives = self.included_base_objectives
        included_difficulties = self.included_difficulties
        included_constraints = self.included_constraints
        constraint_definitions = self.constraint_definitions()
        templates: List[GameObjectiveTemplate] = []

        for objective in self.objective_definitions():
            if objective.key not in included_base_objectives:
                continue

            for variant in objective.variants:
                if (
                    variant.difficulty is not None
                    and variant.difficulty not in included_difficulties
                ):
                    continue

                for constraint in constraint_definitions:
                    if constraint.key not in included_constraints:
                        continue
                    if constraint.key not in objective.compatible_constraints:
                        continue
                    templates.append(
                        self.compose_objective_template(variant, constraint)
                    )

        return templates
