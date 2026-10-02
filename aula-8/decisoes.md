# Decisões — terminal da biblioteca

Preencha no papel antes de criar o `biblioteca.py`. Quatro respostas curtas. Se o desenho mudar no meio da aula, anote na margem.

Guia: [aula-08-guia.md](aula-08-guia.md).

---

## 1. Opções do menu

Quais opções aparecem, com número e texto?

Ficha de instruções:
Existem as matrículas para poder acessar a biblioteca:
20261302   José Andradas dos Santos CRÉDITO DO ESTUDANTE: 100
20261507   Eduardo Figueiredo       CRÉDITO DO ESTUDANTE: 100
20231202   Roberto Silveira         CRÉDITO DO ESTUDANTE: 100
20251500   Kaue Justos              CRÉDITO DO ESTUDANTE: 100
    Só serão aceitos estudantes já matriculados na faculdade vinculada. Não há como registrar alunos diretamente na biblioteca.

----------
PRIMEIRA MENSAGEM
_ mensagem: Bem vindo aluno!
input: Por favor identifique-se através do seu número de matrícula:
----------

ÍNDICE FIXO sempre que atualizar/utilizar algum código TUDO ISSO aparece:
                CABEÇALHO
    ESTANTE
    livros disponíveis:
    | Código | Título |
|--------|--------|
| `101` | Dom Casmurro |
| `102` | O Alienista |
| `103` | Capitães da Areia |
| `104` | Vidas Secas |
| `105` | O Cortiço |

                MEIO
AVISO: 
OS LIVROS x e y estão atrasados
OS LIVROS x e y vencem hoje
                
                FIM
texto= "TEXTO VARIÁVEL DE ACORDO COM INPUT"

Menu:
a_ pegar emprestado
b_ devolver
c_ consultar perfil

VOLTAR


-----------------------
CÓDIGOS:
 QUANDO ENTRA EM UM CÓDIGO DESAPARECE AS OUTRAS OPÇÕES E SÓ FICA ELA E "VOLTAR", APARECE SEMPRE UM INPUT NOVO PARA DIGITAR
a_ pegar emprestado
    input: qual livro você deseja pegar emprestado?
        mensagem: ok, não esqueça de devolvê-lo em 7 dias!
        Matrícula que já tem 2 livros em aberto não leva o terceiro.
        Livro que já saiu não empresta de novo.
        Código que não está no acervo não empresta.

b_ devolver
    input::Você possui os livros ["","",""] para devolver, digite o código do livro que você deseja entregar ou selecione TODOS:
        input: Você ainda possui os livros ["",""] que estão em ATRASO para devolver, digite o código do livro que você deseja entregar:
                input: para entregar o livro TAL é necessário pagar a multa de R$ x
                    pagar
                    voltar
                TODOS os livros que você tem atrasados somam uma multa de R$ x
                    pagar
                    voltar
    input: Você ainda possui os livros ["","",""] para devolver, digite o código do livro que você deseja entregar:
   
    mensagem: Você não possui livros para devolver

    - Livro que está na estante não devolve.

c_ perfil
PERFIL matrícula 20261302 - Nome TAL
AVISO: Possui/Não Possui os livros x,y.
       X precisa ser entregue em X dias! e Y está atrasado
CRÉDITO DO ESTUDANTE: 100

d_ sair

O resumo, ao sair, traz cinco números de todo o período em que o programa ficou aberto:

- quantos empréstimos aconteceram
- quantas devoluções
- quantos livros ainda estão fora
- quantos desses estão atrasados naquele dia
- quanto entrou de multa
Resumo: 1 empréstimo, 1 devolução, 0 fora, 0 atrasados, `R$ 2.00`.

biblioteca fecha e abre no próximo dia
Deseja reutilizar a matrícula digitada anteriormente?
        SIM
            Bem vindo de volta, nome_tal!
            Bem vindo aluno, nome_tal!

---

## 2. O que o programa lembra

Quando o menu volta, o que ainda precisa estar guardado? 
Dia 
livro = [nome, emprestado? s/n, emprestado para a matrícula TAL/matrícula vazia, codigo_livro]
matrícula = [nome, crédito do estudante, livros_emprestados[nome, dias usados, multa= s/n], TOTAL R$ MULTA, numero_matricula]

livros livres
empréstimos de cada matrícula
CRÉDITO DO ESTUDANTE
multas direcionadas a cada matrícula
o que mais a dupla decidir.

---

## 3. Recusas do empréstimo

Em que ordem você confere estas três perguntas: o código está no acervo? o livro já saiu? a matrícula já tem 2 livros em aberto?
já planejado na descrição dos CÓDIGOS

---

## 4. Prazo

Como você calcula que o prazo estourou?

Empréstimo no dia 1 está em dia até o dia 7. No dia 8 há 1 dia de atraso. No dia 9 há 2.
