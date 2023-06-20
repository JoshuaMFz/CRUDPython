'''
Crie um programa que faça o computador jogar pedra, papel tesoura com você.
'''

import random
from time import sleep


print('''Suas Opções: 
[0] - Pedra
[1] - Papel
[2] - Tesoura ''')

opt = int(input('Digite sua opção: '))
sleep(1)
print('-=' * 10)
print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO')
print('-=' * 10)

itens = ('Pedra', 'Papel', 'Tesoura')
optpc = random.randint(0, 2)

if opt == 0: #jogador jogou pedra
    print(f'Você jogou {itens[opt]}')
    if optpc == 0:
        print(f'O computador jogou {itens[optpc]}')
        print(f'\033[1:33mTemos um EMPATE!!!')
    elif optpc == 1:
        print(f'O computador jogou {itens[optpc]}')
        print(f'\033[1:31mVocê PERDEU!!!!')
    elif optpc == 2:
        print(f'O computador jogou {itens[optpc]}')
        print(f'\033[1:32mVocê GANHOU!!!')
elif opt == 1: # jogador jogou papel
    print(f'Você jogou {itens[opt]}')
    if optpc == 0:
        print(f'O computador jogou {itens[optpc]}')
        print(f'\033[1:32mVocê ganhou!!!!')
    elif optpc == 1:
        print(f'O computador jogou {itens[optpc]}')
        print(f'\033[1:33mTemos um EMPATE!!!!')
    elif optpc == 2:
        print(f'O computador jogou {itens[optpc]}')
        print(f'\033[1:31mVocê PERDEU!!!!')
elif opt == 2: #jogador jogou tesoura
    print(f'Você jogou TESOURA')
    if optpc == 0:
        print(f'O computador jogou {itens[optpc]}')
        print(f'\033[1:31mVocê perdeu!!!!')
    elif optpc == 1:
        print(f'O computador jogou {itens[optpc]}')
        print(f'\033[1:32mVocê GANHOU!!!!')
    elif optpc == 2:
        print(f'O computador jogou {itens[optpc]}')
        print(f'\033[1:33mTemos um EMPATE!!!!!!!')
else:
    print(f'Você escolheu uma opção inválida, tente novamente!')









