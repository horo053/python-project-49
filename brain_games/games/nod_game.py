from random import randint

def nod_game():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    print(f'Question: {num1} {num2}')

    user_answer = input('Your answer: ')

    if num2 == 0:
        correct_answer = num1
    else:
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        correct_answer = num1

    return user_answer, correct_answer