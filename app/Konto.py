import re


class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        self.czyPeselJestPoprawny()
        if kod_rabatowy is not None and self.czyKlientPo1960() is True:
            self.realizacjaKoduRabatowego(kod_rabatowy)

    def czyPeselJestPoprawny(self):
        if len(self.pesel) != 11:
            self.pesel = "Niepoprawny pesel!"

    def czyKlientPo1960(self):
        rok_urodzenia = int(self.pesel[0:2])
        if rok_urodzenia <= 60:
            return False
        else:
            return True

    def realizacjaKoduRabatowego(self, kod_rabatowy):
        if re.match(r"^PROM_[a-zA-Z0-9][a-zA-Z0-9]\b", kod_rabatowy):
            self.saldo = self.saldo + 50

