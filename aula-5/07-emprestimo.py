# Emprestimo — renda e score
# Sem laço, sem lista, sem try. Valores ficticios.
#
# Regras:
# - renda <= 0 ou score < 0: recusar
# - renda >= 2000  e  score >= 600: "aprovado"
# - caso contrario: "negado" com mensagem (renda baixa, score baixo ou ambos)
#
# Fronteira: renda 2000 e score 600 → aprovado.
#            renda 2000 e score 599 → negado.

print("Emprestimo ficticio")
renda = float(input("Renda mensal: "))
score = int(input("Score de credito: "))

# complete: and / or, mensagens
