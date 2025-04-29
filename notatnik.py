users = [
    {"name": "Beata", "location": "Lublin", "posts": 555},
]


def remove_user(users_data: list): ->None

    uzytkownik_do_usuniecia = input("Podaj uzytkownika do usuniecia: ")

    for user in users_data:

        if user["name"] == uzytkownik_do_usuniecia:
            users_data.remove(user)

print(users)
