# Jogo pedra papel tesoura, com as entradas do USUÁRIO.

print('''Olá jogadores, sejam bem-vindos ao jogo chamado: JOKENPÔ. Suas opções podem ser: 
[1] = Papel
[2] = Pedra
[3] = Tesoura
''')

jogador1 = int(input('Ola, Jogador 1. Escolha sua opção: '))
jogador2 = int(input('Olá, Jogador 2. Escolha sua opção: '))

if jogador1 == 1 and jogador2 == 1:
    print('Temos um EMPATE!')
elif jogador1 == 1 and jogador2 == 2:
    print('O Jogador1 venceu! Papel encobre pedra.')
elif jogador1 == 1 and jogador2 == 3:
    print('O Jogador2 venceu! Tesoura corta papel.')
elif jogador1 == 2 and jogador2 == 1:
    print('O Jogador2 venceu! Papel encobre pedra')
elif jogador1 == 2 and jogador2 == 2:
    print('Temos um EMPATE!')
elif jogador1 == 2 and jogador2 == 3:
    print('O Jogador1 venceu! Pedra quebra tesoura.')
elif jogador1 == 3 and jogador2 == 1:
    print('O Jogador1 venceu! Tesoura corta papel')
elif jogador1 == 3 and jogador2 == 2:
    print('O Jogador2 venceu! Pedra quebra tesoura')
elif jogador1 == 3 and jogador2 == 3:
    print('Temos um EMPATE!')
else:
    print('Opção inválida, tente novamente!')






