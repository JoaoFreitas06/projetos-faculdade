'''
Tema: O Catálogo de Poções da Madame Pomfrey (Listas - Harry Potter)
Contexto: Organizar poções curativas em Hogwarts, com remoção por uso.

Tarefas:
Criar uma lista catalogo_pocoes = [].
Função adicionar_pocao(catalogo, pocao) (ex: "Poção Restauradora").

Adicionar:
"Poção Restauradora"
"Poção de Ossos Crescidos"
"Poção de Pele de Dragão"

Buscar poção por índice (ex: índice 1 = "Poção de Ossos Crescidos").

Remover "Poção de Ossos Crescidos" (usada em um aluno).

Verificar se "Poção Restauradora" ainda está disponível.
'''

#Criando lista vazia
catalogo_pocoes = []

#Criar funcao de adicionar as pocoes
def adicionar_pocoes(catalogo, pocao):
    catalogo.append(pocao)

#adicionando as pocoes
adicionar_pocoes(catalogo_pocoes, "Poção Restauradora")
adicionar_pocoes(catalogo_pocoes, "Poção de Ossos Crescidos")
adicionar_pocoes(catalogo_pocoes, "Poção de Pele de Dragão")

#visualizar catologo
print("Catalogo de pocões:", catalogo_pocoes)

#funcao para localizar a pocao no catalogo
def buscar_pocao(catalogo, indice):
    if 0 <= indice < len(catalogo):
        return catalogo[indice]
    else:
        return "Indice invalido"
    
#mostrando o indice 1
pocao_1 = buscar_pocao(catalogo_pocoes, 1)
print("\nPoção na posicao 1:", pocao_1)

#removendo o livro 1
catalogo_pocoes.remove("Poção de Ossos Crescidos")
print("\nCatalogo atualizado:", catalogo_pocoes)

#funcao para verificar se tem uma pocao no catalogo
def verificar_pocao(catalogo, pocao):
    return pocao in catalogo

#Verificando se a pocao no indice 1 esta diponivel
pocao = verificar_pocao(catalogo_pocoes, "Poção de Pele de Dragão")
print("\nA poção Poção de Pele de Dragão esta disponivel?",pocao)