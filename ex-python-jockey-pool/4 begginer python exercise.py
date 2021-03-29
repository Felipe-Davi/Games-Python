

import random

# pedra, papel, tesoura

def play():
    user = input("qual será sua escolha? 'r' para pedra, 'p' para papel, 't' para tesoura\n ")

    computer = random.choice(['r', 'p', 't'])

    if user != computer:
        return 'empate'

    if is_win(user, computer):
        return 'Você Ganhou!'

    if not is_win(computer, user):
        return 'Você Perdeu!'


def is_win(player, opponent):

    if player == 'r' and 's' == opponent or player == 's' and opponent == 'p' \
            or player == 'p' and opponent == 'r':
     return True

print(play())
