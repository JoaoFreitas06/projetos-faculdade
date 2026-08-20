'''
Tema: A Pilha de Magias do "The Witcher" (Pilhas - LIFO)
Contexto: Geralt de Rívia usa uma pilha de magias — a última magia aprendida é a primeira a ser usada em batalha.

Tarefas:

Criar uma pilha (list) chamada magias_geralt.

Função aprender_magia(pilha, magia) (ex: "Igni").

Adicionar: "Quen", "Aard", "Yrden".

Visualizar a pilha.

Função usar_magia(pilha) que remove e retorna a última magia.

Verificar se a pilha está vazia após uso.
'''

magias_geralt = [] #Criando pilha vazia

def aprender_magia(pilha, magia): # função para adicionar as magias na lista
    pilha.append(magia)

#adicionando as magias
aprender_magia(magias_geralt, "Quen")
aprender_magia(magias_geralt, "Yrden")
aprender_magia(magias_geralt, "Igni")
aprender_magia(magias_geralt, "Aard")

#mostrando todas as magias
print("Magias prontas:", magias_geralt)

#Função para utilizar a ultima magia adicionada
def utilizar_magia(pilha):
    if len(pilha) > 0: #confere se a lista tem itens
        return pilha.pop() #retira o ultimo item da lista e mostra ele
    else:
        return "Magias Esgotadas!"

#mostra a magia que foi utilizada
magias = utilizar_magia(magias_geralt)
print("\nA proxima magia a ser uzada é:", magias)

#funcao que mostra se a pilha de magias esta vazia
def pilha_vazia(pilha):
    return len(pilha) == 0 #confere se o valor dela esta zerado e retorna true or false

print("\nA pilha de magias esta vazia?", pilha_vazia(magias_geralt))

#mostra as magias que ainda tem
print("\nPilha de magias atualizada:", magias_geralt)

#utilizando o resto das magias
print("\nUtilizando o restante das magias")
while len(magias_geralt):
    magias_restantes = utilizar_magia(magias_geralt)
    print("\nMagia sendo utilizada:", magias_restantes)

#verificando se a lista esta vazia
print("\nTodas as magias foram utilizadas?", pilha_vazia(magias_geralt))