def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']} z miejscowości: {user['location']}, opublikował {user['posts']} postów ")

def add_user(users_data: list) -> None:
    new_name = input('Podaj imię nowego użytkownika: ')
    new_location = input('Podaj lokalizację nowego użytkownika: ')
    new_posts = int(input('Podaj liczbę postów nowego użytkownika: '))
    users_data.append({'name': new_name , 'location': new_location, 'posts': new_posts})

def remove_user(users_data: list) -> None:
    użytkownik_do_usunięcia = input('Podaj użytkownika do usunięcia: ')

    for user in users_data:

        if user['name'] == użytkownik_do_usunięcia:
            users_data.remove(user)

