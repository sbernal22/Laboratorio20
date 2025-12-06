import numpy as np
def normalizar(lista, modo):
    if modo not in ["minmax", "zscore", "unit"]:
        print("El modo debe ser 'minmax', 'zscore' o 'unit'")
        return None
    arr = np.array(lista)
    if modo == "minmax":
        minimo=np.min(arr)
        maximo=np.max(arr)
        if maximo-minimo == 0:
            print("Error: todos los valores son iguales")
            return None
        return ((arr-minimo)/(maximo-minimo)).tolist()
    elif modo == "zscore":
        media = np.mean(arr)
        desviacion = np.std(arr)
        if desviacion == 0:
            print("La desviación estándar es cero")
            return None
        return ((arr - media) / desviacion).tolist()
    elif modo == "unit":
        norma = np.linalg.norm(arr)
        if norma == 0:
            print("La norma del vector es cero")
            return None
        return (arr / norma).tolist()
valores = [10, 20, 30]
print(normalizar(valores, "minmax"))
print(normalizar(valores, "zscore"))
print(normalizar(valores, "unit"))
print("Original:", valores)