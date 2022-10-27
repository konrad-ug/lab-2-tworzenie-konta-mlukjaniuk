import re


class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = pesel
        self.czyPeselJestPoprawny()
        if kod_rabatowy is not None and self.czyKlientPo1960():
            self.realizacjaKoduRabatowego(kod_rabatowy)

    def czyPeselJestPoprawny(self):
        if len(self.pesel) != 11:
            self.pesel = "Niepoprawny pesel!"

    def rokUrodzeniaKlienta(self):
        cyfra_kontrolna = int(self.pesel[2])
        if cyfra_kontrolna == 0 or cyfra_kontrolna == 1:
            rok_urodzenia = 1900 + int(self.pesel[0:2])
        else:
            rok_urodzenia = 2000 + int(self.pesel[0:2])
        return rok_urodzenia

    def czyKlientPo1960(self):
        if self.rokUrodzeniaKlienta() > 1960:
            return True
        else:
            return False


    def realizacjaKoduRabatowego(self, kod_rabatowy):
        if re.match(r"^PROM_[a-zA-Z0-9][a-zA-Z0-9]\b", kod_rabatowy):
            self.saldo = self.saldo + 50

