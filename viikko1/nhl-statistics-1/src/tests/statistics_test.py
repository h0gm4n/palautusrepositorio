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
        self.search = self.statistics.search("Semenko")

        self.assertEqual(str(self.search), "Semenko EDM 4 + 12 = 16")


    def test_tiimihaku_toimii(self):
        self.teamsearch = self.statistics.team("EDM")

        self.assertEqual(len(self.teamsearch), 3)

    def test_sorttaus_toimii(self):

        self.sort = self.statistics.top(0)

        self.assertEqual(len(self.sort), 1)









