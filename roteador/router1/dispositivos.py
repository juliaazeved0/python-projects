
from abc import ABC, abstractmethod

class Dispositivo(ABC):

    marca = None
    modelo = None
    tipo_conexao = None
    
    def __init__(self, marca, modelo, sistema_operacional, tipo_conexao):
        self.marca=marca
        self.modelo=modelo
        self.sistema_operacional=sistema_operacional
        self.tipo_conexao = tipo_conexao

    def get_tipo_conexao(self):
        return self.tipo_conexao
    
    def conectar():
        abstractmethod
    
        
class Notebook(Dispositivo):
    
    def __init__(self, marca, modelo, sistema_operacional,tipo_conexao, possui_mouse, possui_entrada_USB, possui_bateria_removivel):
        super().__init__(marca, modelo, sistema_operacional, tipo_conexao)
        self.possui_mouse = possui_mouse
        self.possui_entrada_USB = possui_entrada_USB
        self.possui_bateria_removivel = possui_bateria_removivel

    
    def conectar(self, tipo_conexao):

        if tipo_conexao == "wifi" or tipo_conexao == "ethernet":
            print(f"Solicitação de conexão para Notebook foi realizada via: {tipo_conexao}")
        else:
            print("Impossível conectar a rede.")



class Smartphone(Dispositivo):

    def __init__(self, marca, modelo, sistema_operacional, tipo_conexao, possui_5g, possui_nfc):
        super().__init__(marca, modelo, sistema_operacional, tipo_conexao)
        self.possui_5g = possui_5g
        self.possui_nfc = possui_nfc

    
    def conectar(self, tipo_conexao):
        
        if tipo_conexao == "wifi":
            print(f"Solicitação de conexão para Smartphone foi realizada via: {tipo_conexao}")
        else:
            print("Impossível conectar a rede.")


