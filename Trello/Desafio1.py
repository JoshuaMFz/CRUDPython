a = eval(input('Digite o valor de A: '))
b = eval(input('Digite o valor de B: '))
c = eval(input('Digite o valor de C: '))

#Fórmula de Delta: b² - 4.a.c

delta = (b ** 2) - (4 * a * c)

# Fórmula de Bhaskara: -b +- Raiz de Delta / 2.a

if delta < 0:
    print(f'Não é possível calcular os valores. O valor de delta é negativo: {delta}')
elif delta == 0:
    x = - b / (2 * a)
    print(f'O valor de X é: {x}')
else:
    raiz = int(delta ** 0.5)
    x1 = (- b + raiz) / (2 * a)
    print(f'O valor de x1 é: {x1}')
    x2 = (- b - raiz) / (2 * a)
    print(f'O valor de x2 é: {x2}')


