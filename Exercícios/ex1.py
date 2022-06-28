#Exercício 1. Leia um número inteiro positivo e declare se ele é par ou ímpar.

numero = int(input("Digite um número: "))
if (numero%2) == 0:
    print('o numero {} é par'.format(numero))
else:
    print('o numero {} é ímpar'.format(numero))