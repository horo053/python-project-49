from random import randint


def prime_number_game():
    number = randint(1, 100)
    print(f'Question: {number}')

    list_del = []
    del_num = number
    for _ in range(1, number + 1):
        if number % del_num == 0:
            list_del.append(del_num)
        del_num -= 1

    if len(list_del) > 2:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'

    user_answer = input('Your answer: ')

    return correct_answer, user_answer