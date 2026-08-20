'''Tema: O Inventário do "Death Note" (Listas - Ordem Aleatória)
Contexto: Light Yagami precisa organizar seus itens (Death Note, maçã, relógio de shinigami) e verificar se um item específico está disponível.

Tarefas:

Criar uma lista inventario_light = [].

Função adicionar_item(inventario, item).

Adicionar: "Death Note", "Maçã", "Relógio de Shinigami".

Visualizar o inventário.

Função buscar_item(inventario, item) que retorna True se o item existe.

Remover "Maçã" (consumida).

Verificar se "Death Note" ainda está no inventário.
'''

from collections import deque

#criandop a fila vazia
inventario_light = deque()

#função para adicionar itens
def adicionar_item(fila, item):
    fila.append(item)

#adicionando os itens na fila
adicionar_item(inventario_light, "Death Note")
adicionar_item(inventario_light, "Maçã")
adicionar_item(inventario_light, "Relógio de Shinigami")

#visualizando a fila
print("Itens na fila do inventário:", list(inventario_light))

#função para remover itens
def remover_item(fila):
    if len(fila) > 0:
        return fila.popleft()
    else:
        return "Inventário vazio"

#removendo o primeiro item
item_removido = remover_item(inventario_light)
print("\nItem removido:", item_removido)

#função para verificar se a fila esta vazia
def inventario_vazio(fila):
    return len(fila) == 0

print("\nO inventario está vazio?", inventario_vazio(inventario_light))

#visualizar itens restantes
print("\nItens restantes no inventario:", list(inventario_light))

#removendo todos os itens restantes
print("\nRemovendo itens restantes:")
while not inventario_vazio(inventario_light):
    print("Item removido:", remover_item(inventario_light))

#verificando se a fila esta vazia
print("\nO inventario esta totalmente vazio?", inventario_vazio(inventario_light))