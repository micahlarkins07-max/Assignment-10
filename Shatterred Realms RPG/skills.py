# skills.py


class Skill:

    def __init__(
            self,
            name,
            cooldown):

        self.name = name
        self.cooldown = cooldown

    def use(
            self,
            player,
            monster):

        pass


class Strike(Skill):

    def __init__(self):

        super().__init__(
            "Strike",
            0
        )

    def use(
            self,
            player,
            monster):

        damage = 15

        monster.hp -= damage

        print(
            f"\n🗡️ Strike deals "
            f"{damage} damage!"
        )


class Fireball(Skill):

    def __init__(self):

        super().__init__(
            "Fireball",
            2
        )

    def use(
            self,
            player,
            monster):

        damage = 30

        print("\n🔥")
        print("🔥🔥")
        print("🔥🔥🔥")
        print("💥")

        monster.hp -= damage

        print(
            f"\n☄️ Fireball deals "
            f"{damage} damage!"
        )


class Heal(Skill):

    def __init__(self):

        super().__init__(
            "Heal",
            3
        )

    def use(
            self,
            player,
            monster):

        heal_amount = 25

        player.hp += heal_amount

        if player.hp > player.max_hp:

            player.hp = (
                player.max_hp
            )

        print(
            f"\n💚 Restored "
            f"{heal_amount} HP!"
        )


class Blizzard(Skill):

    def __init__(self):

        super().__init__(
            "Blizzard",
            4
        )

    def use(
            self,
            player,
            monster):

        damage = 45

        print("\n❄️")
        print("❄️❄️")
        print("❄️❄️❄️")
        print("🌨️")

        monster.hp -= damage

        print(
            f"\n❄️ Blizzard deals "
            f"{damage} damage!"
        )