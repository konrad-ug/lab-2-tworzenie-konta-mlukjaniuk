class Konto:
    def __init__(self):
        self.saldo = 0
        self.oplata_przelewu_ekspresowego = 0

    def wykonajPrzelewWychodzacy(self, kwota_przelewu):
        if self.saldo >= kwota_przelewu > 0:
            self.saldo = self.saldo - kwota_przelewu

    def wykonajPrzelewPrzychodzacy(self, kwota_przelewu):
        if kwota_przelewu > 0:
            self.saldo = self.saldo + kwota_przelewu

    def wykonajPrzelewWychodzacyEkspresowy(self, kwota_przelewu):
        if self.saldo >= kwota_przelewu > 0:
            self.saldo = self.saldo - kwota_przelewu - self.oplata_przelewu_ekspresowego
