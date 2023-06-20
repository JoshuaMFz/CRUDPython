n1 = eval(input('Digite o primeiro número: '))
n2 = eval(input('Digite o segundo número: '))
n3 = eval(input('Digite o terceiro número: '))


if n1 > n2 and n1 > n3:
    print(f'O número 1 é o maior: {n1}')
    if n2 < n3:
        print(f'O número 2 é o menor: {n2}')
    elif n3 < n2:
        print(f'O número 3 é o menor: {n3}')
    elif n2 == n3:
        print(f'O número 2 e o 3 são iguais!')
    else:
        print(f'O número 1 e 3 são iguais')
elif n2 > n1 and n2 > n3:
    print(f'O número 2 é o maior: {n2}')
    if n1 < n3:
        print(f'O número 1 é o menor: {n1}')
    elif n3 < n1:
        print(f'O número 3 é o menor!: {n3}')
    elif n3 == n1:
        print(f'O número 3 e 1 são iguais!')
    else:
        print(f'O número 3 e 2 são iguais.')
elif n3 > n1 and n3 > n2:
    print(f'O número 3 é o maior: {n3}')
    if n1 < n2:
        print(f'O número 1 é o menor: {n1}')
    elif n2 < n1:
        print(f'O número 2 é o menor: {n2}')
    elif n1 == n2:
        print(f'O número 1 e 2 são iguais!')
    else:
        print(f'O número 1 e 3 são iguais!')
elif n1 < n2 and n2 == n3:
    print(f'O número 1 é o menor: {n1}')
    print(f'O número 2 e 3 são iguais!')
elif n2 < n1 and n1 == n3:
    print(f'O número 2 é o menor: {n2}')
    print(f'O número 1 e 3 são iguais!')
else:
    print(f'O número 3 é o menor: {n3}')
    print(f'O número 2 e 3 são iguais!')


