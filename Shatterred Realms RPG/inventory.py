# inventory.py


def show_inventory(player):

    print("\n🎒 INVENTORY")
    print("══════════════")

    if not player.inventory:

        print("Inventory Empty")

        return

    for index, item in enumerate(
            player.inventory,
            start=1):

        print(
            f"{index}. {item}"
        )


def use_item(player):

    if not player.inventory:

        print(
            "\n❌ No items available."
        )

        return

    print("\n🎒 USE ITEM")
    print("══════════════")

    for index, item in enumerate(
            player.inventory,
            start=1):

        print(
            f"{index}. {item}"
        )

    print("0. Cancel")

    choice = input(
        "\nSelect Item: "
    )

    if choice == "0":

        return

    if not choice.isdigit():

        return

    choice = int(choice)

    if (
        choice < 1
        or
        choice > len(
            player.inventory
        )
    ):

        return

    item = player.inventory[
        choice - 1
    ]

    if item == "Potion":

        heal = 30

        player.hp = min(
            player.max_hp,
            player.hp + heal
        )

        player.inventory.remove(
            item
        )

        print(
            f"\n💚 Restored "
            f"{heal} HP"
        )

    elif item == "Mega Potion":

        heal = 75

        player.hp = min(
            player.max_hp,
            player.hp + heal
        )

        player.inventory.remove(
            item
        )

        print(
            f"\n💚 Restored "
            f"{heal} HP"
        )

    elif item == "Elixir":

        player.hp = (
            player.max_hp
        )

        player.inventory.remove(
            item
        )

        print(
            "\n✨ Fully Restored!"
        )