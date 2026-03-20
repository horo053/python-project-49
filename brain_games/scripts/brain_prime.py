from brain_games.games import prime_number_game
from brain_games.scripts import brain_games
from brain_games import cycle_of_rounds

def prime_number():
    name = brain_games.greet()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    cycle_of_rounds.cycle_of_rounds(prime_number_game.prime_number_game, name)


def main():
    prime_number()


if __name__ == "__main__":
    main()