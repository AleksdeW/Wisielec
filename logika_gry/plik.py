class HangmanGame:
    def __init__(self, word, max_lives=6):
        self.word = word.lower()
        self.max_lives = max_lives
        self.lives = max_lives
        self.odkryte = []

    def guess_litera(self, litera):
        litera = litera.lower()

        # check na liczbe liter
        if len(litera) != 1 or not litera.isalpha():
            return "Podaj jedną literę alfabetu."

        # sprawdzenie czy litera była już podana
        if litera in self.odkryte:
            return f"Litera '{litera}' została już podana."

        # dodanie litery do odkrytych
        self.odkryte.append(litera)

        # aktualizacja liczby żyć
        if litera not in self.word:
            self.lives -= 1
            return f"Zła litera! Pozostało żyć: {self.lives}"

        return "Dobra litera!"

    # aktualny stan słowa
    def get_word_state(self):
        result = ""

        for litera in self.word:
            if litera in self.odkryte:
                result += litera + " "
            else:
                result += "_ "

        return result.strip()

    # Sprawdzanie warunków wygranej i przegranej
    def is_won(self):
        for litera in self.word:
            if litera not in self.odkryte:
                return False
        return True
    
    def is_lost(self):
        return self.lives <= 0