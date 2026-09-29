# Laboratorio — cracha e horario
# Sem laço, sem lista, sem try.
#
# Regras:
# - hora < 0 ou hora > 23: recusar
# - cracha == "s"  e  hora >= 8  e  hora < 18: "acesso liberado"
# - cracha "s" fora do horario: "fora do expediente"
# - sem cracha: "cracha obrigatorio"
#
# Fronteira: cracha s e hora 8 → libera. Hora 18 → fora do expediente.
#            Hora 17 → libera.

print("Acesso laboratorio")
cracha = input("Cracha valido (s/n): ")
hora = int(input("Hora atual (0-23): "))

# complete: and, mensagens
