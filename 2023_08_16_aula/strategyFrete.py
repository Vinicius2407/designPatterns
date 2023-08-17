# Definindo a classe base para as estratégias de envio
class EnvioStrategy:
    def calcularFrete(self, peso):
        pass

# Implementação da estratégia de envio aérea
class EnvioAerea(EnvioStrategy):
    def calcularFrete(self, peso):
        return peso * 25.0

# Implementação da estratégia de envio express
class EnvioExpress(EnvioStrategy):
    def calcularFrete(self, peso):
        return peso * 15.0

# Implementação da estratégia de envio pelos correios
class EnvioCorreios(EnvioStrategy):
    def calcularFrete(self, peso):
        return peso * 10.0

# Classe do produto
class Produto:
    def __init__(self, nome, valor, peso, estrategiaEnvio):
        self.nome = nome
        self.valor = valor
        self.peso = peso
        self.estrategiaEnvio = estrategiaEnvio

class Contexto():
    def calcularFrete(self, produto, strategy):
        return strategy.calcularFrete(produto.peso)

# Criando instâncias das estratégias de envio
envioAerea = EnvioAerea()
envioExpress = EnvioExpress()
envioCorreios = EnvioCorreios()

# Criando instâncias de produtos com diferentes formas de envio
produto1 = Produto("Cadeira Gamer", 300, 15, envioAerea)
produto2 = Produto("Notebook", 3000, 4, envioExpress)
produto3 = Produto("Prato de porcelana", 50, 0.5, envioCorreios)

# Criando o contexto para fazer a chamada da estratégia
contexto = Contexto()

# Calculando o valor total dos produtos com frete
produtos = [produto1, produto2, produto3]

for produto in produtos:
    valorTotal = contexto.calcularFrete(produto, produto.estrategiaEnvio) + produto.valor
    print(f"Produto: {produto.nome}, Valor Total: R${valorTotal:.2f}")
