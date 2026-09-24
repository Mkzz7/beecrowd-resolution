numeros = [float(input()) for _ in range(6)]

positivos = 0
lista_media= []
for numero in numeros:
    if numero > 0:
        positivos += 1
        lista_media.append(numero)


media = sum(lista_media) / len(lista_media)
print(f"{positivos} valores positivos")
print(f"{media:.1f}")
        
