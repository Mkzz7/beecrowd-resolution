numeros = [float(input()) for _ in range(5)]

pares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
        
print(f"{pares} valores pares".lower())