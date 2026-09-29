print("Hotel Sabor e Travesseiro")

hospede = input("Nome do hospede: ")
diarias = int(input("Diarias: "))
valor_diaria = float(input("Valor da diaria: "))
taxa = float(input("Taxa de turismo: "))

hospedagem =  diarias * valor_diaria
total =  hospedagem + taxa

print()
print("=" * 32)
print(f"Hospede:    {hospede}")
print(f"Diarias:    {diarias}")
print(f"Diaria:     R$ {valor_diaria:.2f}")
print(f"Hospedagem: R$ {hospedagem:.2f}")
print(f"Taxa:       R$ {taxa:.2f}")
print("-" * 32)
print(f"TOTAL:      R$ {total:.2f}")
print("=" * 32)