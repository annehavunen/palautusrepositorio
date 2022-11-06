import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_haku_toimii(self):
        pelaaja = self.statistics.search("Semenko")
        self.assertEqual(pelaaja.name, "Semenko")
    
    def test_haku_palauttaa_none_jos_nimea_ei_loydy(self):
        pelaaja = self.statistics.search("Olematon")
        self.assertEqual(pelaaja, None)

    def test_funktio_team_toimii(self):
        pelaajat = self.statistics.team("PIT")
        self.assertEqual(pelaajat[0].name, "Lemieux")

    def test_funktio_top_toimii_ilman_parametria(self):
        eniten_pisteita = self.statistics.top(1)
        self.assertEqual(eniten_pisteita[0].name, "Gretzky")

    def test_funktio_top_palauttaa_eniten_maaleja_tehneet(self):
        eniten_maaleja = self.statistics.top(1, SortBy.GOALS)
        self.assertEqual(eniten_maaleja[0].name, "Lemieux")

    def test_funktio_top_palauttaa_eniten_avustaneet(self):
        eniten_avustuksia = self.statistics.top(1, SortBy.ASSISTS)
        self.assertEqual(eniten_avustuksia[0].name, "Gretzky")
