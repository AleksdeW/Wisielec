from przeplyw.multiplayer import tryb_multiplayer
from dane.gra import wczytaj_baze_z_pliku, wylosuj_haslo
from interfejs.input_handler import pobierz_litere
from logika_gry.plik import HangmanGame
from dane.wczytanie_gry import wczytaj_gre, zapisz_gre
from interfejs.szubienica import pokaz_szubienice 

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
        
    poziom = input("Wybierz poziom (łatwy, średni, trudny): ").strip().lower()
    
    if poziom not in baza:
        print(f"Błąd: Nie ma takiego poziomu jak '{poziom}'!")
        return False
        
    dostepne_kategorie = ", ".join(baza[poziom].keys())
    print(f"\nDostępne kategorie dla poziomu '{poziom}': {dostepne_kategorie}")
    
    kategoria = input("Wybierz kategorię: ").strip()
    
    haslo = wylosuj_haslo(baza, poziom, kategoria)
    
    if haslo is None:
        print("Błąd: Nie udało się wylosować hasła z podanych kategorii.")
        return False
        
    print(f"\nWylosowano hasło do odgadnięcia!")
    gra = HangmanGame(haslo)

    koniec_gry = False
    czy_wygral = False

    while not koniec_gry:
        bledy = gra.max_lives - gra.lives
        print(f"\nPozostało żyć: {gra.lives}")
        pokaz_szubienice(bledy)
        
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

    if not czy_wygral:
        pokaz_szubienice(gra.max_lives)

    print(f"\nSłowo to: {gra.word.upper()}")
    return czy_wygral


def zakonczenie_gry(wynik):
    print("\n=== KONIEC PARTII ===")

    if wynik == True:
        print("WYGRAŁEŚ! Gratulacje!")
    else:
        print("PRZEGRAŁEŚ! Następnym razem pójdzie lepiej.")

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
