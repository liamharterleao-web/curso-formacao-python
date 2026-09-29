print("Cine Python")

tipo = input("Tipo (inteira/meia): ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preco: "))

total =  quantidade * preco

print("=" * 28)
print(f"Tipo: {tipo}")
print(f"Qtd:  {quantidade}")
print(f"Unitario: R$ {preco:.2f}")
# complete: TOTAL com R$ e duas casas
print(f"TOTAL: R$ {total:.2f}")
print("=" * 28)