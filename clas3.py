class Aluno:
    def __init__(self, nome, RA, n1,n2,n3,n4):
        self.nome = nome
        self.ra = RA
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4

    def mostrar_situacao (self):
        res = (self.n1 + self.n2 + self.n3 + self.n4)/4
        print(f"media = {res}")
        if res >= 7:
            print("aprovado")
        elif 5 <= res <= 6.9:
            print("exame")
        else:
            print("reprovado")

aluno1 = Aluno("joao",123,9,10,7,8)
aluno1.mostrar_situacao()
