def pobierz_litere(uzyte_litery):
    while True:
        znak = input("Podaj literę: ").lower().strip()

        # użytkownik musi wpisać 1 znak
        if len(znak) != 1:
            print("Wpisz tylko jedną literę.")
            continue

        # znak musi być literą
        if not znak.isalpha():
            print("Musisz podać literę.")
            continue

        # litera nie może się powtarzać
        if znak in uzyte_litery:
            print("Ta litera była już podana.")
            continue

        return znak
