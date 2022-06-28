#8. Dada uma matriz 8x8 vazia, distribua aleatoriamente um rei branco (R) e um rei negro (r),
#com a condição deles não estarem em casas contíguas, isto é, tem que haver pelo menos uma
#casa vazia entre eles.

import random

matriz = []

for l_R in range(8):
    linha = []
    for c_R in range(8):
      linha.append(0)
    matriz.append(linha)

l_R = random.randint(0, 7)
c_R = random.randint(0, 7)
matriz[l_R][c_R] = 'r'

l_R = random.randint(0, 7)
c_R = random.randint(0, 7)
matriz[l_R][c_R] = 'R'

for l_R in range(0,7):
    for c_R in range(0,7):
        if matriz[l_R][c_R] == 'r':
            if (matriz[l_R - 1][c_R] == 0 and matriz[l_R - 1][c_R - 1] == 0 and matriz[l_R - 1][c_R - 1] == 0 and matriz[l_R + 1][c_R] == 0
            and matriz[l_R + 1][c_R + 1] == 0 and matriz[l_R + 1][c_R - 1] == 0 and matriz[l_R][c_R + 1] == 0 and matriz[l_R][c_R - 1] == 0):
                break
            else:
                matriz[l_R - 1][c_R] = 0
                matriz[l_R - 1][c_R - 1] = 0
                matriz[l_R - 1][c_R - 1] = 0
                matriz[l_R + 1][c_R] = 0
                matriz[l_R + 1][c_R + 1] = 0
                matriz[l_R + 1][c_R - 1] = 0
                matriz[l_R][c_R + 1] = 0
                matriz[l_R][c_R - 1] = 0
                l_R = random.randint(0, 8)
                c_R = random.randint(0, 8)
                print(f'{l_R},{c_R}')
                matriz[l_R][c_R] = 'R'


for l_R in range(8):
    for c_R in range(8):
        print(f'[{matriz[l_R][c_R]}]', end = '')
    print()
