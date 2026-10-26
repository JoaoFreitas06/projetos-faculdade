# Atividade sobre agentes inteligentes

Aula 19/10/2026 | Professora Kadidja Valéria | Inteligência artificial

**Disciplina:** Inteligência Artificial, Linguagens Formais e Autômatos

**Estudante:** João Vitor de Freitas | **Turma:** N1

Realize os exercícios 2.3, 2.4 e 2.5 do Capítulo 2 sobre agentes inteligentes. Analise a racionalidade, descreva ambientes de tarefa por meio do modelo PEAS e explique os conceitos com suas próprias palavras. Utilize o capítulo disponibilizado e justifique suas respostas.

**Modalidade sugerida:** individual com consulta. **Tempo estimado:** 2h30. **Prazo:** conforme orientação da professora.

## Preparação
Leia os tópicos sobre racionalidade, ambientes e estrutura dos agentes, especialmente a Seção 2.3.2.

## Exercício 2.3
Para cada afirmação, indique V ou F, justifique e forneça exemplo ou contraexemplo. Explicite as hipóteses utilizadas.

### a. Um agente que detecta apenas informações parciais sobre o estado não pode ser perfeitamente racional.

- Julgamento: F
- Justificativa: Mesmo tendo apenas as informações parciais, ele ainda tem a racionaliade do que ele ja absorveu de informações. Assim, mesmo com a informação inconpleta, ele ainda pode escolher a melhor proxima ação com o que ja tem.
- Exemplo ou contraexemplo: Um medico que decide qual o medicamento dar para o paciente mesmo não tendo todos os exames necessarios para realizar o diagnostico certeiro, ele ira passar o remedio com mais chance de melhora.

### b. Existem ambientes de tarefa nos quais nenhum agente reativo puro pode comportar-se racionalmente.

- Julgamento: V
- Justificativa: Como e um agente reativo puro, ele não tem memoria, então em algum ambiente que necessite disso ele pode falhar.
- Exemplo ou contraexemplo: Um explorador que tem que desbravar 3 caminhos diferentes, um de cada vez, mas a cada caminho que ele vai, ele so lembra dele, pois não lembra dos anteriores (tipo um alzheimer).

### c. Existe um ambiente de tarefa em que todo agente é racional.

- Julgamento: V
- Justificativa: se todas as ações dão o mesmo desempenho, nenhuma e melhor que outra, então qualquer escolha vai ser a melhor possivel.
- Exemplo ou contraexemplo: Um jogo que toda a jogada gera a mesma pontuação, Nenhuma jogada ira ser melhor que a outra.

### d. A entrada para o programa de agente é a mesma que a entrada para a função de agente.

- Julgamento: F
- Justificativa: a função recebe a sequência completa de percepções, o programa recebe apenas a percepção atual. Se precisar do histórico, o programa deve armazená-lo.
- Exemplo ou contraexemplo: IA de conversa. A função considera a conversa inteira, o programa recebe só a mensagem atual e precisa guardar o histórico em uma variável.

### e. Toda função de agente é implementável por uma combinação de programa/máquina.

- Julgamento: F
- Justificativa: a máquina tem memória e tempo finitos. Funções que exigem recursos ilimitados (ou que não da pra programar) não podem ser implementadas.
- Exemplo ou contraexemplo: agente de xadrez perfeito feito por tabela com todas as sequências de percepções. A tabela teria mais entradas do que cabe em qualquer computador.

### f. Suponha que um agente selecione sua ação uniformemente ao acaso do conjunto de ações possíveis. Existe um ambiente de tarefa determinista em que esse agente é racional.

- Julgamento: V
- Justificativa: se todas as ações levam ao mesmo desempenho, escolher na sorte e tão bom quanto qualquer outra.
- Exemplo ou contraexemplo: porta que abre com qualquer um de dois botões. Escolher ao acaso funciona tão bem quanto qualquer outro.

### g. É possível para um dado agente ser perfeitamente racional em dois ambientes de tarefa distintos.

- Julgamento: V
- Justificativa: se a melhor ação é a mesma nos dois ambientes (ou os ambientes são diferentes só em detalhes que não afetam a decisão), o mesmo agente é racional nos dois.
- Exemplo ou contraexemplo: agente de xadrez que utiliza uma estrategia otima para dois adversarios diferentes. Ele e racional nos dois.

### h. Todo agente é racional em um ambiente não observável.

- Julgamento: F
- Justificativa: se ele não consegue observar não consegue diferir se tem ações melhores e piores, se ele escolhe mal não e racional.
- Exemplo ou contraexemplo: robô pintor sem sensores que gira em círculos sem pintar. Ele é pior que um que segue uma sequência fixa de pintura.

### i. Um agente jogador de pôquer perfeitamente racional nunca perde.

- Julgamento: F
- Justificativa: pôquer envolve sorte e informação oculta. Racional maximiza o resultado esperado, não o resultado de cada mão.
- Exemplo ou contraexemplo:  o agente joga bem com um par de ases, mas o adversário completa uma sequência por sorte. Ele perde a mão e continua racional.

## Exercício 2.4
Para cada caso, delimite o agente, preencha o PEAS e justifique todas as classificações. Considere Titã como cenário hipotético do exercício.

### Caso 1 — Jogar futebol.

- Agente analisado: um jogador de um time
- Objetivo e hipóteses: ajudar o time a marcar mais gols que o adversário.
- P — Medida de desempenho: gols marcados, menos gols sofridos, vitória, respeito às regras.
- E — Ambiente: campo, bola, gols, companheiros, adversários, árbitro.
- A — Atuadores: pernas, cabeça, voz/gestos.
- S — Sensores: olhos, ouvidos, tato/equilíbrio.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Não da pra ver o campo todo o tempo inteiro |
| Número de agentes | Multiagente (coopera com o time, compete com o adversário) | Vários jogadores com objetivos próprios. |
| Previsibilidade |	Estocástico | Movimento da bola e reações dos outros não são previsíveis com certeza. |
| Dependência entre decisões | Sequencial | Posicionamento e passes de agora afetam as jogadas seguintes. |
| Mudança durante a decisão | Dinâmico | O jogo continua enquanto o jogador pensa. |
| Natureza dos elementos | Contínuos | Posição, velocidade e tempo variam continuamente. |
| Conhecimento do funcionamento | Conhecido | Regras e física básica da bola são conhecidas. |

### Caso 2 — Explorar os oceanos subterrâneos de Titã.

- Agente analisado: robô submarino autônomo.
- Objetivo e hipóteses: mapear e coletar dados do oceano de Titã; hipótese: sem outros agentes e com comunicação lenta com a Terra.
- P — Medida de desempenho: quantidade e qualidade de dados científicos, área explorada, sobrevivência do robô.
- E — Ambiente: oceano sob o gelo de Titã (líquido, pressão, temperatura baixa, correntes, relevo).
- A — Atuadores: propulsores, lemes, braço de coleta, antena de comunicação.
- S — Sensores: sonar, câmeras, termômetro, sensor de pressão, sensores químicos.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Sensores têm alcance limitado e o ambiente é escuro e pouco mapeado. |
| Número de agentes | Agente único | Hipótese: não há outros agentes. |
| Previsibilidade | Estocástico | Correntes, falhas e terreno desconhecido tornam os resultados incertos. |
| Dependência entre decisões | Sequencial | Energia e posição de agora afetam o que vem depois. |
| Mudança durante a decisão | Dinâmico | Correntes e condições mudam enquanto o robô decide. |
| Natureza dos elementos | Contínuos | Posição, pressão, temperatura e tempo são contínuos. |
| Conhecimento do funcionamento | Desconhecido | Ambiente pouco conhecido; o agente precisa aprender. |

### Caso 3 — Comprar livros usados de IA na Internet.

- Agente analisado: agente de software (bot de compras).
- Objetivo e hipóteses: comprar livros de IA em boa condição e com preço baixo, dentro de um orçamento.
- P — Medida de desempenho: preço pago, condição e relevância do livro, prazo de entrega, orçamento respeitado.
- E — Ambiente: Internet: lojas, sebos online, vendedores, outros compradores, sistemas de pagamento.
- A — Atuadores: digitar buscas, clicar em links, preencher formulários, finalizar pagamento (saídas digitais).
- S — Sensores: leitura de páginas web (preço, descrição, fotos, avaliações, estoque) — entradas digitais.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Não vê todo o estoque, nem a condição real do livro, nem preços de todas as lojas. |
| Número de agentes | Multiagente (competitivo) | Vendedores e outros compradores disputam os mesmos livros. |
| Previsibilidade | Estocástico | O livro pode ser vendido, o vendedor pode falhar ou atrasar. |
| Dependência entre decisões | Sequencial | O orçamento gasto e os livros já comprados afetam as próximas compras. |
| Mudança durante a decisão | Dinâmico | Preços e estoque mudam enquanto o agente navega. |
| Natureza dos elementos | Discretos | Páginas, links, ações e preços (em centavos) são contáveis. |
| Conhecimento do funcionamento | Conhecido | Sabe como navegar e comprar em sites (regras gerais). |

### Caso 4 — Jogar uma partida de tênis.

- Agente analisado: um tenista.
- Objetivo e hipóteses: vencer a partida; hipótese: partida individual (simples).
- P — Medida de desempenho: pontos, games e sets ganhos; erros não forçados.
- E — Ambiente: quadra, bola, rede, adversário, juiz.
- A — Atuadores: pernas (deslocar), braço e raquete (golpes), saque.
- S — Sensores: olhos (bola e adversário), ouvidos, tato na raquete.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Não sabe a estratégia do adversário nem o efeito/rotação exatos da bola. |
| Número de agentes | Multiagente (competitivo) | O adversário tenta o oposto do agente. |
| Previsibilidade | Estocástico | Resultado do golpe e resposta do adversário são incertos. |
| Dependência entre decisões | Sequencial | Cada golpe influencia o ponto e o jogo. |
| Mudança durante a decisão | Dinâmico | A bola continua em movimento enquanto decide. |
| Natureza dos elementos | Contínuos | Posição, velocidade e tempo variam continuamente. |
| Conhecimento do funcionamento | Conhecido | Regras e física da bola são conhecidas. |

### Caso 5 — Praticar tênis contra uma parede.

- Agente analisado: um tenista treinando sozinho.
- Objetivo e hipóteses: melhorar a técnica e manter a bola em jogo; hipótese: parede ideal, sem vento.
- P — Medida de desempenho: número de rebatidas seguidas, precisão dos golpes.
- E — Ambiente: parede, bola, piso, quadra.
- A — Atuadores: pernas, braço e raquete.
- S — Sensores: olhos (bola), ouvidos (som do rebote), tato.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Completamente observável (sob a hipótese) | Posição e velocidade da bola são percebidas; a parede não esconde nada. |
| Número de agentes | Agente único | A parede não tem objetivos nem estratégia. |
| Previsibilidade | Determinístico (sob a hipótese) | Com parede e bola ideais, o rebote segue a física. Na prática há pequenos ruídos. |
| Dependência entre decisões | Sequencial | Cada golpe define o próximo rebote. |
| Mudança durante a decisão | Dinâmico | A bola se move enquanto o jogador decide. |
| Natureza dos elementos | Contínuos | Posição, velocidade e tempo contínuos. |
| Conhecimento do funcionamento | Conhecido | Física do rebote conhecida. |

### Caso 6 — Realizar um salto de altura.

- Agente analisado: um atleta saltador.
- Objetivo e hipóteses: ultrapassar a barra na maior altura possível; hipótese: analisar um único salto.
- P — Medida de desempenho: altura superada, barra não derrubada.
- E — Ambiente: pista de corrida, barra, colchão, vento, juiz.
- A — Atuadores: pernas (corrida e impulso), braços e tronco (postura no ar).
- S — Sensores: olhos (barra, distância), equilíbrio, tato dos pés.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Não percebe com exatidão o próprio corpo no ar nem o vento. |
| Número de agentes | Agente único | Hipótese: os outros atletas não interferem no salto. |
| Previsibilidade | Estocástico | Pequenos erros e vento alteram o resultado. |
| Dependência entre decisões | Episódico (hipótese de um salto) | Um salto é avaliado de forma independente. Em competição completa seria sequencial. |
| Mudança durante a decisão | Semidinâmico | O ambiente (barra) não muda, mas há limite de tempo para a tentativa. |
| Natureza dos elementos | Contínuos | Corpo, trajetória e tempo contínuos. |
| Conhecimento do funcionamento | Conhecido | Regras do salto e física básica conhecidas. |

### Caso 7 — Participar de um leilão de um item, realizando lances.

- Agente analisado: um participante (pessoa ou software) que dá lances.
- Objetivo e hipóteses: ganhar o item pagando no máximo seu valor limite; hipótese: leilão inglês (lances crescentes).
- P — Medida de desempenho: ganhar o item com a maior diferença entre valor do item e preço pago; não passar do limite.
- E — Ambiente: casa de leilões (ou site), item, leiloeiro, outros participantes.
- A — Atuadores: dar lance (voz, plaquinha ou clique), desistir.
- S — Sensores: ver/ouvir os lances, preço atual e tempo restante.

| Propriedade | Classificação | Justificativa |
|---|---|---|
| Observabilidade | Parcialmente observável | Não vê o limite nem a estratégia dos outros participantes. |
| Número de agentes | Multiagente (competitivo) | Todos querem o mesmo item. |
| Previsibilidade | Estocástico (influência estratégica) | O que os outros farão é incerto e define o resultado. |
| Dependência entre decisões | Sequencial | Lances anteriores afetam o preço e as decisões seguintes. |
| Mudança durante a decisão | Dinâmico | Outros podem dar lances enquanto o agente pensa. |
| Natureza dos elementos | Discretos | Lances em valores definidos e rodadas contáveis. |
| Conhecimento do funcionamento | Conhecido | Regras do leilão são conhecidas. |

### Opções para classificação
- **Observabilidade:** Completamente observável, parcialmente observável ou não observável.
- **Número de agentes:** Agente único ou multiagente; indique cooperação ou competição quando pertinente.
- **Previsibilidade:** Determinístico ou estocástico; considere a influência estratégica de outros agentes.
- **Dependência entre decisões:** Episódico ou sequencial.
- **Mudança durante a decisão:** Estático, dinâmico ou semidinâmico.
- **Natureza dos elementos:** Discretos, contínuos ou combinação; considere estados, tempo, percepções e ações.
- **Conhecimento do funcionamento:** Conhecido ou desconhecido para o agente.

### Comparação final
1. O que muda entre jogar tênis contra outra pessoa e praticar contra uma parede?
2. Por que comprar livros usados pode exigir decisões com informações incompletas?
3. Como outros agentes influenciam futebol e leilões?

Respostas: 
1. **Tênis contra pessoa x parede:** com a pessoa, o ambiente é multiagente competitivo: o adversário reage e usa estratégia, então é estocástico e parcialmente observável. Contra a parede é agente único: a parede não tem estratégia, o rebote é muito mais previsível e o treino é mais "controlado".
2. **Livros usados e informação incompleta:** o agente não vê a condição real do livro, o estoque total, os preços de todas as lojas nem se o vendedor é confiável. Avaliações podem ser falsas e os preços mudam. Ele precisa decidir (comprar agora ou esperar?) mesmo sem saber tudo.
3. **Outros agentes em futebol e leilão:** no futebol, companheiros cooperam e adversários competem. Cada decisão depende do que os outros fazem (passe, marcação). No leilão, os lances dos outros definem o preço e quem ganha. Em ambos, é preciso antecipar o comportamento dos outros.

## Exercício 2.5
Defina cada termo com suas palavras em duas a quatro linhas e apresente um exemplo.

### Agente
- Definição: qualquer coisa que percebe o ambiente por sensores e age sobre ele por atuadores para atingir algum objetivo.
- Exemplo: aspirador robô (sensores de sujeira e obstáculos; rodas e escova).

### Função de agente
- Definição: descrição abstrata (matemática) que associa cada sequência de percepções a uma ação. É a "regra ideal" do comportamento.
- Exemplo: tabela "se percebi [A, sujo] → aspirar; [A, limpo] → ir para B".

### Programa de agente
- Definição: código concreto que implementa a função em uma máquina. Recebe só a percepção atual e, se precisar, guarda memória.
- Exemplo: programa em Python do aspirador que lê o sensor e escolhe a ação, guardando um contador de passos.

### Racionalidade
- Definição: escolher, a cada momento, a ação que maximiza o desempenho esperado, dado o que o agente percebeu e já sabe. Não exige ser perfeito nem prever o futuro.
- Exemplo: levar guarda-chuva ao ver nuvens escuras. Se não chover, a decisão continua racional.

### Autonomia
- Definição: capacidade de o agente decidir com base na própria experiência, e não só no conhecimento colocado pelo programador.
- Exemplo: aspirador que aprende o mapa da casa e os horários em que há mais sujeira.

### Agente reativo
- Definição: escolhe a ação só pela percepção atual, com regras do tipo "se... então...". Não tem memória.
- Exemplo: termostato: se temperatura > 25°C, liga o ar.

### Agente baseado em modelo
- Definição: mantém um estado interno (modelo do mundo) que guarda o que não consegue ver agora, atualizado com o histórico de percepções.
- Exemplo: carro autônomo que lembra que há um carro no ponto cego mesmo sem vê-lo.

### Agente baseado em objetivos
- Definição: escolhe ações pensando em atingir um objetivo, planejando e comparando caminhos que levam a ele.
- Exemplo: GPS que planeja a rota até o destino.

### Agente baseado em utilidade
- Definição: além de atingir o objetivo, mede o quão bom é cada resultado (utilidade) e escolhe o melhor, equilibrando vários critérios.
- Exemplo: GPS que escolhe a rota ponderando tempo, pedágio e segurança.

### Agente com aprendizagem
- Definição: melhora o próprio desempenho com a experiência, usando um crítico que avalia as ações e um elemento que altera o comportamento.
- Exemplo: recomendador de filmes que ajusta as sugestões conforme o que o usuário assiste.

## Síntese com autômatos
Escolha um caso do item 2.4. Apresente três estados internos, três percepções, três ações e duas regras no formato estado atual + percepção → próximo estado e ação. Explique como estados internos representam informação passada e cite uma limitação da simplificação.

Resposta: 
Caso escolhido: **Caso 7 — leilão** (leilão inglês, agente com limite de preço).

- **Estados internos:** `Observando` (ainda sem lance), `Liderando` (meu lance é o maior), `Superado` (outro passou meu lance).
- **Percepções:** `A` = rival cobre o lance e o novo preço ≤ meu limite; `B` = rival cobre o lance e o novo preço > meu limite; `C` = passa o tempo sem novos lances.
- **Ações:** `dar_lance`, `aguardar`, `desistir`.
- **Regras (estado atual + percepção → próximo estado e ação):**
  1. `Superado + A → Liderando, dar_lance` (cubro o lance, pois ainda cabe no limite).
  2. `Superado + B → Superado, desistir` (preço passou do meu limite; saio do leilão).
- **Estados e informação passada:** o estado resume o que aconteceu antes. `Liderando` "lembra" que meu último lance é o maior; `Superado` "lembra" que fui ultrapassado. Assim o agente não precisa guardar toda a sequência de lances.
- **Limitação:** a simplificação perde informação: não guarda o valor dos lances anteriores, o orçamento restante nem o padrão dos rivais. Com poucos estados, também não aprende nem planeja estratégia.

## Entrega e avaliação
Confira: identificação; nove análises no item 2.3; sete casos completos no item 2.4; dez conceitos no item 2.5; síntese; referências.
Nome sugerido: `NomeSobrenome_Atividade_AgentesInteligentes`. Prazo e envio conforme orientação da professora.

| Critério | Atividade avaliativa (1,0 ponto) A2 |
|---|---:|
| Item 2.3 — correção e argumentação | 30% |
| Item 2.4 — PEAS e classificação justificada | 40% |
| Item 2.5 — precisão conceitual e exemplos | 20% |
| Síntese, organização e referências | 10% |

## Referências
Material-base: Capítulo 2 — Agentes inteligentes, disponibilizado para a aula de 19/10/2026.
Referências adicionais: ...
