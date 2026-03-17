from brain_games.games import even_check_game
import prompt


def even_check():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count_correct_answers = 0

    for _ in range(3):
        user_answer, correct_answer = even_check_game.even_check_game()

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
    even_check()


if __name__ == "__main__":
    main()