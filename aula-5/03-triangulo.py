# Triangulo — tres lados
# Sem laço, sem lista, sem try.
#
# Tres numeros formam triangulo se cada lado e menor que a soma dos outros dois
# (as tres comparacoes, com and).
#
# Lado <= 0: recusar.
#
# Casos:
# 3, 4, 5 → forma
# 1, 2, 3 → nao forma (1+2 nao e maior que 3)
# 2, 2, 3 → forma (fronteira: 2+2 > 3)

import sys

print("Triangulo")

a = float((input("Lado a: ")))
b = float((input("Lado b: ")))
c = float((input("Lado c: ")))


if a <= 0 or b <= 0 or c <= 0:
    sys.exit()

soma = a + b
if soma >  c:
    print("Triângulo formado com êxito")
else:
    print(f"Lado a: {a} + lado b: {b} não é maior do que o lado c: {c}")
                

