def qtd_digitos(numero: int) -> int:

    return len(str(numero)) 

n = int(input("Digite um número inteiro: "))
print(f"O número {n} tem {qtd_digitos(n)} dígitos.")
