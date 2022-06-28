#Exercício 5. Lidas duas matrizes quadradas de tamanho 4, X e Y, gere a matriz W, que corresponde ao produto de X por Y e a matriz Z, produto de Y por X.

matriz_a = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
matriz_b = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
matriz_c = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
matriz_d = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
aux = 0

for l in range(0,4):
    for c in range(0,4):
        matriz_a[l][c] = int(input(f'Digita os valores para a matriz X [{l}, {c}] = '))

print()

for l in range(0,4):
    for c in range(0,4):
        matriz_b[l][c] = int(input(f'Digita os valores para a matriz Y [{l}, {c}] = '))

print()

print('MATRIZ X')
for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz_a[l][c]}]', end = '')
    print()

print()

print('MATRIZ Y')
for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz_b[l][c]}]', end = '')
    print()

print()

print('A MULTIPLICAÇÃO ENTRE X E Y = MATRIZ W')
for l in range(0,4):
    for c in range(0,4):
        for x in range(0,4):
            aux += matriz_a[l][x] * matriz_b[x][c]
        matriz_c[l][c] = aux
        aux = 0

for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz_c[l][c]}]', end = '')
    print()

print()

print('A MULTIPLICAÇÃO ENTRE Y E X = MATRIZ Z')
for l in range(0,4):
    for c in range(0,4):
        for x in range(0,4):
            aux += matriz_b[l][x] * matriz_a[x][c]
        matriz_c[l][c] = aux
        aux = 0

for l in range(0,4):
    for c in range(0,4):
        print(f'[{matriz_c[l][c]}]', end = '')
    print()