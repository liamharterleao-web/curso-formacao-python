print("Caderneta — um item")

nome = input("Nome do item: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preco unitario: "))

total = quantidade * preco

print()
print("=" * 32)
print("LANCHONETE SABOR E CODIGO")
print("=" * 32)
print(f"Item:     {nome}")
print(f"Qtd:      {quantidade}")
print(f"Unitário: {preco:.2f}")
print(f"TOTAL:    {total:.2f}")
print
# complete: unitário com R$ e duas casas
print()
print("-" * 32)
# complete: TOTAL com R$ e duas casas
print()
print("=" * 32)