from __future__ import annotations
from dataclasses import dataclass

from Options import Toggle
from ..game import Game
from ..enums import KeymastersKeepGamePlatforms

@dataclass
class RandophiliaServerArchipelagoOptions:
    randophilia_niko_is_here: RandophiliaNikoIsHereOption
    randophilia_nono_is_here: RandophiliaNonoIsHereOption



class RandophiliaNikoIsHereOption(Toggle):
    """Include everything Niko can face in the Keep."""
    display_name = "Randophilia - Niko is Here"
    default = False

class RandophiliaNonoIsHereOption(Toggle):
    """Include everything Nono can face in the Keep."""
    display_name = "Randophilia - Nono is Here"
    default = False



class RandophiliaServerKeepGame(Game):
    name = "Randophilia Server"
    platform = KeymastersKeepGamePlatforms.META
    platforms_other = None
    is_adult_only_or_unrated = False
    should_autoregister = False
    options_cls = RandophiliaServerArchipelagoOptions