# Exercícios resolvidos da Lista1.

## 1.Alfabeto
Σ = {a, b, c}

1. 3 símbolos
2. a, b, c
3. Sim: a ∈ Σ.
4. Não: d ∉ Σ.
5. abc.

## 2.Palavras sobre um Alfabeto
Σ = {0, 1}

1. 0101 — válida, só tem símbolos de Σ.
2. 00110 — válida, só tem símbolos de Σ.
3. 012 — não válida, 2 não pertence ao alfabeto.
4. 111 — válida, só tem símbolos de Σ.
5. 10a — não válida, a não pertence ao alfabeto.

## 3.Pertinência de símbolos e palavras
Σ = {0, 1}

1. 0 ∈ Σ — verdadeiro.
2. 1 ∈ Σ — verdadeiro.
3. 01 ∈ Σ — falso, 01 é palavra e não símbolo do alfabeto.
4. 01 ∈ Σ* — verdadeiro.
5. 2 ∈ Σ — falso.
6. 101 ∈ Σ* — verdadeiro.

## 4.Linguagem
L = {0, 01, 011, 0111}

1. 0 ∈ L — sim.
2. 01 ∈ L — sim.
3. 0111 ∈ L — sim.
4. 10 ∈ L — não.
5. 111 ∈ L — não.
6. 011 ∈ L — sim.

## 5.Descrevendo uma linguagem por padrão

L = { bⁿ | n ≥ 1 }

1. b, bb, bbb, bbbb, bbbbb.
2. bⁿ significa n ocorrências do símbolo b.
3. Sim: bbbbbb = b⁶ e 6 ≥ 1.
4. Não: ε seria b⁰, e a condição exige n ≥ 1.

## 6.Linguagem vazia e palavra vazia

L = ∅ é uma linguagem sem nenhuma palavra.

L = {ε} é uma linguagem com uma palavra, a palavra vazia.

1. L = {ε} possui uma palavra.
2. L = ∅ não possui nenhuma palavra.
3. |ε| = 0.

Portanto ∅ ≠ {ε}.

## 7.Estrutura de uma gramática

G = ({S, A}, {0, 1}, P, S), com P = {S → 0A, A → 1}

1. V = {S, A}
2. T = {0, 1}
3. P = {S → 0A, A → 1}
4. S
5. 01

   S ⇒ 0A ⇒ 01

## 8.Como ler e aplicar uma produção

S → 0S

1. S ⇒ 0S
2. 0S ⇒ 00S
3. 00S ⇒ 000S
4. Sequência completa:

   S ⇒ 0S ⇒ 00S ⇒ 000S

A derivação não terminou: ainda existe o não terminal S.

## 9.Derivação completa de uma palavra

G: S → aS | b

Gerando aaab:

S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab

## 10.Identificando palavras geradas por uma gramática

G: S → 0S | 1

1. 1 — sim.

   S ⇒ 1

2. 01 — sim.

   S ⇒ 0S ⇒ 01

3. 001 — sim.

   S ⇒ 0S ⇒ 00S ⇒ 001

4. 0001 — sim.

   S ⇒ 0S ⇒ 00S ⇒ 000S ⇒ 0001

5. 101 — não. A produção S → 1 encerra a derivação, então o 1 só pode ser o
   último símbolo.
6. 1001 — não, pelo mesmo motivo.

L(G) = { 0ⁿ1 | n ≥ 0 }

## Desafio final

G: S → aS | b

1. b — sim.

   S ⇒ b

2. ab — sim.

   S ⇒ aS ⇒ ab

3. aab — sim.

   S ⇒ aS ⇒ aaS ⇒ aab

4. aaab — sim.

   S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaab

5. aba — não. A produção S → b consome o S e encerra a derivação, então nada
   pode ser escrito depois do b. Toda palavra da gramática termina em b.

6. Derivação completa de aaaab:

   S ⇒ aS ⇒ aaS ⇒ aaaS ⇒ aaaaS ⇒ aaaab

7. Padrão: uma quantidade qualquer de a (podendo ser nenhum), seguida de
   exatamente um b no final.

   L(G) = { aⁿb | n ≥ 0 }
