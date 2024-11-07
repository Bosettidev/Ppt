import random
import os
import time

os.system('clear')

def jogo():
    list = ['pedra', 'papel', 'tesoura']
    comp = random.choice(list)

    player = input('Escolha pedra, papel ou tesoura: ')

    while player != 'pedra' and player != 'papel' and player != 'tesoura':
        os.system('clear')
        player = input('Escolha pedra, papel ou tesoura: ')

    if player == 'pedra' and comp == 'papel':
        print('O computador escolheu papel, você perdeu!')
        time.sleep(1)
        os.system('clear')
    elif player == 'pedra' and comp == 'tesoura':
        print('O computador escolheu tesoura, você ganhou!')
        time.sleep(1)
        os.system('clear')
    elif player == 'papel' and comp == 'pedra':
        print('O computador escolheu pedra, você ganhou!')
        time.sleep(1)
        os.system('clear')
    elif player == 'papel' and comp == 'tesoura':
        print('O computador escolheu tesoura, você perdeu!')
        time.sleep(1)
        os.system('clear')
    elif player == 'tesoura' and comp == 'pedra':
        print('O computador escolheu pedra, você perdeu!')
        time.sleep(1)
        os.system('clear')
    elif player == 'tesoura' and comp == 'papel':
        print('O computador escolheu papel, você ganhou!')
        time.sleep(1)
        os.system('clear')
    else:
        print('Empate!')
        time.sleep(1)
        os.system('clear')

jogo()

dnv = input('Deseja jogar novamente? (s/n) ')

if dnv == 's':
    os.system('clear')
    jogo()
else:
    os.system('clear')
    print('Obrigado por jogar!')
    breakpoint

if __name__ == '__main__':
    jogo()