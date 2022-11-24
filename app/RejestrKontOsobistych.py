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
