def calcular_multa(peso_peixes):
   
    limite = 50  
    valor_multa_por_kg = 4.0 

    if peso_peixes > limite:
        excesso = peso_peixes - limite
        multa = excesso * valor_multa_por_kg
    else:
        excesso = 0
        multa = 0

    return excesso, multa


peso = float(input("Digite o peso de peixes trazido (Kg): "))

excesso, multa = calcular_multa(peso)

print(f"Peso excedente: {excesso:.2f} Kg")
print(f"Valor da multa: R$ {multa:.2f}")
