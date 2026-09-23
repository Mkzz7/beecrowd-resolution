numeros = [float(input()) for _ in range(6)]

positivos = 0

for numero in numeros:
    if numero > 0:
        positivos += 1
        
print(f"{positivos} valores positivos")