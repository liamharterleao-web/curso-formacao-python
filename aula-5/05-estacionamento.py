# Estacionamento — tempo ou VIP
# Sem laço, sem lista, sem try.
#
# Regras:
# - minutos < 0: recusar
# - minutos <= 15  ou  vip == "s": estacionamento gratis
# - caso contrario: cobrar R$ 8.00
#
# Fronteira: 15 minutos (nao VIP) → gratis. 16 → R$ 8.00.

print("Estacionamento")
minutos = int(input("Minutos: "))
vip = input("Cliente VIP (s/n): ")

# complete: or, mensagem e valor
