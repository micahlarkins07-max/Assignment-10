# main.py

from auth import (
    login,
    register
)

from database import (
    get_account
)

from player import (
    Player
)

from game import (
    start_game
)


def show_title():

    print()

    print(
        "════════════════════════════"
    )

    print(
        "🌑 SHATTERED REALMS 🌑"
    )

    print(
        "════════════════════════════"
    )

    print()

    print(
        "⚔️ A Terminal RPG Adventure ⚔️"
    )

    print()


def show_story():

    print()

    print(
        "════════════════════════════"
    )

    print(
        "📖 STORY"
    )

    print(
        "════════════════════════════"
    )

    print()

    print(
        "For centuries, the realm"
    )

    print(
        "of Eldoria lived in peace."
    )

    print()

    print(
        "Then came the Eclipse."
    )

    print()

    print(
        "Ancient relics vanished."
    )

    print()

    print(
        "Monsters spread across"
    )

    print(
        "the land."
    )

    print()

    print(
        "The Shadow King has"
    )

    print(
        "returned."
    )

    print()

    print(
        "You are the Realmwalker,"
    )

    print(
        "the last hero capable"
    )

    print(
        "of restoring balance."
    )

    print()

    print(
        "Find the Three Relics."
    )

    print(
        "Defeat the Shadow King."
    )

    print()

    print(
        "Good luck..."
    )

    print()

    input(
        "Press ENTER to begin..."
    )


def create_player(username):

    account = get_account(
        username
    )

    if account is None:

        print(
            "\n❌ Failed to load account."
        )

        input(
            "\nPress ENTER..."
        )

        return None

    return Player(
        account
    )


def main():

    while True:

        show_title()

        print("1. Login")
        print("2. Register")
        print("3. Exit")

        choice = input(
            "\n> "
        ).strip()

        username = None

        # ==================
        # LOGIN
        # ==================

        if choice == "1":

            username = login()

        # ==================
        # REGISTER
        # ==================

        elif choice == "2":

            username = register()

        # ==================
        # EXIT
        # ==================

        elif choice == "3":

            print(
                "\n👋 Goodbye!"
            )

            break

        # ==================
        # INVALID INPUT
        # ==================

        else:

            print(
                "\n❌ Invalid option."
            )

            input(
                "\nPress ENTER..."
            )

            continue

        # Login or register failed

        if not username:

            input(
                "\nPress ENTER..."
            )

            continue

        player = create_player(
            username
        )

        if player is None:

            continue

        # Only show story
        # for new characters

        if player.quest_step == 0:

            show_story()

        # Start game loop

        start_game(
            player
        )


if __name__ == "__main__":

    main()