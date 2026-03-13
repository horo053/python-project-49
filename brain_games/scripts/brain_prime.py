from random import randint
import prompt

def prime_number():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    count_correct_answers = 0

    for _ in range(3):
        number = randint(1, 100)
        print(f'Question: {number}')

        list_del = []
        del_num = number
        for _ in range(1, number):
            if number % del_num == 0:
                list_del.append(del_num)
            del_num -= 1

        if len(list_del) > 2:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'

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
    prime_number()


if __name__ == "__main__":
    main()