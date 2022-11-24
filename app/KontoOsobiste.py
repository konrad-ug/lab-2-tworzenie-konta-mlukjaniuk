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

    def sprawdzTrzyOstatnieTransakcje(self):
        if len(self.historia_przelewow) < 3:
            return False
        if self.historia_przelewow[-3] > 0 and self.historia_przelewow[-2] > 0 and self.historia_przelewow[-1] > 0:
            return True
        return False

    def sprawdzPiecOstatnichTransakcji(self, kwota_kredytu):
        if len(self.historia_przelewow) < 5:
            return False
        if sum(self.historia_przelewow[-5:]) <= kwota_kredytu:
            return False
        return True

    def zaciagnijKredyt(self, kwota_kredytu):
        if kwota_kredytu <= 0:
            return False
        if self.sprawdzTrzyOstatnieTransakcje() or self.sprawdzPiecOstatnichTransakcji(kwota_kredytu):
            self.saldo = self.saldo + kwota_kredytu
            return True
        return False

