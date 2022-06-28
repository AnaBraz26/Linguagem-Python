#Exercício 3. Lidos 8 números reais crie um vetor e gere outro vetor na ordem inversa de entrada.

numeros = list()

for n in range(0,8):
    numeros.append(int(input('Digite um numero: ')))

print('Esse é o vetor original: ',end = ' ')
for n in numeros:
    print(f'{n}', end = ' ')

numeros.reverse()

print(f'\nEsse é o vetor invertido: ',end = '')
for n in numeros:
    print(f'{n}', end=' ')

print('\n')