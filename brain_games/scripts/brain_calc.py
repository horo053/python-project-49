from random import randint, choice
import prompt

def calculation():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')

    list_symbol = ['-', '+', '*']

    count_correct_answers = 0

    for _ in range(3):
        num1 = randint(1, 100)
        num2 = randint(1, 100)

        symbol_operation = choice(list_symbol)
        print(f'Question: {num1} {symbol_operation} {num2}')

        user_answer = input('Your answer: ')

        correct_answer = 0

        match symbol_operation:
            case '-':
                correct_answer = num1 - num2
            case '+':
                correct_answer = num1 + num2
            case '*':
                correct_answer = num1 * num2

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