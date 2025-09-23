class Carro:
    def __init__(self, marca, modelo, cor, ano, valor, consumo, nivel=0):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel  
        self.consumo = consumo  

    def abastecer(self, litros):
        if litros > 0:
            self.nivel += litros
            print(f"Abastecido {litros} litros. Nível atual: {self.nivel:.2f} litros.")
        else:
            print("O valor a abastecer deve ser positivo.")

    def andar(self, distancia):
        if distancia > 0:
            combustivel_gasto = distancia / self.consumo
            if combustivel_gasto <= self.nivel:
                self.nivel -= combustivel_gasto
                print(f"Percorridos {distancia} km. Combustível gasto: {combustivel_gasto:.2f} litros.")
            else:
                print("Combustível insuficiente para percorrer essa distância.")
        else:
            print("A distância deve ser positiva.")

    def verificar_nivel(self):
        print(f"Nível atual do tanque: {self.nivel:.2f} litros.")

    def calcular_imposto(self):
        ipva = self.valor * 0.035
        print(f"IPVA a pagar: R${ipva:.2f}")
        return ipva



carro1 = Carro("Toyota", "Corolla", "Prata", 2022, 120000, consumo=12)
carro1.abastecer(40)
carro1.andar(100)
carro1.verificar_nivel()
carro1.calcular_imposto()
