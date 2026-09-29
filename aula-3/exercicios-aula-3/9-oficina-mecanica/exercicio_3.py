print("Oficina do Python")

placa = input("Placa: ")
peca = input("Peca: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preco da peca: "))
mao_obra = float(input("Mao de obra: "))

pecas =  quantidade * preco
total =  pecas + mao_obra

print()
print("=" * 32)
print(f"Placa:     {placa}")
print(f"Peca:      {peca}")
print(f"Qtd:       {quantidade}")
print(f"Pecas:     R$ {pecas:.2f}")
print(f"Mao obra:  R$ {mao_obra:.2f}")
print("-" * 32)
print(f"TOTAL:     R$ {total:.2f}")
print("=" * 32)