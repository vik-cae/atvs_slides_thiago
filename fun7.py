def calcular_salario(horas_trabalhadas, valor_hora):
   

    carga_base = 40  
    if horas_trabalhadas <= carga_base:
       
        salario = horas_trabalhadas * valor_hora
    else:
        
        horas_extra = horas_trabalhadas - carga_base
        salario = (carga_base * valor_hora) + (horas_extra * valor_hora * 1.5)
    return salario


horas = float(input("Digite o número de horas trabalhadas: "))
valor = float(input("Digite o valor da hora trabalhada: R$ "))

salario_total = calcular_salario(horas, valor)
print(f"O salário a ser pago é: R$ {salario_total:.2f}")