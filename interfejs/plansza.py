def pokaz_haslo(haslo, odgadniete_litery):
    wynik = ""

    for litera in haslo:
        if litera.lower() in odgadniete_litery:
            wynik += litera + " "
        else:
            wynik += "_ "

    print(wynik)
