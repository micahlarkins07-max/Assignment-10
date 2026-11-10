# game.py

import copy
import random

from maps import MAPS

from combat import battle

from inventory import (
    show_inventory,
    use_item
)

from quest import (
    show_main_quest,
    show_side_quests,
    check_side_quests,
    update_main_quest
)

from map_manager import (
    display_map,
    move_player
)

from database import (
    save_player
)

from victory import (
    victory_screen
)


WEATHER_TYPES = [

    "☀️ Clear",

    "🌧️ Rain",

    "❄️ Blizzard",

    "🌑 Eclipse"
]


def generate_weather():

    return random.choice(
        WEATHER_TYPES
    )


def load_map(player):

    world = copy.deepcopy(
        MAPS[
            player.current_map
        ]
    )

    x = player.position[0]
    y = player.position[1]

    world[y][x] = "🧙"

    return world


def show_controls():

    print()

    print("🎮 CONTROLS")
    print("════════════════════")

    print("W = Up")
    print("A = Left")
    print("S = Down")
    print("D = Right")

    print()

    print("C = Character")
    print("I = Inventory")
    print("Q = Main Quest")
    print("J = Side Quests")

    print("X = Save & Exit")

    print("════════════════════")


def handle_death(player):

    print(
        "\n☠️ You were defeated!"
    )

    print(
        "✨ The town healer restored you."
    )

    player.hp = player.max_hp

    player.current_map = "town"

    player.position = [
        2,
        13
    ]


def start_game(player):

    weather = generate_weather()

    world = load_map(
        player
    )

    player_x = player.position[0]
    player_y = player.position[1]

    while True:

        print("\n" * 2)

        print(
            "════════════════════════"
        )

        print(
            "🌑 SHATTERED REALMS 🌑"
        )

        print(
            f"🌦️ Weather: {weather}"
        )

        print(
            "════════════════════════"
        )

        display_map(
            world
        )

        show_controls()

        choice = input(
            "\n> "
        ).lower().strip()

        # ==================
        # CHARACTER
        # ==================

        if choice == "c":

            player.show_stats()

            input(
                "\nPress ENTER..."
            )

            continue

        # ==================
        # INVENTORY
        # ==================

        elif choice == "i":

            show_inventory(
                player
            )

            use_item(
                player
            )

            continue

        # ==================
        # MAIN QUEST
        # ==================

        elif choice == "q":

            show_main_quest(
                player
            )

            input(
                "\nPress ENTER..."
            )

            continue

        # ==================
        # SIDE QUESTS
        # ==================

        elif choice == "j":

            show_side_quests()

            input(
                "\nPress ENTER..."
            )

            continue

        # ==================
        # SAVE
        # ==================

        elif choice == "x":

            player.position = [
                player_x,
                player_y
            ]

            save_player(
                player
            )

            print(
                "\n✅ Game Saved!"
            )

            break

        # ==================
        # MOVEMENT
        # ==================

        elif choice in [
            "w",
            "a",
            "s",
            "d"
        ]:

            result = move_player(

                player,

                world,

                player_x,

                player_y,

                choice
            )

            event = result[0]

            # ==================
            # NORMAL MOVE
            # ==================

            if event == "MOVE":

                player_x = result[1]
                player_y = result[2]

                player.position = [
                    player_x,
                    player_y
                ]

            # ==================
            # BATTLE
            # ==================

            elif event == "BATTLE":

                monster_tile = result[1]

                battle_result = battle(
                    player,
                    monster_tile
                )

                update_main_quest(
                    player
                )

                check_side_quests(
                    player
                )

                if battle_result == "WIN":

                    save_player(
                        player
                    )

                    victory_screen(
                        player
                    )

                    return

                if player.hp <= 0:

                    handle_death(
                        player
                    )

                    world = load_map(
                        player
                    )

                    player_x = (
                        player.position[0]
                    )

                    player_y = (
                        player.position[1]
                    )

            # ==================
            # MAP CHANGE
            # ==================

            elif event == "MAP_CHANGE":

                destination = result[1]

                spawn_x = result[2]

                spawn_y = result[3]

                player.current_map = (
                    destination
                )

                player.position = [
                    spawn_x,
                    spawn_y
                ]

                world = load_map(
                    player
                )

                player_x = spawn_x
                player_y = spawn_y

                weather = (
                    generate_weather()
                )

        # ==================
        # INVALID INPUT
        # ==================

        else:

            print(
                "\n❌ Invalid Input"
            )

            input(
                "\nPress ENTER..."
            )