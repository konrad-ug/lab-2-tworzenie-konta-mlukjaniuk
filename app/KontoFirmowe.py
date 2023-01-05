from app.Konto import Konto
import requests
import os
BANK_APP_MF_URL = os.getenv('BANK_APP_MF_URL') or 'https://wl-api.mf.gov.pl/api/search/nip/'


class KontoFirmowe(Konto):

    def __init__(self, nazwa_firmy, nip):
        super().__init__()
        self.nazwa_firmy = nazwa_firmy
        self.nip = nip
        self.oplata_przelewu_ekspresowego = 5
        self.czyNipJestPoprawny()
        if self.czyNipWRejestrze(nip) is False:
            raise ValueError("NIP nie jest w rejestrze!")

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

    def czyNipWRejestrze(self, nip):
        response = requests.get(BANK_APP_MF_URL + nip + '?date=2022-12-28')
        if response.status_code == 200:
            return True
        elif self.nip == "Niepoprawny NIP!":
            return None
        else:
            self.nip = "Pranie!"
            return False
