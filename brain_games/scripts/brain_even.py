from brain_games.games import even_check_game
from brain_games.scripts import brain_games
from brain_games import cycle_of_rounds


def even_check():
    name = brain_games.greet()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    cycle_of_rounds.cycle_of_rounds(even_check_game.even_check_game, name)


def main():
    even_check()


if __name__ == "__main__":
    main()