# combat.py

import random

from monster_factory import (
    create_monster
)

from skills import (
    Strike,
    Fireball,
    Heal,
    Blizzard
)

from quest import (
    SIDE_QUESTS
)


SKILL_OBJECTS = {

    "Strike": Strike(),

    "Fireball": Fireball(),

    "Heal": Heal(),

    "Blizzard": Blizzard()
}


def reduce_cooldowns(player):

    expired = []

    for skill in list(
            player.cooldowns.keys()):

        player.cooldowns[
            skill
        ] -= 1

        if (
            player.cooldowns[skill]
            <= 0
        ):

            expired.append(
                skill
            )

    for skill in expired:

        del player.cooldowns[
            skill
        ]


def use_skill(
        player,
        monster):

    print("\n📜 SKILLS")
    print("══════════════")

    for index, skill_name in enumerate(
            player.skills,
            start=1):

        cooldown = ""

        if (
            skill_name
            in
            player.cooldowns
        ):

            cooldown = (
                f" ⏳"
                f"{player.cooldowns[skill_name]}"
            )

        print(
            f"{index}. "
            f"{skill_name}"
            f"{cooldown}"
        )

    choice = input("\n> ")

    if not choice.isdigit():

        return False

    choice = int(choice)

    if (
        choice < 1
        or
        choice > len(
            player.skills
        )
    ):

        return False

    skill_name = player.skills[
        choice - 1
    ]

    if (
        skill_name
        in
        player.cooldowns
    ):

        print(
            "\n⏳ Skill is on cooldown!"
        )

        return False

    skill = SKILL_OBJECTS[
        skill_name
    ]

    skill.use(
        player,
        monster
    )

    if skill.cooldown > 0:

        player.cooldowns[
            skill_name
        ] = skill.cooldown

    return True


def battle(
        player,
        monster_tile):

    monster = create_monster(
        monster_tile
    )

    print(
        f"\n⚔️ "
        f"{monster.icon} "
        f"{monster.name} appears!"
    )

    while (
        player.hp > 0
        and
        monster.hp > 0
    ):

        print("\n══════════════")

        print(
            f"❤️ "
            f"{player.hp}/"
            f"{player.max_hp}"
        )

        print(
            f"{monster.icon} "
            f"{monster.name}: "
            f"{monster.hp}"
        )

        print("══════════════")

        print("\n1. Attack")
        print("2. Skill")
        print("3. Run")

        choice = input("> ")

        if choice == "1":

            damage = random.randint(
                8,
                18
            )

            if (
                random.randint(
                    1,
                    100
                ) <= 10
            ):

                damage *= 2

                print(
                    "\n💥 CRITICAL HIT!"
                )

            monster.hp -= damage

            print(
                f"\n🗡️ "
                f"{damage} damage!"
            )

        elif choice == "2":

            use_skill(
                player,
                monster
            )

        elif choice == "3":

            if (
                random.randint(
                    1,
                    100
                ) <= 50
            ):

                print(
                    "\n🏃 Escaped!"
                )

                return False

            print(
                "\n❌ Couldn't escape!"
            )
       
        else:

            continue

        if monster.hp <= 0:

            break

        enemy_damage = random.randint(

            max(
                1,
                monster.attack - 2
            ),

            monster.attack + 2
        )

        player.hp -= enemy_damage

        print(
            f"\n{monster.icon}"
            f" dealt "
            f"{enemy_damage}"
        )

        reduce_cooldowns(
            player
        )

    if player.hp <= 0:

        print(
            "\n☠️ Defeated..."
        )

        return False

    print(
        f"\n🎉 "
        f"{monster.name}"
        f" defeated!"
    )

    player.gain_xp(
        monster.xp
    )

    player.gain_gold(
        monster.gold
    )

    player.monster_kills += 1

    if monster.name == "Wolf":

        SIDE_QUESTS[
            "wolf_hunter"
        ]["progress"] += 1

    print(
        f"✨ +{monster.xp} XP"
    )

    print(
        f"💰 +{monster.gold} Gold"
    )

    if (
        monster.name ==
        "Shadow King"
    ):

        player.quest_step = 6

        print(
            "\n👑 The Shadow King has fallen!"
        )

        return "WIN"

    return True