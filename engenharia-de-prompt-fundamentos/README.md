# Atividade 01
## (Utilizando o Claude)

# Prompt Generico 
- ## Comando dado: me explique o que e caso de uso.

Caso de uso é uma técnica usada na engenharia de software (e em análise de sistemas de forma geral) para descrever como um usuário interage com um sistema para atingir um objetivo específico.

Ideia central

Um caso de uso descreve:

Quem interage com o sistema (o "ator" — pode ser uma pessoa, outro sistema, etc.)
O que ele quer fazer (o objetivo)
Como essa interação acontece, passo a passo (o fluxo)
Exemplo prático

Imagine um sistema de e-commerce. Um caso de uso poderia ser:

Nome: Realizar compra
Ator: Cliente
Fluxo principal:

Cliente adiciona produto ao carrinho
Cliente acessa o carrinho
Cliente informa endereço de entrega
Cliente escolhe forma de pagamento
Sistema confirma o pedido

Também pode ter fluxos alternativos (ex: pagamento recusado) e pré-condições (ex: cliente precisa estar logado).

Para que serve
Ajuda a entender os requisitos funcionais do sistema (o que ele precisa fazer)
Facilita a comunicação entre quem pede o sistema (cliente/stakeholder) e quem desenvolve
Serve de base para escrever testes e validar se o sistema funciona como esperado
Frequentemente é representado visualmente em diagramas de caso de uso (parte da UML), com bonequinhos representando atores conectados a elipses representando as ações
Diferença de "requisito"

Um requisito é mais técnico e pontual ("o sistema deve validar CPF"). Um caso de uso é mais amplo e conta uma "história" de interação, do início ao fim de um objetivo do usuário.

# Prompt Estruturado

- ## Novo Comando: Agora, atue como um professor de uma faculdade de TI, com mestrado em UML, me explique o que e Caso de Uso como se fosse para um iniciante, usando alguma analogia que alguem que não tem tanta familiariadade com o tema entenda.

Caso de Uso — explicando como se fosse a primeira aula

Vou usar uma analogia que costumo dar para minhas turmas de calouros: pense em um restaurante.

A analogia do restaurante

Imagine que você está documentando como um restaurante funciona, mas não quer descrever cada detalhe técnico da cozinha (isso viria depois). Você quer descrever as coisas que as pessoas fazem ali, do ponto de vista de quem interage com o restaurante.

Então você lista coisas como:

Cliente → "Fazer um pedido"
Cliente → "Pagar a conta"
Garçom → "Anotar pedido na comanda"
Cozinheiro → "Preparar prato"
Gerente → "Fechar o caixa no fim do dia"

Repare: cada uma dessas frases é uma ação com um objetivo, feita por alguém específico. Isso, no mundo da TI, é exatamente o que chamamos de Caso de Uso.

Traduzindo os termos
No restaurante	No sistema
Cliente, Garçom, Cozinheiro	Atores (quem interage)
"Fazer um pedido"	Caso de Uso (o que é feito)
O restaurante em si	O sistema
Por que isso é útil?

Quando você projeta um sistema (por exemplo, um app de delivery), antes de pensar em código, banco de dados ou telas, você quer responder uma pergunta simples:

"Quem usa esse sistema, e o que cada um precisa fazer nele?"

Se você não sabe responder isso claramente, é sinal de que ainda não entendeu bem o problema — e vai acabar programando "no escuro".

E o desenho?

Na UML, a gente representa isso visualmente assim:

Um bonequinho (👤) = o ator
Uma bolinha oval (⬭) = o caso de uso
Uma linha ligando os dois = "esse ator realiza essa ação"

Fica parecendo um mapa simples de "quem faz o quê" dentro do sistema.

# Reflexão:

Estruturando o prompt e pedindo pra IA te explicar tudo do jeito que voce mais prefere, fica mais organizado e melhor para seguir a linha de raciocinio.