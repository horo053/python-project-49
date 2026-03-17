from random import randint

def even_check_game():
    number = randint(1, 100)
    print(f'Question: {number}')

    is_even = number % 2 == 0
    correct_answer = 'yes' if is_even else 'no'

    user_answer = input('Your answer: ')

    return correct_answer, user_answer