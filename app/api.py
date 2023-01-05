from flask import Flask, jsonify, request

from app.KontoOsobiste import KontoOsobiste
from app.RejestrKontOsobistych import RejestrKontOsobistych

app = Flask(__name__)


@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto_osobiste():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    if RejestrKontOsobistych.wyszukajKontoPoPeselu(dane["pesel"]) is not None:
        return "Konto o podanym numerze pesel już istnieje", 400
    else:
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
        RejestrKontOsobistych.aktualizujDaneKonta(pesel, dane)
        return jsonify("Dane konta zaktualizowane"), 202
