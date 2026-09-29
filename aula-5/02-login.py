# Login — senha valida
# Sem laço, sem lista, sem try. Nao peca senha real de ninguem.
#
# Regras:
# - senha vazia  ou  tamanho < 4: recusar com mensagem
# - senha com 4 ou mais caracteres e nao vazia: "acesso liberado"
#
# Use or (invalida) ou and (valida). not pode aparecer.
#
# Fronteira: "abcd" (4 letras) → libera. "abc" → recusa.
import sys

print("Login ficticio")
usuario = input("Usuario: ")
senha = input("Senha (ficticia): ")

if len(senha) == "" or len(senha) < 4:
    sys.exit("Senha vazia ou com menos de 4 caracteres possui parâmetro inválido")
else:
    print("Acesso liberado")