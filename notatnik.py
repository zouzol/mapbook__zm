users = [
    {"name": "Beata", "location": "Lublin", "posts": 555},
]
def update_user(users_data: list) -> None:

    użytkownik_do_edycji = input('Podaj użytkownika do edycji: ')
    for user in users_data:
        if user['name'] == użytkownik_do_edycji:
            user["name"]=input("Podaj nowe imie uzytkownika: ")
            user["location"]=input("Podaj nowa lokalizacje uzytkownika: ")
            user["posts"]=int(input("Podaj nowa liczbe postow: "))


update_user(users)

print(users)
