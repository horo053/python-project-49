from random import randint
import prompt

def arithmetic_progression():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')

    count_correct_answers = 0

    for _ in range(3):
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

        print(f'Question: {progression}')

        user_answer = input('Your answer: ')

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
    arithmetic_progression()


if __name__ == "__main__":
    main()