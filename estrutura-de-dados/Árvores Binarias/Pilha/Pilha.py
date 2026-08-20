class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item) 

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        raise IndexError("Pilha vazia")

    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]
        return None

    def esta_vazia(self):
        return len(self.items) == 0

    def tamanho(self):
        return len(self.items)