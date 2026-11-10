# map_manager.py

import random

from npc import npc_menu
from shop import shop_menu

from quest import (
    SIDE_QUESTS
)


def display_map(world):

    print()

    for row in world:

        print(
            "".join(row)
        )

    print()


def move_player(
        player,
        world,
        x,
        y,
        direction):
    """
    Returns:

    ("MOVE", new_x, new_y)

    ("BATTLE", monster_tile)

    ("MAP_CHANGE",
     destination,
     spawn_x,
     spawn_y)

    ("NONE", x, y)
    """

    new_x = x
    new_y = y

    direction = direction.lower()

    # ==================
    # MOVEMENT
    # ==================

    if direction == "w":

        new_y -= 1

    elif direction == "s":

        new_y += 1

    elif direction == "a":

        new_x -= 1

    elif direction == "d":

        new_x += 1

    else:

        return (
            "NONE",
            x,
            y
        )

    # ==================
    # TILE LOOKUP
    # ==================

    try:

        tile = world[
            new_y
        ][
            new_x
        ]

    except IndexError:

        return (
            "NONE",
            x,
            y
        )

    # ==================
    # WALL
    # ==================

    if tile == "🧱":

        print(
            "\n🚫 A wall blocks your path."
        )

        return (
            "NONE",
            x,
            y
        )

    # ==================
    # NPCS
    # ==================

    elif tile in [
        "👴",
        "🧝",
        "👮"
    ]:

        npc_menu(
            player
        )

        return (
            "NONE",
            x,
            y
        )

    # ==================
    # SHOP
    # ==================

    elif tile == "🛒":

        shop_menu(
            player
        )

        return (
            "NONE",
            x,
            y
        )

    # ==================
    # CHEST
    # ==================

    elif tile == "📦":

        print(
            "\n📦 Treasure Chest Found!"
        )

        gold = random.randint(
            25,
            100
        )

        player.gold += gold

        player.chests_opened += 1

        SIDE_QUESTS[
            "treasure_hunter"
        ][
            "progress"
        ] += 1

        print(
            f"💰 +{gold} Gold"
        )

        if random.randint(
                1,
                100
        ) <= 30:

            player.inventory.append(
                "Potion"
            )

            print(
                "🧪 Found a Potion!"
            )

        world[
            new_y
        ][
            new_x
        ] = "⬜"

    # ==================
    # PORTAL
    # ==================

    elif tile == "🚪":

        if (
            player.current_map
            == "town"
        ):

            print(
                "\n🌲 Entering the Forest..."
            )

            return (

                "MAP_CHANGE",

                "forest",

                2,

                1
            )

        elif (
            player.current_map
            == "forest"
        ):

            print(
                "\n🏘️ Returning to Town..."
            )

            return (

                "MAP_CHANGE",

                "town",

                2,

                13
            )

    # ==================
    # FINAL BOSS
    # ==================

    elif tile == "👑":

        if (
            player.quest_step
            < 5
        ):

            print(
                "\n🚫 You need all three relics first!"
            )

            return (
                "NONE",
                x,
                y
            )

        return (
            "BATTLE",
            tile
        )

    # ==================
    # MONSTERS
    # ==================

    elif tile in [
        "👹",
        "🐺",
        "💀",
        "👺"
    ]:

        world[
            new_y
        ][
            new_x
        ] = "⬜"

        return (
            "BATTLE",
            tile
        )

    # ==================
    # NORMAL MOVEMENT
    # ==================

    world[y][x] = "⬜"

    world[
        new_y
    ][
        new_x
    ] = "🧙"

    return (

        "MOVE",

        new_x,

        new_y
    )