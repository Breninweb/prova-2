linhas = int(input("quantas linhas a matriz vai ter: "))
colunas = int(input("quantas colunas a matriz vai ter: "))
contador = 0

lista = [[0 for i in range(linhas)] for j in range(colunas)]

for linha in range(linhas):
    lista[linha] = int(input("Escolha o valor: "))

for i in range(4):
    print(lista[i])
    contador = linhas

if contador == linhas:
    print(lista.sort())

print(sum(lista))    

print(max(lista))