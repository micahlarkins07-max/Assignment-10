# quest.py


MAIN_QUEST = {

    0:
    "Speak with Elder Rowan",

    1:
    "Defeat 5 Monsters",

    2:
    "Find the Fire Relic",

    3:
    "Find the Ice Relic",

    4:
    "Find the Light Relic",

    5:
    "Defeat the Shadow King",

    6:
    "🎉 The Realm Has Been Saved!"
}


SIDE_QUESTS = {

    "wolf_hunter": {

        "name":
        "🐺 Wolf Hunter",

        "goal":
        3,

        "progress":
        0,

        "completed":
        False,

        "reward_gold":
        100
    },

    "treasure_hunter": {

        "name":
        "📦 Treasure Hunter",

        "goal":
        2,

        "progress":
        0,

        "completed":
        False,

        "reward_xp":
        150
    }
}


def show_main_quest(player):

    print("\n📜 MAIN QUEST")
    print("════════════════════")

    print(
        MAIN_QUEST.get(
            player.quest_step,
            "Unknown Quest"
        )
    )


def show_side_quests():

    print("\n📖 SIDE QUESTS")
    print("════════════════════")

    for quest in SIDE_QUESTS.values():

        status = (
            "✅"
            if quest["completed"]
            else "⬜"
        )

        print(
            f"\n{status} "
            f"{quest['name']}"
        )

        print(
            f"Progress: "
            f"{quest['progress']}"
            f"/{quest['goal']}"
        )


def update_main_quest(player):

    if (
        player.quest_step == 1
        and
        player.monster_kills >= 5
    ):

        player.quest_step = 2

        print(
            "\n✅ Main Quest Updated!"
        )

        print(
            "Seek the Fire Relic."
        )


def check_side_quests(player):

    wolf_quest = SIDE_QUESTS[
        "wolf_hunter"
    ]

    if (

        not wolf_quest["completed"]

        and

        wolf_quest["progress"]
        >=
        wolf_quest["goal"]

    ):

        wolf_quest[
            "completed"
        ] = True

        player.gold += (
            wolf_quest[
                "reward_gold"
            ]
        )

        print(
            "\n🏆 SIDE QUEST COMPLETE!"
        )

        print(
            f"+{wolf_quest['reward_gold']} Gold"
        )

    treasure_quest = SIDE_QUESTS[
        "treasure_hunter"
    ]

    if (

        not treasure_quest[
            "completed"
        ]

        and

        treasure_quest[
            "progress"
        ]
        >=
        treasure_quest[
            "goal"
        ]

    ):

        treasure_quest[
            "completed"
        ] = True

        player.gain_xp(
            treasure_quest[
                "reward_xp"
            ]
        )

        print(
            "\n🏆 SIDE QUEST COMPLETE!"
        )

        print(
            f"+{treasure_quest['reward_xp']} XP"
        )