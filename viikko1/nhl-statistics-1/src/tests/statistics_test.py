import unittest
from statistics import Statistics
from player import Player

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

        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_toimii(self):
        self.search = self.statistics.search("S")

        self.assertEqual(str(self.search), "Semenko EDM 4 + 12 = 16")









