print("Caixa — troco")

nome = input("Item: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preco: "))
pago = float(input("Valor pago: "))

total =  quantidade * preco
troco =  pago - preco

print("=" * 30)
print(f"Item:  {nome}")
print(f"Total: R$ {total:.2f}")
print(f"Pago:  R$ {pago:.2f}")
print("-" * 30)
print(f"Troco: R$ {troco:.2f}")
print("=" * 30)