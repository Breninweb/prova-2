matriz = [
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

diagonal = 1

matriz[0][0] = diagonal   
matriz[1][1] = diagonal
matriz[2][2] = diagonal    
matriz[3][3] = diagonal


for i in range(4):
    print(matriz[i])
    