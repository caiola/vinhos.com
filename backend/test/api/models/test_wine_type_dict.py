import unittest

from api.models.wine_type_dict import WineTypes


class TestWineTypes(unittest.TestCase):
    def test_all(self):
        # Arrange
        expected_wine_types = [
            # Category: Vinho
            {"id": 101, "main_category_id": 1, "name": "Branco"},
            {"id": 102, "main_category_id": 1, "name": "Branco Doce"},
            {"id": 103, "main_category_id": 1, "name": "Champagne"},
            {"id": 104, "main_category_id": 1, "name": "Colheita tardia"},
            {"id": 105, "main_category_id": 1, "name": "Espumante"},
            {"id": 106, "main_category_id": 1, "name": "Rosé"},
            {"id": 107, "main_category_id": 1, "name": "Tinto"},
            {"id": 108, "main_category_id": 1, "name": "Sake"},
            # Category: Porto
            {"id": 201, "main_category_id": 2, "name": "Raridades"},
            {"id": 202, "main_category_id": 2, "name": "Porto Garrafeira"},
            {"id": 203, "main_category_id": 2, "name": "Miniaturas"},
            {"id": 204, "main_category_id": 2, "name": "Magnum & Superiores"},
            {"id": 205, "main_category_id": 2, "name": "Garrafas Únicas"},
            {"id": 206, "main_category_id": 2, "name": "Conjuntos"},
        ]

        # Act
        wine_types_generator = WineTypes.all()

        # Assert
        for expected_wine_type, actual_wine_type in zip(expected_wine_types, wine_types_generator):
            self.assertDictEqual(expected_wine_type, actual_wine_type)


if __name__ == "__main__":
    unittest.main()
