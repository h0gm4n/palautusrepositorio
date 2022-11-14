
from playerreader import PlayerReader

class PlayerStats:

    def __init__(self, reader):
        self.reader = reader
        self.players = PlayerReader.get_players(reader)

    def top_scorers_by_nationality(self, nationality):

        def check_nationality(player):
            if player.nationality == nationality:
                return True
            return False

        nationality_iterator = filter(check_nationality, self.players)

        nationality_players = list(nationality_iterator)

        nationality_players.sort(key=lambda x: x.points, reverse=True)

        newlist = sorted(nationality_players, key=lambda x: x.points, reverse=True)

        return newlist

