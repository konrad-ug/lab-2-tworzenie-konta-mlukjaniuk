from flask import Flask, request, jsonify
from app.RejestrKontOsobistych import RejestrKontOsobistych
from app.KontoOsobiste import KontoOsobiste
app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto_osobiste():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = KontoOsobiste(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKontOsobistych.dodajKonto(konto)
    return jsonify("Konto stworzone"), 201


@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    print("Request o liczbe kont")
    return jsonify(RejestrKontOsobistych.liczbaKont()), 200


@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f"Request o konto z peselem: {pesel}")
    konto = RejestrKontOsobistych.wyszukajKontoPoPeselu(pesel)
    if konto is None:
        return jsonify("Nie znaleziono konta"), 404
    else:
        return jsonify(f"Właścicielem konta o peselu {pesel} jest {konto.imie} {konto.nazwisko}. Saldo konta wynosi"
                       f" {konto.saldo}"), 200


@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def usun_konto_z_peselem(pesel):
    print(f"Request o usunięcie konta z peselem: {pesel}")
    konto = RejestrKontOsobistych.wyszukajKontoPoPeselu(pesel)
    if konto is None:
        return jsonify("Nie znaleziono konta"), 404
    else:
        RejestrKontOsobistych.usunKonto(pesel)
        return jsonify("Konto usunięte"), 200


@app.route("/konta/konto/<pesel>", methods=['PUT'])
def aktualizuj_dane_konta(pesel):
    dane = request.get_json()
    print(f"Request o aktualizację danych konta z peselem: {pesel}")
    konto = RejestrKontOsobistych.wyszukajKontoPoPeselu(pesel)
    if konto is None:
        return jsonify("Nie znaleziono konta"), 404
    else:
        if dane.get("imie") is not None:
            konto.imie = dane["imie"]
        if dane.get("nazwisko") is not None:
            konto.nazwisko = dane["nazwisko"]
        if dane.get("pesel") is not None:
            konto.pesel = dane["pesel"]
        if dane.get("saldo") is not None:
            konto.saldo = dane["saldo"]
        return jsonify(f"Dane konta zaktualizowane: Imię: {konto.imie}, Nazwisko: {konto.nazwisko}, Pesel:"
                       f" {konto.pesel}, Saldo: {konto.saldo}"), 200
