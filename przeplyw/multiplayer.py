def turniej_multiplayer(funkcja_gry):
    print("\n=== TRYB WIELOOSOBOWY (Turniej do 3 punktów) ===")
    gracz1 = input("Podaj imię Gracza 1: ")
    gracz2 = input("Podaj imię Gracza 2: ")

    punkty_g1 = 0
    punkty_g2 = 0
    runda = 1

    while punkty_g1 < 3 and punkty_g2 < 3:
        print(f"\n{'=' * 30}")
        print(f"RUNDA {runda} | WYNIK: {gracz1} [{punkty_g1} : {punkty_g2}] {gracz2}")
        print(f"{'=' * 30}")

        print(f"\nKolej gracza: {gracz1}!")
        wynik_g1 = funkcja_gry()

        if wynik_g1 == True:
            punkty_g1 += 1
            print(f"\nBRAWO! {gracz1} zdobywa punkt!")
        else:
            print(f"\nNiestety, {gracz1} nie odgadł hasła.")

        if punkty_g1 == 3:
            break

        print(f"\nKolej gracza: {gracz2}!")
        wynik_g2 = funkcja_gry()

        if wynik_g2 == True:
            punkty_g2 += 1
            print(f"\nBRAWO! {gracz2} zdobywa punkt!")
        else:
            print(f"\nNiestety, {gracz2} nie odgadł hasła.")

        runda += 1

    print("\n" + "*" * 30)
    print("        KONIEC TURNIEJU!        ")
    print("*" * 30)
    print(f"Ostateczny wynik: {gracz1} [{punkty_g1} : {punkty_g2}] {gracz2}")

    if punkty_g1 >= 3:
        print(f"\nZwycięzcą zostaje: {gracz1}!")
    else:
        print(f"\nZwycięzcą zostaje: {gracz2}!")

    wybor = input("\nCzy chcesz zapisać wynik turnieju? (t/n): ")
    if wybor.lower() == 't':
        # [KOD MATEUSZA] - zapis statystyk
        print("[MATEUSZ: Zapisywanie wyniku multi do pliku...]")

    print("Naciśnij ENTER, aby wrócić do Menu Głównego...")
    input()