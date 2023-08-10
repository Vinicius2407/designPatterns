# Definir uma interface que representa as possibilidades
# de pagamento (forma de pagamento)

class PagamentStrategy:
    def pagar(valor):
        pass

# Existe uma classe concreta de pagamento PixStrategy
class PixStrategy(PagamentStrategy):
    def __init__(self, chavePixOrigem, chavePixDestino = None):
        self.chavePixOrigem = chavePixOrigem
        self.chavePixDestino = chavePixDestino
    
    def pagar(self, valor):
        # Aqui vai o código para realizar o pagamento
        print(f"Pagamento de R$ {valor} realizado com sucesso via PIX para a chave {self.chavePix}")

class BoletoStrategy(PagamentStrategy):
    def __init__(self, codigoBarras):
        self.codigoBarras = codigoBarras

    def pagar(self, valor):
        # Aqui vai o código para realizar o pagamento
        valor = valor * 0.9
        print(f"Pagamento de R$ {valor} realizado com sucesso via Boleto para o código {self.codigoBarras}")

# Existe um contexto, que representa a preferencia do cliente
# por uma forma de pagamento
class Contexto:
    def realizarPagamento(self, strategy, valor):
        strategy.pagar(valor)


if __name__ == "__main__":
    # 1. Usuario escolhe a forma de pagamento no pix
    pixPagamento = PixStrategy("123.456.789-01")

    # 2. Passar para o "Context" processar o pagamento
    context = Contexto()
    context.realizarPagamento(pixPagamento, 3000) # Preciso passar qual a estretégia que sera 
    
    # 3. Usuario escolhe a forma de pagamento no boleto
    boletoPagamento = BoletoStrategy("15151515151151515151515151515")
    context.realizarPagamento(boletoPagamento, 3000) # Preciso passar qual a estretégia que sera

    # 4. Usuario escolhe a forma de pagamento no cartao
    # pode parcelar, acrescentar + 5% de juros
