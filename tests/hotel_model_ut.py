import unittest

from models.hotel import HotelModel


class HotelModelTest(unittest.TestCase):
    def test_hotel_model(self):
        hotel_id = "bravo"
        nome = "Bravo Hotel"
        estrelas = 4.29
        diaria = 720.20
        cidade = "Rio de Janeiro"

        novo_hotel = HotelModel(
            hotel_id=hotel_id,
            nome=nome,
            estrelas=estrelas,
            diaria=diaria,
            cidade=cidade
        )

        assert novo_hotel.hotel_id == hotel_id
        assert novo_hotel.nome == nome

