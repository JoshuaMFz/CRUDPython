

# class Computador:
#     def __init__(self, marca, valor, memoria):
#         self.marca = marca
#         self.valor = valor
#         self.memoria = memoria
#
#     def Desligar(self):
#         print('Estou desligando')
#
#     def Ligar(self):
#         print('Estou ligando')
#
#     def Info(self):
#         print(self.marca, self.memoria, self.valor)
#
# computador1 = Computador('Asus', 'R$ 3,000', '8GB')
#
# computador1.Desligar()

#Exercício

from random import randint

class Carro:
    def __init__(self, cor, chassi, modelo):
        self.cor = cor
        self.chassi = chassi
        self.modelo = modelo

    def Ligar(self):
        print('Ligando o carro!')

    def Desligar(self):
        print('Desligando o carro')

    def Andar(self):
        print('Estou me locomovendo.')

carro1 = Carro('Azul', randint(123123, 999999), 'Gol Rebaixado')
print(carro1.chassi, carro1.cor, carro1.modelo)

