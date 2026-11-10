class Player:

    def __init__(self, data):

        self.username = data["username"]

        self.level = data.get(
            "level",
            1
        )

        self.xp = data.get(
            "xp",
            0
        )

        self.hp = data.get(
            "hp",
            100
        )

        self.max_hp = data.get(
            "max_hp",
            100
        )

        self.gold = data.get(
            "gold",
            50
        )

        self.inventory = data.get(
            "inventory",
            ["Potion"]
        )

        self.skills = data.get(
            "skills",
            ["Strike"]
        )

        self.position = data.get(
            "position",
            [2, 13]
        )

        self.current_map = data.get(
            "current_map",
            "town"
        )

        self.quest_step = data.get(
            "quest_step",
            0
        )

        self.monster_kills = data.get(
            "monster_kills",
            0
        )

        self.chests_opened = data.get(
            "chests_opened",
            0
        )

        self.cooldowns = {}

        self.unlock_skills()

    def gain_gold(
            self,
            amount):

        self.gold += amount

    def gain_xp(
            self,
            amount):

        self.xp += amount

        while self.xp >= (
            self.level * 100
        ):

            self.xp -= (
                self.level * 100
            )

            self.level += 1

            self.max_hp += 20

            self.hp = self.max_hp

            print(
                f"\n🌟 LEVEL UP!"
            )

            print(
                f"You reached Level "
                f"{self.level}"
            )

            self.unlock_skills()

    def unlock_skills(self):

        if (
            self.level >= 3
            and
            "Fireball"
            not in self.skills
        ):

            self.skills.append(
                "Fireball"
            )

            print(
                "\n🔥 Learned Fireball!"
            )

        if (
            self.level >= 5
            and
            "Heal"
            not in self.skills
        ):

            self.skills.append(
                "Heal"
            )

            print(
                "\n💚 Learned Heal!"
            )

        if (
            self.level >= 8
            and
            "Blizzard"
            not in self.skills
        ):

            self.skills.append(
                "Blizzard"
            )

            print(
                "\n❄️ Learned Blizzard!"
            )

    def hp_bar(self):

        current = max(
            0,
            self.hp
        )

        filled = int(
            (current /
             self.max_hp)
            * 10
        )

        empty = 10 - filled

        return (
            "🟥" * filled
            +
            "⬜" * empty
        )

    def show_stats(self):

        print()

        print(
            "════════════════════"
        )

        print(
            f"🧙 {self.username}"
        )

        print(
            f"⭐ Level: "
            f"{self.level}"
        )

        print(
            f"❤️ {self.hp}/"
            f"{self.max_hp}"
        )

        print(
            self.hp_bar()
        )

        print(
            f"✨ XP: "
            f"{self.xp}"
        )

        print(
            f"💰 Gold: "
            f"{self.gold}"
        )

        print(
            f"👹 Kills: "
            f"{self.monster_kills}"
        )

        print(
            f"📦 Chests: "
            f"{self.chests_opened}"
        )

        print("\n📜 Skills")

        for skill in self.skills:

            cooldown = ""

            if skill in self.cooldowns:

                cooldown = (
                    f" (CD "
                    f"{self.cooldowns[skill]})"
                )

            print(
                f" • {skill}"
                f"{cooldown}"
            )

        print(
            "════════════════════"
        )