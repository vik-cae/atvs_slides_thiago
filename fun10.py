def simular_financiamento(valor_veiculo, entrada, taxa_juros, parcelas):

    valor_financiado = valor_veiculo - entrada
    

    i = taxa_juros / 100

    parcela = valor_financiado * (i * (1 + i) ** parcelas) / ((1 + i) ** parcelas - 1)

    total_pago = parcela * parcelas
    

    juros_pago = total_pago - valor_financiado
    
    financiamento = {
        "valor_financiado": valor_financiado,
        "parcela": parcela,
        "total_pago": total_pago,
        "juros_pago": juros_pago
    }
    
    return financiamento

valor_veiculo = float(input("Digite o valor do veículo: R$ "))
entrada = float(input("Digite o valor da entrada: R$ "))
taxa = float(input("Digite a taxa de juros mensal (%): "))
parcelas = int(input("Digite o número de parcelas: "))

resultado = simular_financiamento(valor_veiculo, entrada, taxa, parcelas)

print("\n===== SIMULAÇÃO DE FINANCIAMENTO =====")
print(f"Valor financiado: R$ {resultado['valor_financiado']:.2f}")
print(f"Valor de cada parcela: R$ {resultado['parcela']:.2f}")
print(f"Total pago ao final: R$ {resultado['total_pago']:.2f}")
print(f"Total de juros pagos: R$ {resultado['juros_pago']:.2f}")
print("======================================")
