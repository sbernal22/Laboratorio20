n = int(input("Ingrese N mayor o igual a 3: "))
while n < 3:
    print("N debe ser mayor o igual a 3")
    n = int(input("Ingrese N mayor o igual a 3: "))
matriz = [[0] * n for _ in range(n)]
numero = 1
fila_inicio = 0
fila_fin = n - 1
col_inicio = 0
col_fin = n - 1
while fila_inicio <= fila_fin and col_inicio <= col_fin:
    for i in range(col_inicio, col_fin + 1):
        matriz[fila_inicio][i] = numero
        numero += 1
    fila_inicio += 1
    for i in range(fila_inicio, fila_fin + 1):
        matriz[i][col_fin] = numero
        numero += 1
    col_fin -= 1
    if fila_inicio <= fila_fin:
        for i in range(col_fin, col_inicio - 1, -1):
            matriz[fila_fin][i] = numero
            numero += 1
        fila_fin -= 1
    if col_inicio <= col_fin:
        for i in range(fila_fin, fila_inicio - 1, -1):
            matriz[i][col_inicio] = numero
            numero+=1
        col_inicio+=1
for fila in matriz:
    print(fila)