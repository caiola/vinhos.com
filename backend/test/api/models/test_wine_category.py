import unittest

from api.models.wine_category_dict import WineCategories


class TestWineCategories(unittest.TestCase):
    def test_all(self):
        # Arrange
        expected_categories = [
            {"id": 1, "main_category_id": None, "name": "Vinho"},
            {"id": 2, "main_category_id": None, "name": "Porto"},
        ]

        # Act
        wine_categories_generator = WineCategories.all()

        # Assert
        for expected_category, actual_category in zip(expected_categories, wine_categories_generator):
            self.assertDictEqual(expected_category, actual_category)


if __name__ == "__main__":
    unittest.main()
