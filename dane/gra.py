import json
import random_number
import os


def wczytaj_baze_z_pliku(nazwa_pliku="hasla.json"):
    """Wczytuje dane z pliku JSON i zwraca je jako słownik Pythona."""
    if not os.path.exists(nazwa_pliku):
        print(f"Błąd: Plik {nazwa_pliku} nie istnieje!")
        return None

    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        return json.load(plik)


def wylosuj_haslo(baza, poziom, kategoria):
    """Pobiera konkretne hasło na podstawie wyboru użytkownika."""
    try:
        lista_slow = baza[poziom][kategoria]

        liczba = random_number.random_number()


        indeks = liczba % len(lista_slow)
        return lista_slow[indeks].upper()
    except KeyError:
        return None
