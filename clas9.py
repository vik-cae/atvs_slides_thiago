class AlunoAcademia:
    def __init__(self, nome, idade, peso, altura, mensalidade=120.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = mensalidade

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        print(f"IMC de {self.nome}: {imc:.2f}")
        return imc

    def obter_valor_mensalidade(self):
        if self.idade < 18:
            desconto = 0.2  
            valor_com_desconto = self.mensalidade * (1 - desconto)
            print(f"Aluno menor de idade. Mensalidade com desconto: R${valor_com_desconto:.2f}")
            return valor_com_desconto
        else:
            print(f"Aluno maior de idade. Mensalidade: R${self.mensalidade:.2f}")
            return self.mensalidade


aluno1 = AlunoAcademia("Vitória", 17, 55, 1.65)
aluno1.calcular_imc()
aluno1.obter_valor_mensalidade()

aluno2 = AlunoAcademia("João", 20, 75, 1.80)
aluno2.calcular_imc()
aluno2.obter_valor_mensalidade()
