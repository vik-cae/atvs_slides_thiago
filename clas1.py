class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def mostra_nome(self):
        print(f"nome: {self.nome}")

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
        print(f"idade alterada para: {self.idade}")

    def imprimir_endereco(self):
        print(f"o endereço é: {self.endereco}")

pessoa1 = Pessoa("Vitoria", 25, "rua das papoulas,121")
pessoa1.mostra_nome()
pessoa1.alterar_idade(17)
pessoa1.imprimir_endereco()
