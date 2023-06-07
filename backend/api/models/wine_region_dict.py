"""
Define the Wine Regions dict
"""


class WineRegions():
    def all():
        regions = [
            # Country: pt - Regions of Portugal
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
            # {"id": 15, "country": "pt", "name": "Minho"},
        ]

        for region in regions:
            yield region
