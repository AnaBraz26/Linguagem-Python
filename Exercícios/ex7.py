#Exercício 7. Lido um número inteiro positivo m encontre o próximo número primo maior que 2m. 

m = int(input("Digite um número: "))
num = 2 * m
print(f"{m} x 2 = {num}")

while True:
    num = num + 1
    div = 0
    for n in range(1, num+1):
        if (num % n) == 0:
            div += 1
        else:
            print(end = '')

    if div > 2:
       print(end = '')
    else:
        print(f'O próximo número primo de {2 * m} é {num}')
        exit(True)
