from brain_games.games import arithmetic_progression_game as apg
from brain_games.scripts import brain_games
from brain_games import cycle_of_rounds

def arithmetic_progression():
    name = brain_games.greet()

    print('What number is missing in the progression?')

    cycle_of_rounds.cycle_of_rounds(apg.arithmetic_progression_game, name)


def main():
    arithmetic_progression()


if __name__ == "__main__":
    main()