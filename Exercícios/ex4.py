#Exercício 4. Lidos dois vetores A e B de tamanho 5, gere o vetor C, soma de A e B.

vetor_a = []
vetor_b = []
vetor_c = []
for a in range (0,5):
    vetor_a.append(int(input('Digite um numero para o vetor a: ')))

for b in range(0, 5):
    vetor_b.append(int(input('Digite um numero para o vetor b: ')))

for a,b in zip(vetor_a,vetor_b) :
    vetor_c.append(a + b)

print(f'\nEsse é o vetor A: ',end = '')
for a in vetor_a:
    print(f'{a}', end=' ')

print(f'\nEsse é o vetor B: ', end='')
for b in vetor_b:
        print(f'{b}', end=' ')

print(f'\nA soma dos vetores a e b é igual ao vetor c: ', end = '')
for c in vetor_c:
    print(f'{c}', end = ' ')

print('\n')