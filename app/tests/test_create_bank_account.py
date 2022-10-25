import unittest

from ..Konto import Konto


class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "12345678911")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_niepoprawny_pesel(self):
        konto = Konto("Dariusz", "Januszewski", "12345678")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!")

    def test_poprawny_pesel(self):
        konto = Konto("Dariusz", "Januszewski", "12345678911")
        self.assertEqual(konto.pesel, "12345678911")

    def test_niepoprawny_kod(self):
        konto = Konto("Dariusz", "Januszewski", "12345678911", "prom_12")
        self.assertEqual(konto.saldo, 0)

    def test_poprawny_kod(self):
        konto = Konto("Dariusz", "Januszewski", "12345678911", "PROM_12")
        self.assertEqual(konto.saldo, 50)
