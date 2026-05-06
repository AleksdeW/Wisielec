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