salario = float(input(""))
def calcular_porcentagem(salario, percentual):
    aumento = salario * percentual
    novo_salario = salario + aumento
    print(f"Novo salário: {novo_salario:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print(f"Em percentual: {(percentual * 100):,.0f} %")

if 0 <= salario <= 400:
    calcular_porcentagem(salario, 0.15)
elif 400.01 <= salario <= 800:
    calcular_porcentagem(salario, 0.12)
elif 800.01 <= salario <= 1200:
    calcular_porcentagem(salario, 0.10)
elif 1200.01 <= salario <= 2000:
    calcular_porcentagem(salario, 0.07)
elif salario > 2000:
    calcular_porcentagem(salario, 0.04)