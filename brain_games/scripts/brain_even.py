from random import randint
import prompt


def parity_check():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    k = 0
    for i in range(3):
        number = randint(1, 100)
        print(f'Question: {number}')
        resp = input('Your answer: ')
        if number % 10 in (1, 3, 5, 7, 9) and resp == 'no':
            print('Correct!')
        elif number % 10 in (2, 4, 6, 8, 0) and resp == 'yes':
            print('Correct!')
        else:
            if resp == 'no':
                print('\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
            else:
                print('\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
            print(f'Let\'s try again, {name}!')
            break
        k += 1
    if k == 3:
        print(f'Congratulations, {name}!')


def main():
    parity_check()


if __name__ == "__main__":
    main()