from random import randint
import prompt


def even_check():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count_correct_answers = 0

    for _ in range(3):
        number = randint(1, 100)
        print(f'Question: {number}')

        is_even = number % 2 == 0
        correct_answer = 'yes' if is_even else 'no'

        user_answer = input('Your answer: ')

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