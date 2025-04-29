def get_user_into(user_data: list) -> None:
    for user in users:
        print(f"Twój znajomy {user["name"]} z {user["location"]} opublikował {user["posts"]} postów.")


def add_user(users_data: list) -> None:
    new_name = input("Podaj imię nowego użytkownika: ")
    new_location = input("Podaj lokalizacje nowego użytkownika: ")
    new_posts = int(input("Podaj liczbę postów nowego urzytkownika: "))
    users_data.append({"name": new_name, "location": new_location, "posts": new_posts})
