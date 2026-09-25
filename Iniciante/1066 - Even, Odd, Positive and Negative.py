numeros = [float(input()) for _ in range(5)]

positivo = 0
negativo = 0
pares = 0
impares = 0

for numero in numeros:

    if numero == 0:
        pares +=1

    if numero > 0:
        positivo +=1
        if numero % 2 == 0:
            pares +=1
        elif numero % 2 >= 1:
            impares +=1

    elif numero < 0:
        negativo += 1
        if numero % 2 == 0:
            pares +=1       
        else:
            impares +=1

print(f"{pares} valor(es) par(es)") 
print(f"{impares} valor(es) impar(es)") 
print(f"{positivo} valor(es) positivo(s)") 
print(f"{negativo} valor(es) negativo(s)") 