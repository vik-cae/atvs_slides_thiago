import datetime  

class Agenda:
    def __init__(self, dia, mes, ano, anotacao=""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = anotacao

    def validar_data(self):
        try:
            data = datetime.date(self.ano, self.mes, self.dia)
            print(f"Data válida: {data.strftime('%d/%m/%Y')}")
            return True
        except ValueError:
            print("Data inválida!")
            return False

    def anotar_tarefa(self, anotacao):
        if self.validar_data():
            self.anotacao = anotacao
            print("Tarefa anotada com sucesso!")

    def mostrar_anotacao(self):
        if self.anotacao:
            print(f"Tarefa para {self.dia:02d}/{self.mes:02d}/{self.ano}: {self.anotacao}")
        else:
            print(f"Não há anotações para {self.dia:02d}/{self.mes:02d}/{self.ano}.")


agenda1 = Agenda(23, 9, 2025)
agenda1.validar_data()
agenda1.anotar_tarefa("Estudar Python")
agenda1.mostrar_anotacao()

agenda2 = Agenda(31, 2, 2025)
agenda2.anotar_tarefa("Reunião") 
