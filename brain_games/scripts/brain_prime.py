from brain_games.games import prime_number_game
from brain_games.scripts import brain_games

def prime_number():
    name = brain_games.greet()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count_correct_answers = 0

    for _ in range(3):
        user_answer, correct_answer = prime_number_game.prime_number_game()

        if user_answer == correct_answer:
            print('Correct!')
            count_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            break

    if count_correct_answers == 3:
        print(f'Congratulations, {name}!')


def main():
    prime_number()


if __name__ == "__main__":
    main()