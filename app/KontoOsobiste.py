import re
from app.Konto import Konto


class KontoOsobiste(Konto):
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        super().__init__()
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.oplata_przelewu_ekspresowego = 1
        self.czyPeselJestPoprawny()
        if kod_rabatowy is not None and self.czyKlientPo1960():
            self.realizacjaKoduRabatowego(kod_rabatowy)

    def czyPeselJestPoprawny(self):
        if len(self.pesel) != 11:
            self.pesel = "Niepoprawny pesel!"

    def rokUrodzeniaKlienta(self):
        cyfra_rok = int(self.pesel[2])
        rok_urodzenia = None
        if cyfra_rok == 0 or cyfra_rok == 1:
            rok_urodzenia = 1900 + int(self.pesel[0:2])
        elif cyfra_rok == 2 or cyfra_rok == 3:
            rok_urodzenia = 2000 + int(self.pesel[0:2])
        elif cyfra_rok == 4 or cyfra_rok == 5:
            rok_urodzenia = 2100 + int(self.pesel[0:2])
        elif cyfra_rok == 6 or cyfra_rok == 7:
            rok_urodzenia = 2200 + int(self.pesel[0:2])
        elif cyfra_rok == 8 or cyfra_rok == 9:
            rok_urodzenia = 1800 + int(self.pesel[0:2])
        return rok_urodzenia

    def czyKlientPo1960(self):
        return self.rokUrodzeniaKlienta() > 1960

    def realizacjaKoduRabatowego(self, kod_rabatowy):
        if re.match(r"^PROM_[a-zA-Z0-9][a-zA-Z0-9]\b", kod_rabatowy):
            self.saldo = self.saldo + 50



