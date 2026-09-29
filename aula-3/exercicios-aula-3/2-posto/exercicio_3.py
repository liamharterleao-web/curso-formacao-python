print("Posto Sabor e Pista")

combustivel = input("Combustivel: ")
litros =  float(input("Litros: "))
preco =  float(input("Preço: "))

total =  float(litros * preco)

print("=" * 28)
print(f"Combustivel: {combustivel}")
print(f"Litros:      {litros}")
# complete: preco e total com R$ e :.2f
print("Preço:    R$ ", preco)
print(f"Total:    R$ {total:.2f}")
print("=" * 28)
