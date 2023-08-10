# Implementar o Singleton

# class Connection:
#     _instance = None

#     def __init__(self):
#         print("Conexão criada")
#         self.driver = "mysql"

#     def __new__(cls, *args, **kwargs):
#         print("Criando instância")
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

# if __name__ == "__main__":
#     conn = Connection()
#     conn.driver = "postgres"
#     print(id(conn))

#     conn2 = Connection()
#     conn.driver = "sqlite"
#     print(id(conn2))

#     print(conn.driver)

class SiteConfiguration:
    _instance = None
    visitantes = 0
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, titulo = "", subtitulo = "", emailContato = ""):
        self._instance.titulo = titulo
        self._instance.subtitulo = subtitulo
        self._instance.emailContato = emailContato
        self.addVisitante()  # Adicionar um visitante ao criar uma nova instância

    def addVisitante(self):
        self.visitantes += 1

    def get_info(self):
        return f"Título: {self.titulo}\nSubtítulo: {self.subtitulo}\nEmail de Contato: {self.email_contato}\n"


class Cliente:
    def __init__(self):
        self.site_config = SiteConfiguration("Site do Fulano", "Um site de testes", "exemplo@gmail.com")

    def exibir_informacoes(self):
        print(f"--Informações do Site--\n{self.site_config.get_info()}")
        print(f"Número de Visitantes: {self.site_config.visitantes}")


if __name__ == "__main__":
# Teste do Singleton
    cliente = Cliente()
    cliente = Cliente()
    cliente = Cliente()
    cliente4 = Cliente()
    cliente1 = Cliente()
    cliente2 = Cliente()

    cliente.exibir_informacoes()
    print("----")
    cliente2.exibir_informacoes()


