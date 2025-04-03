import datetime

class DataAtual:

    def imprime_data(self):
        now = datetime.datetime.now()
        print("Data atual:", now.strftime("%d/%m/1"
        "%Y"))

    def imprime_hora(self):
        now = datetime.datetime.now()
        print("Hora atual:", now.strftime("%H:%M"))

    def imprime_data_hora(self):
        now = datetime.datetime.now()
        print("Data e hora atual:", now.strftime("%c"))

    def menu(self):
        print("1 - Imprimir data\n2 - Imprimir hora\n3 - Imprimir data e hora")
        option = int(input("Digite o número correspondente: "))
        self.select_option(option)
        return self.menu()
        
    def select_option(self, option):
        match option:
            case 1:
                self.imprime_data()
            case 2:
                self.imprime_hora()
            case 3: 
                self.imprime_data_hora()
            case _:
                print("Opção inválida!")

data = DataAtual()
data.menu()
