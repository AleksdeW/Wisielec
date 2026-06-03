from przeplyw.multiplayer import tryb_multiplayer
from dane.gra import wczytaj_baze_z_pliku, wylosuj_haslo
from interfejs.input_handler import pobierz_litere
from logika_gry.plik import HangmanGame
from dane.wczytanie_gry import wczytaj_gre, zapisz_gre

def uruchom_gre(tryb):
    if tryb == "single":
        print("\n--- GRA JEDNOOSOBOWA ---")
        wynik = zagraj_pojedyncza_partie()
        zakonczenie_gry(wynik)

    elif tryb == "multi":
        tryb_multiplayer(zagraj_pojedyncza_partie)


def zagraj_pojedyncza_partie():
    baza = wczytaj_baze_z_pliku()
    
    if baza is None:
        print("[Błąd] Błąd bazy haseł!")
        return False
        
    poziom = input("Wybierz poziom (np. latwy, sredni, trudny): ")
    kategoria = input("Wybierz kategorię (np. zwierzeta, panstwa): ")
    
    haslo = wylosuj_haslo(baza, poziom, kategoria)
    
    if haslo is None:
        print("Błąd: Nie udało się wylosować hasła z podanych kategorii.")
        return False
        
    print(f"Wylosowano hasło do odgadnięcia!")
    gra = HangmanGame(haslo)

    koniec_gry = False
    czy_wygral = False

    while not koniec_gry:
        # [KOD MAGDY] - funkcja rysująca wisielca
        print(f"\n[MAGDA: Tu rysuje się szubienica, pozostało żyć: {gra.lives}]")
        
        print(f"Hasło: {gra.get_word_state()}")

        litera = pobierz_litere(gra.odkryte)

        komunikat = gra.guess_litera(litera)
        print(komunikat)

        if gra.is_won():
            czy_wygral = True
            koniec_gry = True
        elif gra.is_lost():
            czy_wygral = False
            koniec_gry = True

    print(f"\nSłowo to: {gra.word.upper()}")
    return czy_wygral


def zakonczenie_gry(wynik):
    print("\n=== KONIEC PARTII ===")

    # [KOD MAGDY] - komunikat w zależności od wyniku
    if wynik == True:
        print("WYGRAŁEŚ!")
    else:
        print("PRZEGRAŁEŚ!")

    wybor = input("Czy chcesz zapisać swój wynik w statystykach? (t/n): ")

    if wybor.lower() == 't':
        stare_dane = wczytaj_gre()
        if stare_dane is None:
            wygrane = 0
            przegrane = 0
        else:
            wygrane = stare_dane.get("ilosc_wygranych", 0)
            przegrane = stare_dane.get("ilosc_przegranych", 0)
            
        if wynik == True:
            wygrane += 1
        else:
            przegrane += 1
            
        zapisz_gre(wygrane, przegrane)
        print("Dane pomyślnie zapisane do pliku!")
    else:
        print("Pominięto zapisywanie.")

    print("Naciśnij ENTER, aby wrócić do Menu Głównego...")
    input()
