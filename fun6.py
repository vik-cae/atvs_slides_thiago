def montar_tabela(preco_unitario):
    print("Itens  |  Valor")
    print("----------------")
    for quantidade in range(1, 51):  
        valor_total = quantidade * preco_unitario
        print(f"{quantidade:5}  |  R$ {valor_total:.2f}")


preco = 1.99
montar_tabela(preco)