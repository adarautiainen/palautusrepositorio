import requests


class Player:
    def __init__(self, pdict):
        self.name = pdict['name']
        self.team = pdict['team']
        self.nationality = pdict['nationality']
        self.goals = pdict['goals']
        self.assists = pdict['assists']
        self.sumofpoints = self.goals + self.assists

    def __str__(self):
        return f"{self.name} team {self.team}    {self.goals}+{self.assists} = {self.sumofpoints}"


class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()
        return [Player(pdict) for pdict in response]


class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        finnish = [player for player in self.players if player.nationality == nationality]
        for pl in finnish:
            pl.sumofpoints = pl.goals + pl.assists
        return sorted(finnish, key=lambda pl: pl.sumofpoints, reverse=True)


