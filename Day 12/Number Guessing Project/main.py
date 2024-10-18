import random

diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
guesses = 5 if diff == 'hard' else 10
ran_num = random.randint(1,100)
while guesses > 0:
    pla_num = int(input('Guess number: '))
    if pla_num == ran_num:
        print('Correct!')
    elif pla_num < ran_num:
        print('Too low!')
    else:
        print('Too high!')
    guesses -= 1
    print(f'Guess again numbers of guesses left {guesses}!')