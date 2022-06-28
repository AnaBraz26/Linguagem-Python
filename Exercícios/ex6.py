#Exercício 6. Lido um vetor (array) de n elementos verifique se há elementos repetidos.
# Se não houver repetição escreva “Certo”, caso contrário escreva “Há repetição”.

vetor = []

n = int(input('Quantos elementos vão ter no vetor = '))

for a in range(0,n):
    vetor.append(int(input('Digite um valor: ')))

vetor.sort()

for a in vetor:
    print(f'{a}', end=' ')

print()

for a in range(0, n-1):
    if vetor[a] != vetor[a+1]:
        print(end = '')
    else:
        print('Há repetição')
        exit(True)

print('Certo')
