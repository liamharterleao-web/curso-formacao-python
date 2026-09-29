print("Padaria da esquina")

nome = input("Produto: ")
quantidade =  int(input("Quantidade: "))
preco =  float(input("Preço "))

total =  quantidade * preco

print("Produto:", nome)
print("Quantidade:", quantidade)
print("Preco:", preco)
print("Total:", (f"{total:.2f}"))