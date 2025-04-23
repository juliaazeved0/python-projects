 # quando chama o scrpit pela linha de comando ele executa essa sessao

from models import (
    Roteador, 
    Notebook, 
    Smartphone
)

if __name__ == "__main__":
    
    roteador = Roteador()
    notebook = Notebook("Asus Vivobook", "38472")
    notebook.conectar(roteador)
    print("------------------------------")
    smart = Smartphone("Zenfone", "12345678")
    smart.conectar(roteador)

    smart = Smartphone("Samsung Galaxy A7", "12345678")
    smart.conectar(roteador)
    roteador.listar_dispositivos()

