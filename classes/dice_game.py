import random


class DiceGame:
    def __init__(self, dices: int, games: int):
        self.dices = dices
        self.games = games

    def run_game(self):
        result = []
        for game in range(self.games):
            result.append(self.dices * random.randint(1, 6))
        return result




