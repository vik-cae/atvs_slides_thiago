class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def nome_completo(self):
        print(f"Nome completo: {self.nome} {self.sobrenome}")

    def calcular_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"Salário do mês: R${salario:.2f}")

    def incrementar_valor_hora(self, valor_adicional):
        if valor_adicional > 0:
            self.valor_hora += valor_adicional
            print(f"Novo valor por hora: R${self.valor_hora:.2f}")
        else:
            print("O valor adicional deve ser positivo")


funcionario1 = Funcionario("Vitória", "Caetano", 160, 25)
funcionario1.nome_completo()
funcionario1.calcular_salario()
funcionario1.incrementar_valor_hora(5)
funcionario1.calcular_salario()  
