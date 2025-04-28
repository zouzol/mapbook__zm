from utils.model import users
from utils.controller import get_user_into, add_user

def main():
    print(f"Witaj {users[0]["name"]}")

    while True:
        print("============MENU============")
        print("0 - zamknij aplikacje")
        print("1 - wyświetl co u znajomych")
        print("2 - dodaj znajomego użytkownika")
        print("3 - usuń użytkownika")
        print("4 - edytuj użytkownika")
        print("============MENU============")

        choice = input("wybierz opcje menu")
        if choice == "0": break
        if choice == "1": get_user_info(users)
        if choice == "2": add_user(users)



if __name__ == "__main__":
    main()



