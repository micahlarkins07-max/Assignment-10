from tinydb import TinyDB, Query

db = TinyDB("accounts.json")
users = db.table("users")


def create_account(username, password):

    users.insert({

        "username": username,
        "password": password,

        "level": 1,
        "xp": 0,

        "hp": 100,
        "max_hp": 100,

        "gold": 50,

        "quest_step": 0,

        "monster_kills": 0,

        "chests_opened": 0,

        "current_map": "town",

        "position": [2, 13],

        "inventory": [
            "Potion"
        ],

        "skills": [
            "Strike"
        ]
    })


def get_account(username):

    User = Query()

    result = users.search(
        User.username == username
    )

    if result:
        return result[0]

    return None


def user_exists(username):

    User = Query()

    return len(
        users.search(
            User.username == username
        )
    ) > 0


def validate_login(
        username,
        password):

    User = Query()

    result = users.search(

        (User.username == username)

        &

        (User.password == password)
    )

    return len(result) > 0


def save_player(player):

    User = Query()

    users.update({

        "level": player.level,
        "xp": player.xp,

        "hp": player.hp,
        "max_hp": player.max_hp,

        "gold": player.gold,

        "inventory": player.inventory,

        "skills": player.skills,

        "position": player.position,

        "current_map":
        player.current_map,

        "quest_step":
        player.quest_step,

        "monster_kills":
        player.monster_kills,

        "chests_opened":
        player.chests_opened

    },
        User.username ==
        player.username
    )