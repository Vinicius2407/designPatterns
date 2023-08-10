from abc import ABC

# A classe pessoa é muito genérica, não faz sentido instanciar um objeto do tipo pessoa.
# Pessoa ta sendo definida como uma classe abstrata, não pode ser instanciada
class Pessoa(ABC):
    # Contrutor da classe, executado ao instanciar a classe
    def __init__(self): 
        self.nome = ""  #'self' é o 'this' do C#
        

# PF extends Pessoa
class PessoaFisica(Pessoa):
    def __init__(self):
        super().__init__() # Chama o construtor da classe pai
        self.cpf = ""
        self.renda = 0.0

    def printDados(self):
        print("Nome:" + self.nome)
        print("CPF:" + self.cpf)

    @staticmethod
    def quantidadeNumerosCpfNecessarios():
        return 11
    
    # Pode ficar meio primitivo
    def calcularIR(self):
        valor = self.renda * 0.25
        return str(valor)


# PJ extends Pessoa
class PessoaJuridica(Pessoa):
    def __init__(self):
        super().__init__() # Chama o construtor da classe pai
        self.cnpj = ""
        self.faturamento = 0.0
        porcentagemIR = 0.18

    def printDados(self):
        print("Nome:" + self.nome)
        print("CNPJ:" + self.cnpj)

    @staticmethod
    def quantidadeNumerosCnpjNecessarios():
        return 14
    
    # Pode ficar meio primitivo
    def calcularIR(self):
       valor = self.faturamento * 0.18
       return str(valor)


class CalcularIR:
    
    def calcularIR(Pessoa):
        valor = pessoaFisica
        return str(valor)
    

# Main, executado ao rodar o arquivo, não é necessário no Python
if __name__ == "__main__":
    # Instanciando um objeto do tipo Pessoa e atribuindo valores aos atributos
    pessoaJuridica = PessoaJuridica()
    pessoaJuridica.nome = ""
    pessoaJuridica.cnpj = "123456789"
    pessoaJuridica.faturamento = 10600.30
    #pessoaJuridica.printDados()

    pessoaFisica = PessoaFisica()
    pessoaFisica.nome = "Fulano"
    pessoaFisica.cpf = "987654321"
    pessoaFisica.renda = 2400.40
    #pessoaFisica.printDados()
    
    # print("A " + pessoaFisica.nome + " tem que pagar " + pessoaFisica.calcularIR() + " de IR")
    # print("A " + pessoaJuridica.nome + " tem que pagar " + pessoaJuridica.calcularIR() + " de IR")
    
    CalcularIR.calcularIR(pessoaFisica)
    CalcularIR.calcularIR(pessoaJuridica)

    # print(id(pessoaFisica))
    # print(id(pessoaJuridica))
    #print(PessoaFisica.quantidadeNumerosCpfNecessarios())
    #print(PessoaJuridica.quantidadeNumerosCnpjNecessarios())


# Se o endereço de memória for diferente, então são objetos diferentes
# Se o endereço de memória for igual, então são objetos iguais, apenas compartilham alguma coisa em comum