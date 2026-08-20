class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaOrdenada:
    def __init__(self): 
        self.inicio = None

    def inserir(self, valor):
        novo = No(valor)
        if self.inicio is None or valor < self.inicio.valor:
            novo.proximo = self.inicio
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo and atual.proximo.valor < valor:
                atual = atual.proximo
            novo.proximo = atual.proximo
            atual.proximo = novo

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.valor, end=' -> ')
            atual = atual.proximo
        print('None')