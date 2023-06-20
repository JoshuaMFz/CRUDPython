# def função ():
#     print('Hello World!')
#
# função()

# Repetir o mínimo no código.

# def saudacao(msg='Olá', nome='Usuário'):
#     msg = msg.replace('a', '4')
#     nome = nome.replace('a', '4')
#     return f'{msg}, {nome}'
#
# variavel = saudacao('Oi', 'Joshua')
#
# print(variavel)

# def func(*args): - Usar o *args quando não souber quantos argumentos vai utilizar.
#     print(args)

# def func(*args):
#     print(args)
#
# lista = [1, 2, 3, 4, 5]
# n1, n2, *n = lista #Tirando o 1, 2 e desempacotando o resto.
# print(n1, n2, n)
# O primeiro args [0] o último args[-1]
# Quantidade len(args)

def func(*args, **kwargs):
    print(args)
    print(kwargs)
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')

lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]

func(*lista1, *lista2, nome='Jóshua', sobrenome='Martins', idade= 30)



