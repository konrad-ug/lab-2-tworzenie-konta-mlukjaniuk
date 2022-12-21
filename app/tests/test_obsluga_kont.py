import unittest
import requests


class TestObslugaKont(unittest.TestCase):
    body = {
        "imie": "Dariusz",
        "nazwisko": "Kowalski",
        "pesel": "12345678901"
    }

    url = "http://localhost:5000"

    def test_1_tworzenie_konta_poprawne(self):
        create_response = requests.post(self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(create_response.status_code, 201)

    def test_2_znajdz_po_peselu(self):
        get_response = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_response.status_code, 200)
        response_body = get_response.json()
        self.assertEqual(response_body, f"Właścicielem konta o peselu {self.body['pesel']} jest {self.body['imie']} {self.body['nazwisko']}."
                                        f" Saldo konta wynosi 0")

    def test_3_aktualizuj_dane_konta(self):
        body = {
            "imie": "Jan",
            "nazwisko": "Kowalski",
            "pesel": "12345678901"
        }
        update_response = requests.put(self.url + f"/konta/konto/{self.body['pesel']}", json=body)
        self.assertEqual(update_response.status_code, 202)

    def test_4_usun_konto(self):
        delete_response = requests.delete(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(delete_response.status_code, 200)

    def test_5_tworzenie_konta_nieudane(self):
        requests.post(self.url + "/konta/stworz_konto", json=self.body)
        create_response = requests.post(self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(create_response.status_code, 400)


