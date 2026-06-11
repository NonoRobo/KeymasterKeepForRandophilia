import os

import sys
import worlds.LauncherComponents as LauncherComponents
from Utils import user_path

from .world import KeymastersKeepWorld

from NetUtils import RestrictedUnpickler

# On importe ta classe d'option
from .games.vampire_survivors import VampireSurvivorsNikoIncludeDLC

# On l'ajoute manuellement aux modules globaux autorisés par Archipelago
RestrictedUnpickler.global_safe_list.add(
    ("worlds.keymasters_keep.games.vampire_survivors", "VampireSurvivorsNikoIncludeDLC")
)

games_path: str = user_path("keymasters_keep")

if not os.path.exists(games_path):
    os.makedirs(games_path)

init_path: str = os.path.join(games_path, "__init__.py")

if not os.path.exists(init_path):
    with open(init_path, "w") as init_file:
        pass


def launch_client(*args: str) -> None:
    from .client import main
    LauncherComponents.launch_subprocess(main, name="KeymastersKeepClient", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Keymaster's Keep Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        game_name=KeymastersKeepWorld.game,
        supports_uri=True,
    )
)
