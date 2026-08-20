class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None 

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        novo = No(valor)
        novo.proximo = self.inicio
        self.inicio = novo

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.valor, end=' -> ')
            atual = atual.proximo
        print('None')