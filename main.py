import matplotlib.pyplot as plt
from classes.dice_game import DiceGame
from collections import Counter

if __name__ == '__main__':
    statistics1 = []
    statistics2 = []
    statistics3 = []
    game = DiceGame(1, 1)
    games = 1000
    counter = 0
    while games > 0:
        games -= 1
        counter += 1
        player1 = game.run_game()
        player2 = game.run_game()
        player3 = game.run_game()
        statistics1.append(player1[0])
        statistics2.append(player2[0])
        statistics3.append(player3[0])

    counter1 = Counter(statistics1)
    results1 = []
    for key, value in counter1.items():
        results1.append((key, value))

    testlist2 = [(elem2, elem1) for elem1, elem2 in results1]
    # testlist3 = [(elem2, elem1[0]) for elem1, elem2 in statistics2]
    # testlist4 = [(elem2, elem1[0]) for elem1, elem2 in statistics3]
    plt.figure(figsize=(20, 20))
    plt.subplot(131)
    lines = plt.scatter(*zip(*results1))
    # plt.subplot(132)
    # lines2 = plt.scatter(*zip(*testlist3))
    # plt.subplot(133)
    # lines3 = plt.scatter(*zip(*testlist4))
    plt.show()
