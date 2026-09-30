# Alerta clima — calor e chuva
# Sem laço, sem lista, sem try.
#
# Regras:
# - temperatura >= 30  e  chuva == "s": "alerta: risco de temporal quente"
# - temperatura >= 30  e  chuva == "n": "calor seco"
# - temperatura < 30  e  chuva == "s": "chuva sem calor extremo"
# - senao: "tempo estavel"
#
# Fronteira: 30.0 com chuva → alerta. 29.9 com chuva → chuva sem calor.

print("Alerta clima")
temperatura = float(input("Temperatura (C): "))
chuva = input("Chuva (s/n): ")

# complete: and, quatro caminhos com mensagem
if temperatura >= 30 and chuva == "s":
    print("alerta: risco de temporal quente")
elif temperatura >= 30 and chuva == "n":
    print("calor seco")
elif temperatura < 30 and chuva == "s":
    print("chuva sem calor extremo")
else:
    print("tempo estável")