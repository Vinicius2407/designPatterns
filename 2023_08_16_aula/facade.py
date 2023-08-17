# Componentes:
# 1 - PlacaMae
# 2 - Processador
# 3 - Memoria
# 4 - HD
# 5 - PlacaVideo

class PlacaMae:
    def on(self):
        print('Ligando a placa mãe')
    
class Processador:
    def on(self):
        print('Ligando o processador')
    
class Memoria:
    def on(self):
        print('memória ok')

# Ligar o computador
class ComputerFacade:
    def __init__(self):
        self.processador = Processador()
        self.placa = PlacaMae()
        self.memoria = Memoria()

    def on(self):
        self.placa.on()
        self.processador.on()
        self.memoria.on()


if __name__ == '__main__':
    computador = ComputerFacade()
    computador.on()