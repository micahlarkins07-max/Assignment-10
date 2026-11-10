# victory.py


def victory_screen(player):

    print("\n" * 2)

    print("🎉" * 20)

    print()

    print(
        "🏆 HERO OF THE REALMS 🏆"
    )

    print()

    print(
        "👑 The Shadow King has fallen!"
    )

    print()

    print(
        "🌍 Peace has returned to Eldoria."
    )

    print()

    print(
        f"🧙 Hero: "
        f"{player.username}"
    )

    print(
        f"⭐ Final Level: "
        f"{player.level}"
    )

    print(
        f"💰 Gold: "
        f"{player.gold}"
    )

    print(
        f"👹 Monsters Defeated: "
        f"{player.monster_kills}"
    )

    print(
        f"📦 Chests Opened: "
        f"{player.chests_opened}"
    )

    print()

    print("🎉" * 20)

    input(
        "\nPress ENTER..."
    )