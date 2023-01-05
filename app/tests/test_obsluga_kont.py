import subprocess
import time
import unittest
from unittest.mock import patch

import requests

from app.KontoFirmowe import KontoFirmowe
from app.KontoOsobiste import KontoOsobiste
from app.SMTPConnection import SMTPConnection


class TestObslugaKontOsobistych(unittest.TestCase):
    body = {
        "imie": "Dariusz",
        "nazwisko": "Kowalski",
        "pesel": "12345678901"
    }

    url = "http://localhost:5000"

    def test_1_tworzenie_konta_poprawne(self):
        server_process = subprocess.Popen(["flask", "--app", "app/api.py", "run"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)

        create_response = requests.post(self.url + "/konta/stworz_konto", json=self.body)

        self.assertEqual(create_response.status_code, 201)

        server_process.terminate()
        server_process.wait()

    def test_2_znajdz_po_peselu(self):
        server_process = subprocess.Popen(["flask", "--app", "app/api.py", "run"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)

        requests.post(self.url + "/konta/stworz_konto", json=self.body)

        get_response = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_response.status_code, 200)
        response_body = get_response.json()
        self.assertEqual(response_body, f"Właścicielem konta o peselu {self.body['pesel']} jest {self.body['imie']} {self.body['nazwisko']}."
                                        f" Saldo konta wynosi 0")

        server_process.terminate()
        server_process.wait()

    def test_3_aktualizuj_dane_konta(self):
        server_process = subprocess.Popen(["flask", "--app", "app/api.py", "run"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)

        requests.post(self.url + "/konta/stworz_konto", json=self.body)

        body = {
            "imie": "Jan",
            "nazwisko": "Kowalski",
            "pesel": "12345678901"
        }
        update_response = requests.put(self.url + f"/konta/konto/{self.body['pesel']}", json=body)
        self.assertEqual(update_response.status_code, 202)

        server_process.terminate()
        server_process.wait()

    def test_4_usun_konto(self):
        server_process = subprocess.Popen(["flask", "--app", "app/api.py", "run"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)

        requests.post(self.url + "/konta/stworz_konto", json=self.body)

        delete_response = requests.delete(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(delete_response.status_code, 200)

        server_process.terminate()
        server_process.wait()

    def test_5_tworzenie_konta_nieudane(self):
        server_process = subprocess.Popen(["flask", "--app", "app/api.py", "run"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)

        requests.post(self.url + "/konta/stworz_konto", json=self.body)

        requests.post(self.url + "/konta/stworz_konto", json=self.body)
        create_response = requests.post(self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(create_response.status_code, 400)

        server_process.terminate()
        server_process.wait()




# feature17
class TestNipKontFirmowych(unittest.TestCase):

    @patch('requests.get')
    def test_1_nip_w_rejestrze(self, mock_get):
        mock_get.return_value.status_code = 200
        konto = KontoFirmowe("Firma", "1234567890")
        self.assertEqual(konto.nip, "1234567890")

    # @patch('requests.get')
    # def test_2_nip_nie_w_rejestrze(self, mock_get):
    #     mock_get.return_value.status_code = 404
    #     konto = KontoFirmowe("Firma", "1234567890")
    #     self.assertEqual(konto.nip, "Pranie!")


# feature18
# class TestWysylanieHistoriiMailem(unittest.TestCase):
#
#     def test_1_poprawnie_wyslany_mail_konto_osobiste(self):
#         konto = KontoOsobiste("Dariusz", "Kowalski", "12345678901")
#         konto.wykonajPrzelewPrzychodzacy(100)
#         konto.wykonajPrzelewWychodzacy(50)
#         konto.wykonajPrzelewWychodzacy(50)
#         konto.wykonajPrzelewPrzychodzacy(100)
#         smtp_connector = SMTPConnection()
#         status = konto.wyslijHistorieNaMaila("Xyz123@gmail.com", smtp_connector)
#         self.assertTrue(status)
#
#     def test_2_niepoprawny_mail_konto_osobiste(self):
#         pass
#
#     def test_3_poprawnie_wyslany_mail_konto_firmowe(self):
#         pass
#
#     def test_4_niepoprawny_mail_konto_firmowe(self):
#         pass

