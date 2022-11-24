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

    def zaciagnijKredyt(self, kwota_kredytu):
        if kwota_kredytu <= 0:
            return False
        if self.saldo >= 2 * kwota_kredytu and -1775 in self.historia_przelewow:
            self.saldo = self.saldo + kwota_kredytu
            return True
        return False
