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
