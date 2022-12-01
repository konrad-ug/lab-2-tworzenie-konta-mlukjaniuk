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
    print(f"Request o konto z pesel: {pesel}")
    konto = RejestrKontOsobistych.wyszukajKontoPoPeselu(pesel)
    if konto is None:
        return jsonify("Nie znaleziono konta"), 404
    else:
        return jsonify(f"Właścicielem konta o peselu {pesel} jest {konto.imie} {konto.nazwisko}. Saldo konta wynosi"
                       f" {konto.saldo}"), 200
