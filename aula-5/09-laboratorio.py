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
import sys

print("Acesso laboratorio")
cracha = input("Cracha valido (s/n): ")
if cracha == "n":
    print("Cracha obrigatorio")
hora = int(input("Hora atual (0-23): "))

# complete: and, mensagens
if hora < 0 or hora > 23:
    sys.exit(("Recusado"))
elif cracha == "s" and hora >= 8 and hora < 18:
    print("Acesso liberado")
else:
    print("Fora do expediente")