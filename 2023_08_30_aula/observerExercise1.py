from abc import ABC, abstractmethod

class Subject(ABC):
    """Abstract subject"""
    def __init__(self):
        self.observers = []

    def inscrever(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def sair(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    @abstractmethod
    def notificar(self):
        pass

class Observer(ABC):
    """Abstract Observer"""
    @abstractmethod
    def atualizar(self):
        pass

class Estoque(Subject):
    """Observadores ficaram de olho no Estoque"""
    def __init__(self):
        super().__init__()
        self.produtos = []

    def notificar(self):
        print(f"Notificando inscritos: {len(self.observers)}")
        for observer in self.observers:
            observer.atualizar() # avisar todos inscritos

    def receber_produto(self, produto: str, preco: float):
        print(f"Novo produto chegou: {produto} - Preço: {preco}")
        self.produtos.append((produto, preco))
        self.notificar()

class Usuario(Observer):
    def __init__(self, nome, produto=None, subject=None, preco_limite=None):
        self.nome = nome
        self.produto = produto
        self.subject = subject
        self.preco_limite = preco_limite
        if self.subject:
            self.subject.inscrever(self)

    def atualizar(self):
        for produto, preco in self.subject.produtos:
            if (self.produto is None or self.produto == produto) and \
               (self.preco_limite is None or preco < self.preco_limite):
                print(f"[Usuario] {self.nome} notificado")
                print(f"O produto {produto} está disponível por {preco}")

if __name__ == '__main__':
    print('Observer - Notificação de produtos')
    estoque = Estoque()
    joana = Usuario("Joana", "Teclado A", subject=estoque, preco_limite=120)
    fornecedor = Usuario("Fornecedor", subject=estoque)

    estoque.receber_produto("Teclado A", 100)
    estoque.receber_produto("Mouse B", 50)
