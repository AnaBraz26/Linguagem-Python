inicial = int(input("Numero de copias: "))

taxa = int(input("Taxa: "))

semanal = int(input("Numero de copias semanais: "))

i = 0

while(inicial < 1000000):	
        copias = inicial - (inicial * (taxa/100))		
        inicial = copias + semanal
        i = i + 1

print(i)
