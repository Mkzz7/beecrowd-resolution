numero = int(input(""))

anos = numero // 365

sobra = numero % 365

meses = sobra // 30

dias = sobra % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")