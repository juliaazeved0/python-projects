
from abc import ABC

class Dispositivo(ABC): 
    def __init__(self, nome:str, senha: str):
        self.nome = nome
        self.ip = None
        self.senha = senha

    def conectar(self, roteador: "Roteador"):
        print("Conectando com o roteador")
        roteador.aceitar(self) 
      

class Roteador: 
    def __init__(self):
        self.contador = 0
        self.lista_dispositivo = []
        self.senha = "12345678"


    def aceitar(self, dispositivo: "Dispositivo"): #esta dentro da classe primeiro parametro obrigatorio é o self
        
        if self.senha == dispositivo.senha: 
            self.contador+=1
            dispositivo.ip = f"102.90.51.{self.contador}"
            self.lista_dispositivo.append(dispositivo)
            print(f"Conexão aceita - {dispositivo.nome} - {dispositivo.ip}")
        else: print("Senha incorreta.")



    def listar_dispositivos(self):
        
        for dispositivo in self.lista_dispositivo:
            print(f"{dispositivo.nome} \n")


class Notebook(Dispositivo): 
    pass

class Smartphone(Dispositivo): 
    pass
