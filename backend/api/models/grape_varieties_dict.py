"""
Define the Status Type model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from .database import Database


class GrapeVarieties():

    def all(self):
        grape_varieties = {
            {"id": 1, "name": "Alfrocheiro"},
            {"id": 2, "name": "Alicante Bouschet"},
            {"id": 3, "name": "Alicante Branco"},
            {"id": 4, "name": "Alvarelhão"},
            {"id": 5, "name": "Alvarelhão-Ceitão"},
            {"id": 6, "name": "Alvarinho"},
            {"id": 7, "name": "Antão Vaz"},
            {"id": 8, "name": "Aragonês"},
            {"id": 9, "name": "Aramon"},
            {"id": 10, "name": "Arinto"},
            {"id": 11, "name": "Arinto dos Açores"},
            {"id": 12, "name": "Avesso"},
            {"id": 13, "name": "Azal Branco"},
            {"id": 14, "name": "Baga"},
            {"id": 15, "name": "Barcelo"},
            {"id": 16, "name": "Bastardo"},
            {"id": 17, "name": "Bical"},
            {"id": 18, "name": "Boal"},
            {"id": 19, "name": "Borraçal"},
            {"id": 20, "name": "Cabernet Sauvignon"},
            {"id": 21, "name": "Camarate"},
            {"id": 22, "name": "Carignan"},
            {"id": 23, "name": "Casculho"},
            {"id": 24, "name": "Castelão"},
            {"id": 25, "name": "Cerceal"},
            {"id": 26, "name": "Cerceal Branco"},
            {"id": 27, "name": "Cercial"},
            {"id": 28, "name": "Chardonnay"},
            {"id": 29, "name": "Chenin Blanc"},
            {"id": 30, "name": "Códega do Larinho"},
            {"id": 31, "name": "Cornifesto"},
            {"id": 32, "name": "Diagalves"},
            {"id": 33, "name": "Dona Branca"},
            {"id": 34, "name": "Donzelinho"},
            {"id": 35, "name": "Donzelinho Tinto"},
            {"id": 36, "name": "Dozelinho"},
            {"id": 37, "name": "Encruzado"},
            {"id": 38, "name": "Espadeiro"},
            {"id": 39, "name": "Fernão Pires"},
            {"id": 40, "name": "Folgasão"},
            {"id": 41, "name": "Fonte Cal"},
            {"id": 42, "name": "Galego Dourado"},
            {"id": 43, "name": "Gewürztraminer"},
            {"id": 44, "name": "Gonçalo Pires"},
            {"id": 45, "name": "Gouveio"},
            {"id": 46, "name": "Gouveio Real"},
            {"id": 47, "name": "Grand Noir"},
            {"id": 48, "name": "Greco di Tufo"},
            {"id": 49, "name": "Grenache"},
            {"id": 50, "name": "Jaen"},
            {"id": 51, "name": "Jampal"},
            {"id": 52, "name": "Loureiro"},
            {"id": 53, "name": "Malvasia"},
            {"id": 54, "name": "Malvasia Fina"},
            {"id": 55, "name": "Malvasia Preta"},
            {"id": 56, "name": "Malvasia Rei"},
            {"id": 57, "name": "Manteúdo"},
            {"id": 58, "name": "Maria Gomes"},
            {"id": 59, "name": "Marsanne"},
            {"id": 60, "name": "Marufo"},
            {"id": 61, "name": "Merlot"},
            {"id": 62, "name": "Moreto"},
            {"id": 63, "name": "Moscatel"},
            {"id": 64, "name": "Moscatel Galego"},
            {"id": 65, "name": "Moscatel Graúdo"},
            {"id": 66, "name": "Moscatel Roxo"},
            {"id": 67, "name": "Mourisco"},
            {"id": 68, "name": "Negra-Mole"},
            {"id": 69, "name": "Nevoeira"},
            {"id": 70, "name": "Olho de Lebre"},
            {"id": 71, "name": "Perrum"},
            {"id": 72, "name": "Petit Manseng"},
            {"id": 73, "name": "Petit Verdot"},
            {"id": 74, "name": "Petite Syrah"},
            {"id": 75, "name": "Pinot Blanc"},
            {"id": 76, "name": "Pinot Noir"},
            {"id": 77, "name": "Português Azul"},
            {"id": 78, "name": "Preto Martinho"},
            {"id": 79, "name": "Rabigato"},
            {"id": 80, "name": "Rabo de Ovelha"},
            {"id": 81, "name": "Ramisco"},
            {"id": 82, "name": "Riesling"},
            {"id": 83, "name": "Roupeiro"},
            {"id": 84, "name": "Rufete"},
            {"id": 85, "name": "Sauvignon Blanc"},
            {"id": 86, "name": "Sémillon"},
            {"id": 87, "name": "Sercial"},
            {"id": 88, "name": "Sercialinho"},
            {"id": 89, "name": "Síria"},
            {"id": 90, "name": "Sousão"},
            {"id": 91, "name": "Syrah"},
            {"id": 92, "name": "Tannat"},
            {"id": 93, "name": "Terrantez"},
            {"id": 94, "name": "Terrantez do Pico"},
            {"id": 95, "name": "Tinta Amarela"},
            {"id": 96, "name": "Tinta Barroca"},
            {"id": 97, "name": "Tinta Caiada"},
            {"id": 98, "name": "Tinta Carvalha"},
            {"id": 99, "name": "Tinta da Barca"},
            {"id": 100, "name": "Tinta Francisca"},
            {"id": 101, "name": "Tinta Grossa"},
            {"id": 102, "name": "Tinta Miúda"},
            {"id": 103, "name": "Tinta Negra"},
            {"id": 104, "name": "Tinta Pinheira"},
            {"id": 105, "name": "Tinta Pomar"},
            {"id": 106, "name": "Tinta Roriz"},
            {"id": 107, "name": "Tinto Cão"},
            {"id": 108, "name": "Touriga Fêmea"},
            {"id": 109, "name": "Touriga Franca"},
            {"id": 110, "name": "Touriga Nacional"},
            {"id": 111, "name": "Trajadura"},
            {"id": 112, "name": "Trincadeira"},
            {"id": 113, "name": "Trincadeira das Pratas"},
            {"id": 114, "name": "Uva-Cão"},
            {"id": 115, "name": "Verdelho"},
            {"id": 116, "name": "Verdelho dos Açores"},
            {"id": 117, "name": "Vinhão"},
            {"id": 118, "name": "Viognier"},
            {"id": 119, "name": "Viosinho"},
            {"id": 120, "name": "Vital"},
        }

        return grape_varieties