# Estacionamento — tempo ou VIP
# Sem laço, sem lista, sem try.
#
# Regras:
# - minutos < 0: recusar
# - minutos <= 15  ou  vip == "s": estacionamento gratis
# - caso contrario: cobrar R$ 8.00
#
# Fronteira: 15 minutos (nao VIP) → gratis. 16 → R$ 8.00.
import sys
print("Estacionamento")
minutos = int(input("Minutos: "))
if minutos < 0 :
    sys.exit("Valor de minutos INVÁLIDO")
vip = input("Cliente VIP (s/n): ")
if minutos <= 15 or vip == "s":
    print("Estacionamento gratuito")
else:
    print("Valor do estacionamento: R$ 8,00")