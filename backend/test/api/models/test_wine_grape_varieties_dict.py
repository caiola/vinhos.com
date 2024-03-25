import unittest

from api.models.wine_grape_variety_dict import WineGrapeVarieties


class TestWineGrapeVarieties(unittest.TestCase):
    def test_all(self):
        # Arrange
        expected_varieties = [
            {"id": 1001, "main_category_id": 1, "name": "Aglianico"},
            {"id": 1002, "main_category_id": 1, "name": "Aglianico del Vulture"},
            {"id": 1003, "main_category_id": 1, "name": "Alfrocheiro"},
        ]

        # Act
        wine_varieties_generator = WineGrapeVarieties.all()

        # Assert
        for expected_variety, actual_variety in zip(
            expected_varieties, wine_varieties_generator
        ):
            self.assertDictEqual(expected_variety, actual_variety)


if __name__ == "__main__":
    unittest.main()
