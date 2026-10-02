# Aula 8 — Terminal da biblioteca

A biblioteca da escola larga o caderno de empréstimos. Um atendente fica no terminal vários dias seguidos: empresta, devolve, consulta quem atrasou e olha a estante. Quando a biblioteca fecha, ele avança o calendário e continua no dia seguinte, no mesmo programa. O programa só termina quando ele pede o resumo e sai.

As regras abaixo são da casa. O desenho do programa é seu: quais opções aparecem no menu, em que ordem as perguntas vêm, e como o terminal lembra um empréstimo quando o menu volta.

---

## A casa

Cinco livros começam na estante, no dia 1.

| Código | Título |
|--------|--------|
| `101` | Dom Casmurro |
| `102` | O Alienista |
| `103` | Capitães da Areia |
| `104` | Vidas Secas |
| `105` | O Cortiço |

O aluno entra pela matrícula, um texto como `2024001`.

O dia da biblioteca começa em **1**. Avançar o dia soma 1 no calendário. Empréstimos, estante e multas continuam lá. O menu volta. Isso não encerra o programa: a biblioteca fechou naquele dia e abre no seguinte.

O prazo é de **7 dias**, contando o dia do empréstimo. Quem levou um livro no dia 1 devolve sem multa até o dia 7. No dia 8 já há **1** dia de atraso. Cada dia a mais soma outro dia.

A multa é **R$ 1,00 por dia de atraso** e só entra na devolução, com `R$` e duas casas. Consultar atraso mostra os dias; a cobrança fica para a hora de devolver.

Cada matrícula fica com no máximo **2** livros em aberto ao mesmo tempo.

---

## O que o atendente precisa fazer

O menu fica aberto. Você escolhe os números e os textos. Estas tarefas precisam existir no mesmo programa:

- Emprestar um livro para uma matrícula.
- Devolver um livro.
- Consultar quem está atrasado: matrícula, código, título e dias. Se ninguém estiver atrasado, uma frase deixa isso claro.
- Ver a estante: o que está disponível e o que está fora.
- Avançar o dia. O menu continua, com o mesmo acervo e os mesmos empréstimos.
- Sair. Aí sim o programa imprime o resumo de tudo o que aconteceu desde que abriu — mesmo que vários dias tenham passado — e termina.

Cada recusa diz o motivo:

- Código que não está no acervo não empresta.
- Livro que já saiu não empresta de novo.
- Matrícula que já tem 2 livros em aberto não leva o terceiro.
- Livro que está na estante não devolve.

O resumo, ao sair, traz cinco números de todo o período em que o programa ficou aberto:

- quantos empréstimos aconteceram
- quantas devoluções
- quantos livros ainda estão fora
- quantos desses estão atrasados naquele dia
- quanto entrou de multa

---

## Antes do código

Preencha [decisoes.md](decisoes.md) no papel. Quatro respostas curtas. Se o desenho mudar no meio do trabalho, anote a mudança na margem.

Só então crie `biblioteca.py` na pasta `aula-08`.

---

## Três situações para conferir

Cada caso começa de novo: dia 1, os cinco livros na estante, nenhum empréstimo.

### Caso 1 — limite e devolução no prazo

1. Empresta `101` para `2024001`.
2. Empresta `102` para a mesma matrícula.
3. Tenta emprestar `103` para a mesma matrícula. O programa recusa: já há 2 livros em aberto.
4. Devolve `101`. Sem multa.
5. A estante mostra `101` disponível e `102` fora.
6. Sai. O programa termina.

Resumo: 2 empréstimos, 1 devolução, 1 livro fora, 0 atrasados, `R$ 0.00`.

### Caso 2 — atraso

1. Empresta `103` para `2024002`.
2. Avança o dia até aparecer o **dia 9**.
3. Consulta atrasos: matrícula `2024002`, código `103`, título Capitães da Areia, **2** dias.
4. Devolve `103`. Multa `R$ 2.00`.
5. Sai. O programa termina.

Resumo: 1 empréstimo, 1 devolução, 0 fora, 0 atrasados, `R$ 2.00`.

### Caso 3 — recusas

Sem avançar o dia.

1. Empresta o código `999`. Recusa: não está no acervo.
2. Devolve `104`. Recusa: está na estante.
3. Empresta `101` para uma matrícula.
4. Empresta `101` de novo, para outra matrícula. Recusa: o livro já saiu.
5. Sai. O programa termina.

Resumo: 1 empréstimo, 0 devoluções, 1 fora, 0 atrasados, `R$ 0.00`. No dia 1 esse livro ainda está no prazo.

---

## Como saber se funcionou

- O menu volta depois de emprestar, devolver, consultar e avançar o dia. Avançar o dia deixa o programa aberto. Só sair termina.
- O caso 1 recusa o terceiro livro e a estante devolve o `101`.
- O caso 2 mostra 2 dias e cobra `R$ 2.00`.
- O caso 3 explica cada recusa, e o resumo fecha com um livro fora.
- Você conta o que o programa precisou lembrar entre uma opção e a seguinte.
