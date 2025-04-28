from untils.model import users
from untils.controller import get_user_into

def main():
    print(f"Witaj {users[0]["name"]}")
    get_user_into(users[1:])

if __name__ == "__main__":
    main()



