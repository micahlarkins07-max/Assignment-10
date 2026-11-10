from database import (
    create_account,
    validate_login,
    user_exists
)


def register():

    print("\n📝 REGISTER")

    username = input(
        "Username: "
    ).strip()

    if not username:

        print(
            "\n❌ Username required."
        )

        return None

    if user_exists(username):

        print(
            "\n❌ Username already exists."
        )

        return None

    password = input(
        "Password: "
    ).strip()

    if not password:

        print(
            "\n❌ Password required."
        )

        return None

    create_account(
        username,
        password
    )

    print(
        "\n✅ Account Created!"
    )

    return username


def login():

    print("\n🔑 LOGIN")

    username = input(
        "Username: "
    ).strip()

    password = input(
        "Password: "
    ).strip()

    if validate_login(
            username,
            password):

        print(
            f"\n✅ Welcome "
            f"back, {username}!"
        )

        return username

    print(
        "\n❌ Invalid login."
    )

    return None