# monster_factory.py

from monster import (
    Goblin,
    Wolf,
    Skeleton,
    Orc,
    ShadowKing
)


MONSTER_MAP = {

    "👹": Goblin,

    "🐺": Wolf,

    "💀": Skeleton,

    "👺": Orc,

    "👑": ShadowKing
}


def create_monster(tile):

    monster_class = MONSTER_MAP.get(
        tile
    )

    if monster_class is None:

        raise ValueError(
            f"Unknown monster tile: {tile}"
        )

    return monster_class()