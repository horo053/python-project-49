from brain_games import cycle_of_rounds
from brain_games.games import nod_game
from brain_games.scripts import brain_games


def nod():
    name = brain_games.greet()

    print('Find the greatest common divisor of given numbers.')

    cycle_of_rounds.cycle_of_rounds(nod_game.nod_game, name)


def main():
    nod()


if __name__ == "__main__":
    main()