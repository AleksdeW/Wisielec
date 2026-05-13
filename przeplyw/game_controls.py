def uruchom_gre(tryb):

    haslo = ""

    if tryb == "single":
        print("\n--- GRA JEDNOOSOBOWA ---")
        # [KOD MATEUSZA] - funkcję do losowania hasła.
        haslo = "PROGRAMOWANIE"
        print("[Wylosowano hasło z bazy!]")

    elif tryb == "multi":
        print("\n--- GRA WIELOOSOBOWA ---")
        haslo = input("Gracz 1, podaj hasło (Gracz 2 nie patrzy!): ")

    petla_rozgrywki(haslo)


def petla_rozgrywki(haslo):

    koniec_gry = False

    while not koniec_gry:
        # [KOD MAGDY] - funkcja rysująca wisielca i ukryte hasło
        print("\n[MAGDA: Tu rysuje się szubienica i aktualny stan hasła]")

        # [KOD MAGDY] - funkcja pobierająca literę od gracza
        litera = input("Podaj literę: ")

        # [KOD JANA] - funkcja sprawdzająca czy litera jest w haśle
        print(f"[JANEK: Sprawdzam, czy litera '{litera}' jest poprawna...]")

        # [KOD JANA] - czy gra się skończyła
        # koniec_gry = sprawdz_czy_koniec()

    zakonczenie_gry()


def zakonczenie_gry():

    print("\n=== KONIEC PARTII ===")

    # [KOD MAGDY] - wyświetlenie komunikatu "WYGRAŁEŚ!" lub "PRZEGRAŁEŚ!"

    wybor = input("Czy chcesz zapisać swój wynik w statystykach? (t/n): ")

    if wybor.lower() == 't':
        # [KOD MATEUSZA] - funkcja zapisująca statystyki/stan do pliku
        print("[MATEUSZ: Zapisywanie danych do pliku...]")
    else:
        print("Pominięto zapisywanie.")

    print("Naciśnij ENTER, aby wrócić do Menu Głównego...")
    input()