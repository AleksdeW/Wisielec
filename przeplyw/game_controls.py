from przeplyw.multiplayer import tryb_multiplayer
from dane.gra import wczytaj_baze_z_pliku, wylosuj_haslo

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
        print("[Błąd bazy haseł!")
    else:
        poziom = input("Wybierz poziom (np. latwy, sredni, trudny): ")
        kategoria = input("Wybierz kategorię (np. zwierzeta, panstwa): ")
        
        haslo = wylosuj_haslo(baza, poziom, kategoria)
             
    print(f"Wylosowano hasło do odgadnięcia!")

    koniec_gry = False
    czy_wygral = False

    while not koniec_gry:
        # [KOD MAGDY] - funkcja rysująca wisielca i ukryte hasło
        print("\n[MAGDA: Tu rysuje się szubienica i aktualny stan hasła]")

        # [KOD MAGDY] - funkcja pobierająca literę od gracza
        litera = input("Podaj literę: ")

        # [KOD JANA] - funkcja sprawdzająca czy litera jest w haśle
        print(f"[JANEK: Sprawdzam, czy litera '{litera}' jest poprawna...]")

        # [KOD JANA] - funkcja Janka musi zwracać dwie rzeczy:

        # --- TYMCZASOWA SYMULACJA DO TESTÓW (Zanim Janek napisze kod) ---
        decyzja = input("Symulacja: Czy udało się odgadnąć hasło? (t/n): ")
        if decyzja.lower() == 't':
            czy_wygral = True
            koniec_gry = True
        else:
            decyzja_porazka = input("Symulacja: Czy skończyły się życia? (t/n): ")
            if decyzja_porazka.lower() == 't':
                czy_wygral = False
                koniec_gry = True

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
