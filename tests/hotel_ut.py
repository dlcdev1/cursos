import unittest

from tests.fixtures import HOTEIS
from resources.hotel import Hoteis, Hotel


class HoteisTest(unittest.TestCase):
    def test_get(self):
        hoteis = Hoteis()
        result = hoteis.get()

        assert result['hoteis'] == HOTEIS


class HotelTest(unittest.TestCase):
    def test_find_hotel(self):
        expected_nome = 'Bravo Hotel'
        expected_cidade = 'Santa Catarina'
        expected_diaria = 380.90
        expected_estrelas = 4.4

        hotel_id = 'bravo'
        hotel = Hotel()
        result = hotel.find_hotel(hotel_id=hotel_id)
        assert result['nome'] == expected_nome
        assert result['cidade'] == expected_cidade
        assert result['diaria'] == expected_diaria
        assert result['estrelas'] == expected_estrelas

    def test_not_find_hotel(self):
        expected_result = None
        hotel_id = "empty"
        hotel = Hotel()
        result = hotel.find_hotel(hotel_id=hotel_id)

        assert result == expected_result

    def test_get_hotel_for_id(self, mocker):
        expected_hotel_nome = 'Alpha Hotel'
        expected_hotel_cidade = 'Rio de Janeiro'
        hotel_id = 'alpha'
        hotel = Hotel()
        result = hotel.get(hotel_id)
        assert result['nome'] == HOTEIS[0]['nome']
        assert result['cidade'] == HOTEIS[0]['cidade']

