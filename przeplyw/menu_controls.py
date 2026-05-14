from przeplyw.game_controls import uruchom_gre
from dane.wczytanie_gry import wczytaj_gre

def uruchom_menu():
    while True:
        # [KOD MAGDY] - wyświetlanie
        #przykład
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
            statystyki = wczytaj_gre()
            
            if statystyki:
                # [KOD MAGDY] - wyswietlanie tabeli wyników
                # przykład
                print(f"Wygrane: {statystyki.get('ilosc_wygranych', 0)}")
                print(f"Przegrane: {statystyki.get('ilosc_przegranych', 0)}")
            else:
                print("Nie znaleziono zapisanych statystyk.")
                
            input("\nNaciśnij ENTER, aby wrócić do menu...")

        elif wybor == '4':
            print("\nDo zobaczenia!")
            break

        else:
            print("\nBŁĄD: Nie ma takiej opcji. Wpisz cyfrę od 1 do 4.")
