from random import randint, choice

def calculation_game():
    list_symbol = ['-', '+', '*']
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

    return user_answer, correct_answer