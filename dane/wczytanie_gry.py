import json
import os


def wczytaj_gre(nazwa_pliku="zapis_gry.json"):
    # Sprawdzamy, czy gracz ma w ogóle jakiś zapis gry
    if not os.path.exists(nazwa_pliku):
        print("Nie znaleziono pliku zapisu!")
        return None

    # Używamy 'r' (read - odczyt) tak samo jak przy bazie haseł
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        zapisane_dane = json.load(plik)
        return zapisane_dane


def zapisz_gre(new_x, new_y):
    filename = "zapisy_gry.json"


    dane_do_zapisu = {
        "ilosc_wygranych": new_x,
        "ilosc_przegranych": new_y
    }

    with open(filename, "w") as f:

        json.dump(dane_do_zapisu, f, indent=4)


