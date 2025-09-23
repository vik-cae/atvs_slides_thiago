class Conta:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def Depositar(self, valor):
        if valor> 0:
            self.saldo += valor
            print(f"deposito de R${valor:.2f} realizado com sucesso")

        else:
            print("o valor do deposito de ser positivo")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"saque de R${valor:.2f} realizado com sucesso")

            else:
                print("saldo insuficientepara o saque")
        else: 
            print(f"o valor do saque deve ser positivo")

    def imprimir_saldo(self):
        print(f"Saldo atual da conta {self.numero} ({self.nome}): R${self.saldo:.2f}")

conta1 = Conta("Vitória", "123.456.789-00", 1001, 500)
conta1.imprimir_saldo()
conta1.Depositar(200)
conta1.sacar(100)
conta1.sacar(700)  # Tentativa de saque maior que o saldo
conta1.imprimir_saldo()