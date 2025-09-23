av = int(input("digite a quantidade de avaliacao: "))
notas = []
i= 0
while i <= av:
    nota = float(input(f"digite a sua nota da avaliacao : "))
    notas.append(nota)
    i+=1

resul = sum(notas) / av
print(f"media = {resul}")