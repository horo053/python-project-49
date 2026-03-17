from brain_games.games import calculation_game
from brain_games.scripts import brain_games

def calculation():
    name = brain_games.greet()

    print('What is the result of the expression?')

    count_correct_answers = 0

    for _ in range(3):
        user_answer, correct_answer = calculation_game.calculation_game()

        if int(user_answer) == int(correct_answer):
            print('Correct!')
            count_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f'Let\'s try again, {name}!')
            break

    if count_correct_answers == 3:
        print(f'Congratulations, {name}!')


def main():
    calculation()


if __name__ == "__main__":
    main()