import requests
from player import Player
from playerreader import PlayerReader
from playerstats import PlayerStats
import datetime

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)


main()