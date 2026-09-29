print("Orcamento — pintura")

largura = float(input("Largura (m): "))
altura = float(input("Altura (m): "))
rendimento = float(input("M2 por litro: "))
preco_litro = float(input("Preco do litro: "))

area =  largura * altura
litros =  area / rendimento
custo =  litros * preco_litro

print("=" * 32)
print(f"Area:    {area:.2f} m2")
print(f"Litros:  {litros:.2f}")
print(f"TOTAL:   R$ {custo:.2f}")
print("=" * 32)

#Orcamento — pintura
#Largura (m): 4.5
#Altura (m): 2.8
#M2 por litro: 10
#Preco do litro: 32.90
#================================
#Area:    12.60 m2
#Litros:  1.26
#TOTAL:   R$ 41.45
#================================
