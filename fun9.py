import math

def calcularTempo(minutos):

    if minutos <= 15:
        valor_base = 0.0
    else:
        valor_hora_inicial = 9.0
        valor_hora_adicional = 1.5

        horas = minutos / 60
        if horas <= 1:
            valor_base = valor_hora_inicial
        else:
            horas_adicionais = math.ceil(horas - 1)
            valor_base = valor_hora_inicial + (horas_adicionais * valor_hora_adicional)


    pis = valor_base * 0.0033     
    cofins = valor_base * 0.002   
    icms = valor_base * 0.17      

    total = valor_base + pis + cofins + icms


    recibo = {
        "valor_base": valor_base,
        "PIS": pis,
        "COFINS": cofins,
        "ICMS": icms,
        "total": total
    }
    return recibo

tempo = int(input("Digite o tempo de estacionamento em minutos: "))

recibo = calcularTempo(tempo)


print("\n===== RECIBO ESTACIONAMENTO =====")
print(f"Tempo utilizado: {tempo} minutos")
print(f"Valor base: R$ {recibo['valor_base']:.2f}")
print(f"PIS (0,33%): R$ {recibo['PIS']:.2f}")
print(f"COFINS (0,20%): R$ {recibo['COFINS']:.2f}")
print(f"ICMS (17%): R$ {recibo['ICMS']:.2f}")
print(f"Total a pagar: R$ {recibo['total']:.2f}")
print("=================================")
