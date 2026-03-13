from random import randint
import prompt

def nod():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')

    count_correct_answers = 0

    for _ in range(3):
        num1 = randint(1, 100)
        num2 = randint(1, 100)

        print(f'Question: {num1} {num2}')

        user_answer = input('Your answer: ')

        if num2 == 0:
            correct_answer = num1
        else:
            while num2 != 0:
                num1, num2 = num2, num1%num2
            correct_answer = num1

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
    nod()


if __name__ == "__main__":
    main()