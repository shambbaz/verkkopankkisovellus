from database import create_database, add_user, get_user

def main():
    print("Tervetuloa verkkopankkiin!")
    create_database()  # Alustetaan tietokanta

    while True:
        print("\nValitse toiminto:")
        print("1. Rekisteröidy")
        print("2. Kirjaudu sisään")
        print("3. Lopeta")

        choice = input("Valintasi: ")

        if choice == "1":
            username = input("Käyttäjänimi: ")
            password = input("Salasana: ")
            add_user(username, password)
            print("Rekisteröinti onnistui!")
        elif choice == "2":
            username = input("Käyttäjänimi: ")
            password = input("Salasana: ")
            user = get_user(username)
            if user and user[2] == password:
                print(f"Tervetuloa takaisin, {username}!")
                print(f"Saldo: {user[3]}€")
            else:
                print("Virheellinen käyttäjänimi tai salasana.")
        elif choice == "3":
            print("Kiitos käynnistä! Näkemiin!")
            break
        else:
            print("Virheellinen valinta.")

if __name__ == "__main__":
    main()
