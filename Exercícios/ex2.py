#Exercício 2. Lidos 10 números declare o maior e o menor.

numeros = list()
for n in range(0,10):
    numeros.append(int(input('Digite um número: ')))

numeros.sort()
print('Maior número: {} Menor Número: {}'.format(numeros[9], numeros[0]))
