from brain_games.games import calculation_game
from brain_games.scripts import brain_games
from brain_games import cycle_of_rounds

def calculation():
    name = brain_games.greet()

    print('What is the result of the expression?')

    cycle_of_rounds.cycle_of_rounds(calculation_game.calculation_game, name)


def main():
    calculation()


if __name__ == "__main__":
    main()