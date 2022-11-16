import requests
from player import Player


class PlayerReader:
    def __new__(cls, url):
        response = requests.get(url).json()
        players = []
        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['team']
            )
            players.append(player)
        return players

class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        top_scorers = sorted(self.players, key=lambda player : player.assists + player.goals, reverse=True)
        filtered_top_scorers = filter(lambda player : player.nationality == nationality, top_scorers)
        return filtered_top_scorers

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
