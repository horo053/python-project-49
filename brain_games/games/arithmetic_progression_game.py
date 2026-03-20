from random import randint
from typing import Any


def arithmetic_progression_game():
    start = randint(1, 25)
    index = randint(5, 10)
    step = randint(2, 8)
    progression = []

    for _ in range(index):
        k = start + index * step
        start += step
        progression.append(k)

    len_progression = len(progression)
    index_num = randint(0, len_progression - 1)
    correct_answer = progression[index_num]
    progression[index_num] = '..'

    print(f'Question:', *progression)

    user_answer = input('Your answer: ')

    return correct_answer, user_answer