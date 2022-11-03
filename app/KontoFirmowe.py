from app.Konto import Konto


class KontoFirmowe(Konto):

    def __init__(self, nazwa_firmy, nip):
        super().__init__()
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip
        self.oplata_przelewu_ekspresowego = 5
        self.czyNipJestPoprawny()

    def czyNipJestPoprawny(self):
        if len(self.nip) != 10:
            self.nip = "Niepoprawny NIP!"

