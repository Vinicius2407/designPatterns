from abc import ABC, abstractmethod

# Classe abstrata para os observadores
class Observer(ABC):
    @abstractmethod
    def atualizar(self, lumens):
        pass

# Observador interno
class ObservadorInterno(Observer):
    def __init__(self, lampadas_internas):
        self.lampadas_internas = lampadas_internas

    def atualizar(self, lumens):
        if lumens < 100:
            print("Observador Interno: Acionar todas as lâmpadas internas")
            self.lampadas_internas.acionar_todas()
        elif 100 <= lumens <= 300:
            print("Observador Interno: Acionar metade das lâmpadas internas")
            self.lampadas_internas.acionar_metade()
        else:
            print("Observador Interno: Desligar todas as lâmpadas internas")
            self.lampadas_internas.desligar_todas()

# Observador externo
class ObservadorExterno(Observer):
    def __init__(self, lampadas_externas):
        self.lampadas_externas = lampadas_externas

    def atualizar(self, lumens):
        if lumens <= 50:
            print("Observador Externo: Acionar todas as lâmpadas externas")
            self.lampadas_externas.acionar_todas()
        elif 50 < lumens <= 200:
            print("Observador Externo: Acionar apenas lâmpadas de LED externas")
            self.lampadas_externas.acionar_led()
        else:
            print("Observador Externo: Desligar todas as lâmpadas externas")
            self.lampadas_externas.desligar_todas()

# Classe para as lâmpadas internas
class LampadasInternas:
    def acionar_todas(self):
        print("Todas as lâmpadas internas foram acesas")

    def acionar_metade(self):
        print("Metade das lâmpadas internas foi acesa")

    def desligar_todas(self):
        print("Todas as lâmpadas internas foram desligadas")

# Classe para as lâmpadas externas
class LampadasExternas:
    def acionar_todas(self):
        print("Todas as lâmpadas externas foram acesas")

    def acionar_led(self):
        print("Apenas as lâmpadas de LED externas foram acesas")

    def desligar_todas(self):
        print("Todas as lâmpadas externas foram desligadas")

# Classe para o Sensor de Luminosidade (o sujeito observado)
class SensorNotifier:
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, lumens):
        for observador in self.observadores:
            observador.atualizar(lumens)

# Exemplo de uso
if __name__ == "__main__":
    sensor = SensorNotifier()
    lampadas_internas = LampadasInternas()
    lampadas_externas = LampadasExternas()

    observador_interno = ObservadorInterno(lampadas_internas)
    observador_externo = ObservadorExterno(lampadas_externas)

    sensor.adicionar_observador(observador_interno)
    sensor.adicionar_observador(observador_externo)

    # Simula uma mudança na luminosidade
    lumens = 304 # Você pode alterar esse valor para testar diferentes cenários
    sensor.notificar_observadores(lumens)
