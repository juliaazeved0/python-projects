from dispositivos import Notebook, Smartphone

class Roteador:
    
    conexao = None
    
    def __init__ (self, conexao):
        self.conexao = conexao

    def set_conexao(self, conexao):
        self.conexao = conexao
    
    def aceitar(self, dispositivo):
        
        if isinstance(dispositivo, Notebook):
            dispositivo.conectar(self.conexao)

        elif isinstance(dispositivo, Smartphone):
            dispositivo.conectar(self.conexao)


class Conectar:
    
    notebook1 = Notebook("Asus", "Vivobook", "Ubuntu", "wifi", True, True, True)
    smartphone1 = Smartphone("Apple", "XS", "IOS", "5g", True, True)
    roteador = Roteador(None)
    roteador.set_conexao(notebook1.get_tipo_conexao())    
    roteador.aceitar(notebook1)
    roteador.set_conexao(smartphone1.get_tipo_conexao())
    roteador.aceitar(smartphone1)
  
