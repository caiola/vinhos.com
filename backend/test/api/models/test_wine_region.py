import unittest

from api.models.wine_region_dict import WineRegions


class TestWineRegions(unittest.TestCase):
    def test_all(self):
        # Arrange
        expected_regions = [
            {"id": 1, "country": "pt", "name": "Açores"},
            {"id": 2, "country": "pt", "name": "Alentejo"},
            {"id": 3, "country": "pt", "name": "Algarve"},
            {"id": 4, "country": "pt", "name": "Bairrada"},
            {"id": 5, "country": "pt", "name": "Beira Interior"},
            {"id": 6, "country": "pt", "name": "Dão"},
            {"id": 7, "country": "pt", "name": "Douro"},
            {"id": 8, "country": "pt", "name": "Lisboa"},
            {"id": 9, "country": "pt", "name": "Madeira"},
            {"id": 10, "country": "pt", "name": "Península de Setúbal"},
            {"id": 11, "country": "pt", "name": "Távora-Varosa"},
            {"id": 12, "country": "pt", "name": "Tejo"},
            {"id": 13, "country": "pt", "name": "Trás-os-Montes"},
            {"id": 14, "country": "pt", "name": "Vinho Verde"},
        ]

        # Act
        wine_regions_generator = WineRegions.all()

        # Assert
        for expected_region, actual_region in zip(expected_regions, wine_regions_generator):
            self.assertDictEqual(expected_region, actual_region)


if __name__ == "__main__":
    unittest.main()
