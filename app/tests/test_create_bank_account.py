import unittest

from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe


class TestCreateBankAccount(unittest.TestCase):

    # feature1
    def test_tworzenie_konta(self):
        pierwsze_konto = KontoOsobiste("Dariusz", "Januszewski", "12345678911")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    # feature2
    def test_niepoprawny_pesel(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "12345678")
        self.assertEqual(konto.pesel, "Niepoprawny pesel!")

    # feature3
    def test_poprawny_pesel(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "12345678911")
        self.assertEqual(konto.pesel, "12345678911")

    # feature4
    def test_niepoprawny_kod(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "61345678911", "prom_12")
        self.assertEqual(konto.saldo, 0)

    def test_poprawny_kod(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "61345678911", "PROM_12")
        self.assertEqual(konto.saldo, 50)

    # feature5
    def test_niepoprawny_kod_po_1960(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "62041678911", "prom_12")
        self.assertEqual(konto.saldo, 0)

    def test_poprawny_kod_po_1960(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "62041678911", "PROM_12")
        self.assertEqual(konto.saldo, 50)

    def test_niepoprawny_kod_do_1960(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "59041678911", "prom_12")
        self.assertEqual(konto.saldo, 0)

    def test_poprawny_kod_do_1960(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "59041678911", "PROM_12")
        self.assertEqual(konto.saldo, 0)

    def test_wykorzystany_kod_po_2000(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "62241678911", "PROM_12")
        self.assertEqual(konto.saldo, 50)

    def test_wykorzystany_kod_po_2100(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "62441678911", "PROM_12")
        self.assertEqual(konto.saldo, 50)

    def test_wykorzystany_kod_po_2200(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "62641678911", "PROM_12")
        self.assertEqual(konto.saldo, 50)

    def test_wykorzystany_kod_po_1800(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "60841678911", "PROM_12")
        self.assertEqual(konto.saldo, 0)


    # feature6
class TestKsiegowaniePrzelewowWychodzacych(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "62041678911"

    def test_udany_przelew_wychodzacy(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.wykonajPrzelewWychodzacy(800)
        self.assertEqual(konto.saldo, 1000-800)

    def test_nieudany_przelew_wychodzacy_za_male_saldo(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 100
        konto.wykonajPrzelewWychodzacy(800)
        self.assertEqual(konto.saldo, 100)

    def test_nieudany_przelew_wychodzacy_zla_kwota(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.wykonajPrzelewWychodzacy(-800)
        self.assertEqual(konto.saldo, 1000)

    def test_nieudany_przelew_wychodzacy_debet(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = -1
        konto.wykonajPrzelewWychodzacy(800)
        self.assertEqual(konto.saldo, -1)


class TestKsiegowaniePrzelewowPrzychodzacych(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "62041678911"

    def test_udany_przelew_przychodzacy(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.wykonajPrzelewPrzychodzacy(800)
        self.assertEqual(konto.saldo, 1000+800)

    def test_udany_przelew_przychodzacy_debet(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = -1
        konto.wykonajPrzelewPrzychodzacy(800)
        self.assertEqual(konto.saldo, -1+800)

    def test_nieudany_przelew_przychodzacy_zla_kwota(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.wykonajPrzelewPrzychodzacy(-800)
        self.assertEqual(konto.saldo, 1000)


    # feature7
class TestTworzenieKontaFirmowego(unittest.TestCase):
    nazwa_firmy = "Firma"

    def test_poprawny_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "1234567890")
        self.assertEqual(konto.nip, "1234567890")

    def test_zbyt_dlugi_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "123456789000")
        self.assertEqual(konto.nip, "Niepoprawny NIP!")

    def test_zbyt_krotki_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "123456789")
        self.assertEqual(konto.nip, "Niepoprawny NIP!")

    def test_niewpisany_nip(self):
        konto = KontoFirmowe(self.nazwa_firmy, "")
        self.assertEqual(konto.nip, "Niepoprawny NIP!")


class TestKsiegowaniePrzelewowWychodzacychKontoFirmowe(unittest.TestCase):
    nazwa_firmy = "Firma"
    nip = "1234567890"

    def test_udany_przelew_wychodzacy(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.wykonajPrzelewWychodzacy(800)
        self.assertEqual(konto.saldo, 1000-800)

    def test_nieudany_przelew_wychodzacy_za_male_saldo(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 100
        konto.wykonajPrzelewWychodzacy(800)
        self.assertEqual(konto.saldo, 100)

    def test_nieudany_przelew_wychodzacy_debet(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = -5
        konto.wykonajPrzelewWychodzacy(800)
        self.assertEqual(konto.saldo, -5)

    def test_nieudany_przelew_wychodzacy_zla_kwota(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.wykonajPrzelewWychodzacy(-800)
        self.assertEqual(konto.saldo, 1000)


class TestKsiegowaniePrzelewowPrzychodzacychKontoFirmowe(unittest.TestCase):
    nazwa_firmy = "Firma"
    nip = "1234567890"

    def test_udany_przelew_przychodzacy(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.wykonajPrzelewPrzychodzacy(800)
        self.assertEqual(konto.saldo, 1000+800)

    def test_udany_przelew_przychodzacy_debet(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = -5
        konto.wykonajPrzelewPrzychodzacy(800)
        self.assertEqual(konto.saldo, -5+800)

    def test_nieudany_przelew_przychodzacy_zla_kwota(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.wykonajPrzelewPrzychodzacy(-800)
        self.assertEqual(konto.saldo, 1000)


    # feature8
class TestKsiegowaniePrzelewowWychodzacychEkspresowychKontoFirmowe(unittest.TestCase):
    nazwa_firmy = "Firma"
    nip = "1234567890"

    def test_udany_przelew_wychodzacy(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.wykonajPrzelewWychodzacyEkspresowy(800)
        self.assertEqual(konto.saldo, 1000-800-5)

    def test_nieudany_przelew_wychodzacy_zla_kwota(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.wykonajPrzelewWychodzacyEkspresowy(-800)
        self.assertEqual(konto.saldo, 1000)

    def test_udany_przelew_wychodzacy_saldo_ponizej_0(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 100
        konto.wykonajPrzelewWychodzacyEkspresowy(100)
        self.assertEqual(konto.saldo, 100-100-5)

    def test_nieudany_przelew_ekspresowy_zbyt_duza_kwota(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 100
        konto.wykonajPrzelewWychodzacyEkspresowy(1000)
        self.assertEqual(konto.saldo, 100)

    def test_nieudany_przelew_ekspresowy_debet(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = -5
        konto.wykonajPrzelewWychodzacyEkspresowy(800)
        self.assertEqual(konto.saldo, -5)


class TestKsiegowaniePrzelewowWychodzacychEkspresowychKontoPrywatne(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "62041678911"

    def test_udany_przelew_wychodzacy(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.wykonajPrzelewWychodzacyEkspresowy(800)
        self.assertEqual(konto.saldo, 1000-800-1)

    def test_nieudany_przelew_wychodzacy_zla_kwota(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.wykonajPrzelewWychodzacyEkspresowy(-800)
        self.assertEqual(konto.saldo, 1000)

    def test_udany_przelew_ekspresowy_saldo_ponizej_0(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 100
        konto.wykonajPrzelewWychodzacyEkspresowy(100)
        self.assertEqual(konto.saldo, 100-100-1)

    def test_nieudany_przelew_ekspresowy_zbyt_duza_kwota(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 100
        konto.wykonajPrzelewWychodzacyEkspresowy(1000)
        self.assertEqual(konto.saldo, 100)

    def test_nieudany_przelew_ekspresowy_debet(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = -5
        konto.wykonajPrzelewWychodzacyEkspresowy(800)
        self.assertEqual(konto.saldo, -5)

    # feature9
class TestHistoriaPrzelewowKontoOsobiste(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "62041678911"

    def test_utworzona_historia_przelewow(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(konto.historia_przelewow, [])

    def test_dodanie_przelewu_przychodzacego(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.wykonajPrzelewPrzychodzacy(100)
        self.assertEqual(konto.historia_przelewow, [100])

    def test_dodanie_przelewu_wychodzacego(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.wykonajPrzelewWychodzacy(100)
        self.assertEqual(konto.historia_przelewow, [-100])

    def test_dodanie_przelewu_wychodzacego_ekspresowego(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.wykonajPrzelewWychodzacyEkspresowy(100)
        self.assertEqual(konto.historia_przelewow, [-100, -1])

    def test_dodanie_kilku_przelewow(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.wykonajPrzelewPrzychodzacy(500)
        konto.wykonajPrzelewWychodzacy(200)
        konto.wykonajPrzelewWychodzacyEkspresowy(100)
        self.assertEqual(konto.historia_przelewow, [500, -200, -100, -1])


class TestHistoriaPrzelewowKontoFirmowe(unittest.TestCase):
    nazwa_firmy = "Firma"
    nip = "1234567890"

    def test_utworzona_historia_przelewow(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        self.assertEqual(konto.historia_przelewow, [])

    def test_dodanie_przelewu_przychodzacego(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.wykonajPrzelewPrzychodzacy(100)
        self.assertEqual(konto.historia_przelewow, [100])

    def test_dodanie_przelewu_wychodzacego(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.wykonajPrzelewWychodzacy(100)
        self.assertEqual(konto.historia_przelewow, [-100])

    def test_dodanie_przelewu_wychodzacego_ekspresowego(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.wykonajPrzelewWychodzacyEkspresowy(100)
        self.assertEqual(konto.historia_przelewow, [-100, -5])

    def test_dodanie_kilku_przelewow(self):
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.wykonajPrzelewPrzychodzacy(500)
        konto.wykonajPrzelewWychodzacy(200)
        konto.wykonajPrzelewWychodzacyEkspresowy(100)
        self.assertEqual(konto.historia_przelewow, [500, -200, -100, -5])
