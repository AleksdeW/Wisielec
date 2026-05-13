from przeplyw.game_controls import uruchom_gre

def uruchom_menu():
    while True:
        # [KOD MAGDY] - wyświetlanie
        print("\n=== GRA W WISIELCA ===")
        print("1. Gra Jednoosobowa")
        print("2. Gra Wieloosobowa")
        print("3. Pokaż Statystyki")
        print("4. Wyjście z gry")
        print("======================")

        wybor = input("Twój wybór (1-4): ")

        if wybor == '1':
            print("\n[Uruchamiam tryb jednoosobowy...]")
            uruchom_gre(tryb="single")

        elif wybor == '2':
            print("\n[Uruchamiam tryb wieloosobowy...]")
            uruchom_gre(tryb="multi")

        elif wybor == '3':
            print("\n--- STATYSTYKI ---")
            # [KOD MATEUSZA] - pobranie danych o wygranych
            # [KOD MAGDY] - wyświetlenie tych danych na ekranie
            print("(Tu będą statystyki)")
            input("Naciśnij ENTER, aby wrócić...")

        elif wybor == '4':
            print("\nDo zobaczenia!")
            break

        else:
            # [KOD MAGDY] - W przyszłości jej ładny komunikat o błędzie
            print("\nBŁĄD: Nie ma takiej opcji. Wpisz cyfrę od 1 do 4.")
