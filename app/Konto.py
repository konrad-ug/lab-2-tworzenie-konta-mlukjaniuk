class Konto:
    def __init__(self):
        self.saldo = 0
        self.oplata_przelewu_ekspresowego = 0
        self.historia_przelewow = []

    def dodajPrzelewDoHistorii(self, kwota_przelewu):
        self.historia_przelewow.append(kwota_przelewu)

    def dodajPrzelewEkspresowyDoHistorii(self, kwota_przelewu):
        self.historia_przelewow.append(-kwota_przelewu)
        self.historia_przelewow.append(-self.oplata_przelewu_ekspresowego)

    def wykonajPrzelewWychodzacy(self, kwota_przelewu):
        if self.saldo >= kwota_przelewu > 0:
            self.saldo = self.saldo - kwota_przelewu
        self.dodajPrzelewDoHistorii(-kwota_przelewu)

    def wykonajPrzelewPrzychodzacy(self, kwota_przelewu):
        if kwota_przelewu > 0:
            self.saldo = self.saldo + kwota_przelewu
        self.dodajPrzelewDoHistorii(kwota_przelewu)

    def wykonajPrzelewWychodzacyEkspresowy(self, kwota_przelewu):
        if self.saldo >= kwota_przelewu > 0:
            self.saldo = self.saldo - kwota_przelewu - self.oplata_przelewu_ekspresowego
        self.dodajPrzelewEkspresowyDoHistorii(kwota_przelewu)



