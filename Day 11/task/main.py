import os
import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


computer = []
player = []

playing = True
colorama_init()
computer_plays = True

def calc_score(arr):
    score = sum(arr)

    if (score > 21) and (11 in arr):
        arr[arr.index(11)] = 1
        score = calc_score(arr)

    return score

def draw_card(arr):
    arr.append(random.choice(cards))

def start_game(player1,player2):
    player1.clear()
    player2.clear()
    plays = True
    random.shuffle(cards)

    for i in range(2):
        plays = draw_card_computer(plays)
        draw_card(player2)

    return plays

def default_output():
    print(f'Your cards: {Fore.GREEN}{player}{Style.RESET_ALL}, current score: {Fore.GREEN}{calc_score(player)}{Style.RESET_ALL}')
    print(f'Computers first card: {Fore.RED}{computer[0]}{Style.RESET_ALL}')

def win_output(win,player_score,computer_score):
    print(f"Your final hand: {Fore.GREEN}{player}{Style.RESET_ALL}, final score: {Fore.GREEN}{player_score}{Style.RESET_ALL}\n"
          f"Computer's final hand: {Fore.RED}{computer}{Style.RESET_ALL}, final score: {Fore.RED}{computer_score}{Style.RESET_ALL}")

    if win == 'player':
        print(f'{Fore.GREEN}Your final hand wins!{Style.RESET_ALL}')

    elif win == 'computer':
        print(f'{Fore.RED}Computer wins!{Style.RESET_ALL}')

    elif win == 'draw':
        print(f'{Fore.YELLOW}draw{Style.RESET_ALL}')

def draw_card_computer(plays):
    if plays:
        draw_card(computer)

        if calc_score(computer) > 16:
            plays = False

    return plays

while True:
    user_input = input('Do you want to play a game of Blackjack? Type "y" or "n": ')

    if user_input != 'y':
        playing = False

    computer_plays = start_game(computer,player)

    default_output()
    while True:

        user_input = input(f"Type 'y' to get another card, type 'n' to pass: ")
        computer_plays = draw_card_computer(computer_plays)

        if user_input == 'y':
            draw_card(player)
            default_output()

        player_score = calc_score(player)

        computer_score = calc_score(computer)

        #Calculation of the winner:
        if (computer_plays and user_input == 'n') or (player_score == 21 or computer_score == 21) or player_score > 21:
            winner = ''

            if player_score == computer_score or (computer_score > 21 and player_score > 21):
                winner = 'draw'

            elif (computer_score == 21 or (computer_score > player_score) or player_score > 21) and computer_score <= 21:
                winner = 'computer'

            else:
                winner = 'player'

            win_output(winner, player_score, computer_score)
            break