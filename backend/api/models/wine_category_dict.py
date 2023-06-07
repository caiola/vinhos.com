"""
Define the Wine Category dict
"""


class WineCategories():
    def all():
        categories = [
            # Main categories
            {"id": 1, "main_category_id": None, "name": "Vinho"},
            {"id": 2, "main_category_id": None, "name": "Porto"},
            {"id": 3, "main_category_id": None, "name": "Whisky"},
            {"id": 4, "main_category_id": None, "name": "Generosos"},
            {"id": 5, "main_category_id": None, "name": "Destilados"},
            {"id": 6, "main_category_id": None, "name": "Bar"},
            {"id": 7, "main_category_id": None, "name": "Gourmet"},

            # Category: Vinho
            {"id": 101, "main_category_id": 1, "name": "Vinhos Portugueses"},
            {"id": 102, "main_category_id": 1, "name": "Vinhos Estrangeiros"},
            {"id": 103, "main_category_id": 1, "name": "Vinhos Monocasta"},
            {"id": 104, "main_category_id": 1, "name": "Vinhos Biológicos"},
            {"id": 105, "main_category_id": 1, "name": "Vinhos Vegan"},
            {"id": 106, "main_category_id": 1, "name": "Vinho de Talha"},
            {"id": 107, "main_category_id": 1, "name": "Colheita Tardia"},
            {"id": 108, "main_category_id": 1, "name": "Vinho de Curtimenta"},
            {"id": 109, "main_category_id": 1, "name": "Champagnes & Espumantes"},
            {"id": 110, "main_category_id": 1, "name": "Magnum & Superiores"},
            {"id": 111, "main_category_id": 1, "name": "Garrafas Únicas"},
            {"id": 112, "main_category_id": 1, "name": "Conjuntos"},
            {"id": 113, "main_category_id": 1, "name": "Bag in Box"},

            # Category: Porto
            {"id": 201, "main_category_id": 2, "name": "Porto Ruby"},
            {"id": 202, "main_category_id": 2, "name": "Porto Tawny"},
            {"id": 203, "main_category_id": 2, "name": "Porto Branco & Rosé"},
            {"id": 204, "main_category_id": 2, "name": "Vinho do Porto Biológico"},
            {"id": 205, "main_category_id": 2, "name": "Raridades"},
            {"id": 206, "main_category_id": 2, "name": "Porto Garrafeira"},
            {"id": 207, "main_category_id": 2, "name": "Miniaturas"},
            {"id": 208, "main_category_id": 2, "name": "Magnum & Superiores"},
            {"id": 209, "main_category_id": 2, "name": "Garrafas Únicas"},
            {"id": 210, "main_category_id": 2, "name": "Conjuntos"},

            # Category: Whisky
            {"id": 301, "main_category_id": 3, "name": "Whisky Escocês"},
            {"id": 302, "main_category_id": 3, "name": "Whisky Americano"},
            {"id": 303, "main_category_id": 3, "name": "Whisky Japonês"},
            {"id": 304, "main_category_id": 3, "name": "Whisky Irlandês"},
            {"id": 305, "main_category_id": 3, "name": "Novidades"},

            # Category: Generosos
            {"id": 401, "main_category_id": 4, "name": "Vinho da Madeira"},
            {"id": 402, "main_category_id": 4, "name": "Vinho Moscatel"},
            {"id": 403, "main_category_id": 4, "name": "Outros generosos"},

            # Category: Destilados
            {"id": 501, "main_category_id": 5, "name": "Aguardentes"},
            {"id": 502, "main_category_id": 5, "name": "Gin"},
            {"id": 503, "main_category_id": 5, "name": "Vodka"},
            {"id": 504, "main_category_id": 5, "name": "Rum"},
            {"id": 505, "main_category_id": 5, "name": "Absinto & Poteen"},
            {"id": 506, "main_category_id": 5, "name": "Tequila & Mezcal"},
            {"id": 507, "main_category_id": 5, "name": "Miniaturas"},
            {"id": 508, "main_category_id": 5, "name": "Magnum & Superiores"},
            {"id": 509, "main_category_id": 5, "name": "Garrafas Únicas "},
            {"id": 510, "main_category_id": 5, "name": "Conjuntos"},
            {"id": 511, "main_category_id": 5, "name": "Destilados Biológicos"},
            {"id": 512, "main_category_id": 5, "name": "Soju"},

            # Category: Bar
            {"id": 601, "main_category_id": 6, "name": "Bebidas"},
            {"id": 602, "main_category_id": 6, "name": "Acessórios vinho"},

            # Category: Gourmet
            {"id": 701, "main_category_id": 7, "name": "Azeites"},
            {"id": 702, "main_category_id": 7, "name": "Vinagres"},
            {"id": 702, "main_category_id": 7, "name": "Acessórios"}
        ]

        for category in categories:
            yield category
