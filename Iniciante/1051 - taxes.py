salario = float(input())
taxa = 0
valor_taxa = (salario * taxa)

if 0.00 <= salario <= 2000.00:
    print("Isento")
elif 2000.01 <= salario <= 3000.00:
    taxa = 0.08
    valor_taxa = (salario - 2000) * taxa
    print(f"R$ {valor_taxa:.2f}")
elif 3000.01 <= salario <= 4500.00:
    taxa = 0.18
    valor_taxa = (salario - 3000) * taxa + (1000 * 0.08)
    print(f"R$ {valor_taxa:.2f}")
elif salario > 4500.00:
    taxa = 0.28
    valor_taxa = (salario - 4500) * taxa + (1500 * 0.18) + (1000 * 0.08)
    print(f"R$ {valor_taxa:.2f}")