import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):

    # feature1
    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "12345678911")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    # feature2
    def test_niepoprawny_pesel(self):
        konto = Konto("Dariusz", "Januszewski", "12345678")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!")

    # feature3
    def test_poprawny_pesel(self):
        konto = Konto("Dariusz", "Januszewski", "12345678911")
        self.assertEqual(konto.pesel, "12345678911")

    # feature4
    def test_niepoprawny_kod(self):
        konto = Konto("Dariusz", "Januszewski", "61345678911", "prom_12")
        self.assertEqual(konto.saldo, 0)

    def test_poprawny_kod(self):
        konto = Konto("Dariusz", "Januszewski", "61345678911", "PROM_12")
        self.assertEqual(konto.saldo, 50)

    # feature5
    def test_niepoprawny_kod_po_1960(self):
        konto = Konto("Dariusz", "Januszewski", "62041678911", "prom_12")
        self.assertEqual(konto.saldo, 0)

    def test_poprawny_kod_po_1960(self):
        konto = Konto("Dariusz", "Januszewski", "62041678911", "PROM_12")
        self.assertEqual(konto.saldo, 50)

    def test_niepoprawny_kod_do_1960(self):
        konto = Konto("Dariusz", "Januszewski", "59041678911", "prom_12")
        self.assertEqual(konto.saldo, 0)

    def test_poprawny_kod_do_1960(self):
        konto = Konto("Dariusz", "Januszewski", "59041678911", "PROM_12")
        self.assertEqual(konto.saldo, 0)
