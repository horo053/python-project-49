def cycle_of_rounds(func_game, name):
    count_correct_answers = 0

    for _ in range(3):
        user_answer, correct_answer = func_game()

        if int(user_answer) == int(correct_answer):
            print('Correct!')
            count_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break

    if count_correct_answers == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f'Let\'s try again, {name}!')