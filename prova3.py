linhas = int(input("quantas linhas a matriz vai ter: "))
colunas = int(input("quantas colunas a matriz vai ter: "))


matriz = [[0 for i in range(linhas)] for j in range(colunas)]

for linha in range(linhas):
    print(matriz[linha])

