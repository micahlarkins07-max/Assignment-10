# npc.py


NPCS = {

    "👴 Elder Rowan": {
        "role": "Quest Giver"
    },

    "🧝 Scholar Elric": {
        "role": "Scholar"
    },

    "👮 Guard Torin": {
        "role": "Guard"
    },

    "🧙 Priestess Mira": {
        "role": "Priestess"
    },

    "🛒 Merchant Luna": {
        "role": "Merchant"
    }
}


def npc_menu(player):

    while True:

        print("\n🏘️ TOWN NPCs")
        print("══════════════")

        npc_names = list(
            NPCS.keys()
        )

        for index, npc in enumerate(
                npc_names,
                start=1):

            print(
                f"{index}. {npc}"
            )

        print("0. Leave")

        choice = input("\n> ")

        if choice == "0":

            break

        if not choice.isdigit():

            continue

        choice = int(choice)

        if (
            choice < 1
            or
            choice > len(
                npc_names
            )
        ):

            continue

        npc = npc_names[
            choice - 1
        ]

        print()

        print(npc)

        if npc == "👴 Elder Rowan":

            if player.quest_step == 0:

                print(
                    "\nThe Eclipse spreads."
                )

                print(
                    "Defeat 5 monsters."
                )

                player.quest_step = 1

            elif player.quest_step == 1:

                print(
                    f"\nProgress:"
                    f" {player.monster_kills}/5"
                )

            else:

                print(
                    "\nThe realm depends on you."
                )

        elif npc == "🧝 Scholar Elric":

            print(
                "\nKnowledge is power."
            )

            if player.quest_step == 2:

                print(
                    "\n🔥 Fire Relic Acquired!"
                )

                player.quest_step = 3

        elif npc == "🧙 Priestess Mira":

            print(
                "\nMay the light guide you."
            )

            if player.quest_step == 3:

                print(
                    "\n❄️ Ice Relic Acquired!"
                )

                player.quest_step = 4

        elif npc == "👮 Guard Torin":

            print(
                "\nStay alert."
            )

            if player.quest_step == 4:

                print(
                    "\n✨ Light Relic Acquired!"
                )

                player.quest_step = 5

        elif npc == "🛒 Merchant Luna":

            print(
                "\nBusiness is good."
            )

        input(
            "\nPress ENTER..."
        )