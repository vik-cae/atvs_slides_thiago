
def somaImposto(taxaImposto, custo):

    valor_imposto = (taxaImposto / 100) * custo

    custo_com_imposto = custo + valor_imposto
    return custo_com_imposto

custo_item = float(input("Digite o custo do item: "))
taxa = float(input("Digite a taxa de imposto em %: "))


valor_final = somaImposto(taxa, custo_item)

print(f"O valor do item com imposto é: R$ {valor_final:.2f}")
