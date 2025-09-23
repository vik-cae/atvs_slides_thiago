def positivo_ou_negativo(num) :
    if num >= 0:
        return 'P'
    else:
        return 'N'

n = int(input("Digite um número inteiro: "))
print(positivo_ou_negativo(n))
