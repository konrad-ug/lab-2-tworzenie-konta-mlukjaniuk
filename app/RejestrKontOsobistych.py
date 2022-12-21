from app.Konto import Konto


class RejestrKontOsobistych():
    lista_kont = []

    @classmethod
    def dodajKonto(cls, konto):
        cls.lista_kont.append(konto)

    @classmethod
    def wyszukajKontoPoPeselu(cls, pesel):
        for konto in cls.lista_kont:
            if konto.pesel == pesel:
                return konto
        return None

    @classmethod
    def liczbaKont(cls):
        return len(cls.lista_kont)

    @classmethod
    def usunKonto(cls, pesel):
        for konto in cls.lista_kont:
            if konto.pesel == pesel:
                cls.lista_kont.remove(konto)
                return True
        return False

    @classmethod
    def aktualizujDaneKonta(cls, pesel, dane):
        konto = cls.wyszukajKontoPoPeselu(pesel)
        if konto is None:
            return False
        else:
            if dane.get("imie") is not None:
                konto.imie = dane["imie"]
            if dane.get("nazwisko") is not None:
                konto.nazwisko = dane["nazwisko"]
            if dane.get("pesel") is not None:
                konto.pesel = dane["pesel"]
            if dane.get("saldo") is not None:
                konto.saldo = dane["saldo"]
            return True
