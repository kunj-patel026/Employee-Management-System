USERNAME = "admin"
PASSWORD = "admin123"


def login():

    print("\n" + "=" * 40)
    print("           ADMIN LOGIN")
    print("=" * 40)

    for attempt in range(3):

        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username == USERNAME and password == PASSWORD:
            print("\n✅ Login Successful!")
            return True

        remaining = 2 - attempt

        if remaining > 0:
            print("\n❌ Invalid Username or Password!")
            print(f"Attempts remaining: {remaining}\n")
        else:
            print("\n❌ Maximum login attempts exceeded.")
            print("Access Denied!")

    return False