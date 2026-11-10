# monster.py


class Monster:

    def __init__(
            self,
            icon,
            name,
            hp,
            attack,
            xp,
            gold):

        self.icon = icon
        self.name = name

        self.hp = hp
        self.attack = attack

        self.xp = xp
        self.gold = gold

    def is_alive(self):

        return self.hp > 0


class Goblin(Monster):

    def __init__(self):

        super().__init__(
            "👹",
            "Goblin",
            30,
            5,
            25,
            15
        )


class Wolf(Monster):

    def __init__(self):

        super().__init__(
            "🐺",
            "Wolf",
            45,
            8,
            40,
            20
        )


class Skeleton(Monster):

    def __init__(self):

        super().__init__(
            "💀",
            "Skeleton",
            65,
            11,
            60,
            30
        )


class Orc(Monster):

    def __init__(self):

        super().__init__(
            "👺",
            "Orc",
            95,
            15,
            90,
            50
        )


class ShadowKing(Monster):

    def __init__(self):

        super().__init__(
            "👑",
            "Shadow King",
            500,
            25,
            1000,
            500
        )