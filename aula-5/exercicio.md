# Exercícios — Aula 5

O mesmo critério do `validador_pedido.py`: **duas condições** com `and`/`or` + fronteira. Onde houver opção nomeada, pode usar `match`/`case`. Sem laço, sem lista, sem `try`.

São **10** contextos. Na aula: priorize **1–4**; o restante é prática / recuperação / quem terminar cedo.

## O que entregar

Um `.py` por contexto, no VS Code. Ticket com `R$` e `:.2f` quando houver valor.

## Critério mínimo

- Pelo menos um `and` ou `or` de verdade (não dois `if` que fingem combinação).
- Fronteira escrita no papel antes de rodar.
- Mensagem quando a regra **não** aplica.

## Contextos

| # | Arquivo | Situação | Foco |
|---|---------|----------|------|
| 1 | [01-frete.py](01-frete.py) | Frete por peso **e** destino | `and` + fronteira |
| 2 | [02-login.py](02-login.py) | Senha: tamanho **e** não vazia | `or` / `and` / `not` |
| 3 | [03-triangulo.py](03-triangulo.py) | Três lados formam triângulo | três `and` |
| 4 | [04-meia-entrada.py](04-meia-entrada.py) | Meia só se estudante **e** idade | `and` |
| 5 | [05-estacionamento.py](05-estacionamento.py) | Grátis se tempo curto **ou** VIP | `or` |
| 6 | [06-loja-vip.py](06-loja-vip.py) | Desconto VIP **e** compra mínima | `and` + fronteira |
| 7 | [07-emprestimo.py](07-emprestimo.py) | Crédito: renda **e** score | `and` |
| 8 | [08-alerta-clima.py](08-alerta-clima.py) | Alerta se calor **e** chuva | `and` |
| 9 | [09-laboratorio.py](09-laboratorio.py) | Acesso: crachá **e** horário | `and` |
| 10 | [10-ingresso.py](10-ingresso.py) | Tipo de ingresso + idade mínima | `match` + `and` |
