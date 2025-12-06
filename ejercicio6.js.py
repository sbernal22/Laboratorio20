def normalizar(lista, modo):
    if modo not in ["minmax", "zscore", "unit"]:
        print("El modo debe ser 'minmax', 'zscore' o 'unit'")
        return None
    if modo == "minmax":
        minimo = min(lista)
        maximo = max(lista)
        resultado = []
        for x in lista:
            valor = (x - minimo) / (maximo - minimo)
            resultado.append(valor)
        return resultado
    elif modo == "zscore":
        suma = 0
        for x in lista:
            suma += x
        media = suma / len(lista)
        suma_cuadrados = 0
        for x in lista:
            suma_cuadrados += (x - media) ** 2
        varianza = suma_cuadrados / len(lista)
        desviacion = varianza ** 0.5
        if desviacion == 0:
            print("La desviación estándar es cero")
            return None
        resultado = []
        for x in lista:
            valor = (x - media) / desviacion
            resultado.append(valor)
        return resultado
    elif modo == "unit":
        suma_cuadrados = 0
        for x in lista:
            suma_cuadrados += x ** 2
        norma = suma_cuadrados ** 0.5
        if norma == 0:
            print("La norma del vector es cero")
            return None
        resultado = []
        for x in lista:
            valor = x / norma
            resultado.append(valor)
        return resultado
valores = [10, 20, 30]
print(normalizar(valores, "minmax"))
print(normalizar(valores, "zscore"))
print(normalizar(valores, "unit"))
print("Original:", valores)