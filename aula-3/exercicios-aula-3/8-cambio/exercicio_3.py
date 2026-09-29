print("Casa de cambio")

cliente = input("Cliente: ")
reais = float(input("Valor em reais: "))
cotacao = float(input("Cotacao (R$ por 1 USD): "))

dolares =  reais / cotacao

print("=" * 32)
print(f"Cliente: {cliente}")
print(f"Reais:   R$ {reais:.2f}")
print(f"Cotacao: {cotacao:.2f}")
print("-" * 32)
print(f"Dolares: US$ {dolares:.2f}")
print("=" * 32)
