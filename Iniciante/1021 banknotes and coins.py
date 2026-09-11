valor = float(input(""))
novo_valor = valor + 0.001

notas = [100,50,20,10,5,2]
moedas = [1,0.50,0.25,0.10,0.05,0.01]

print("NOTAS:")

for cada_nota in notas:
    quantidade = novo_valor // cada_nota
    novo_valor = novo_valor % cada_nota
    print(f"{quantidade:.0f} nota(s) de R$ {cada_nota:.2f}")

print("MOEDAS:")

for cada_moeda in moedas:
    quantidade_moeda = novo_valor // cada_moeda
    novo_valor = novo_valor % cada_moeda
    print(f"{quantidade_moeda:.0f} moeda(s) de R$ {cada_moeda:.2f}")