def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user["name"]} z {user["location"]} opublikował {user["posts"]} postów.")


def add_user(users_data: list) -> None:
    new_name = input("Podaj imię nowego użytkownika: ")
    new_location = input("Podaj lokalizacje nowego użytkownika: ")
    new_posts = int(input("Podaj liczbę postów nowego urzytkownika: "))
    users_data.append({"name": new_name, "location": new_location, "posts": new_posts})


users = [
    {"name": "Beata", "location": "Lublin", "posts": 555},
]


def remove_user(users_data: list): ->None

uzytkownik_do_usuniecia = input("Podaj uzytkownika do usuniecia: ")

for user in users_data:

if user["name"] == uzytkownik_do_usuniecia:
    users_data.remove(user)

print(users)
