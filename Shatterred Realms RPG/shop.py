# shop.py

from items import (
    SHOP_ITEMS
)


def shop_menu(player):

    while True:

        print("\n🛒 LUNA'S SHOP")
        print("══════════════")

        names = list(
            SHOP_ITEMS.keys()
        )

        for index, item in enumerate(
                names,
                start=1):

            print(
                f"{index}. "
                f"{item}"
                f" - "
                f"{SHOP_ITEMS[item]}💰"
            )

        print(
            "\n0. Leave Shop"
        )

        print(
            f"\n💰 Gold: "
            f"{player.gold}"
        )

        choice = input(
            "\n> "
        )

        if choice == "0":

            break

        if not choice.isdigit():

            continue

        choice = int(choice)

        if (
            choice < 1
            or
            choice > len(names)
        ):

            continue

        item = names[
            choice - 1
        ]

        cost = SHOP_ITEMS[
            item
        ]

        if player.gold < cost:

            print(
                "\n❌ Not enough gold!"
            )

            continue

        player.gold -= cost

        player.inventory.append(
            item
        )

        print(
            f"\n✅ Purchased "
            f"{item}"
        )