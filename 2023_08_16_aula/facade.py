# Componentes:
# 1 - PlacaMae
# 2 - Processador
# 3 - Memoria
# 4 - HD
# 5 - PlacaVideo

class PlacaMae:
    def __init__(self, boot):
        self.boot = boot

    def on(self):
        print('Ligando a placa mãe')
    
class Processador:
    def __init__(self, profile):
        self.profile = profile

    def on(self):
        print('Ligando o processador')
    
class Memoria:
    def __init__(self):
        pass
    def on(self):
        print('memória ok')

# Ligar o computador
class ComputerFacade:
    def __init__(self):
        self.placa = PlacaMae("bootNormal")
        self.processador = Processador(profile="dev")
        self.memoria = Memoria()

    def on(self):
        self.placa.on()
        self.processador.on()
        self.memoria.on()


if __name__ == '__main__':
    computador = ComputerFacade()
    computador.on()