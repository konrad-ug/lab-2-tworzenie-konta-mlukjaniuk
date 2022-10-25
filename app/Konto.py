class Konto:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        self.czyPeselJestPoprawny()

    def czyPeselJestPoprawny(self):
        if len(self.pesel) != 11:
            self.pesel = "Niepoprawny pesel!"
