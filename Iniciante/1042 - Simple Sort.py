x1, x2, x3 = map(int, input().split())
maior = 0
meio = 0
menor = 0
if x1 > x2 and x1 > x3:
    maior = x1
elif x2 > x1 and x2 > x3:
    maior = x2
else:
    maior = x3

if x1 < x2 and x1 < x3:
    menor = x1
elif x2 < x1 and x2 < x3:
    menor = x2
else:
    menor = x3

if (x1 != maior and x1 != menor):
    meio = x1
elif (x2 != maior and x2 != menor):
    meio = x2
else:
    meio = x3 



print(menor)
print(meio)
print(maior)
print()
print(x1)
print(x2)
print(x3)