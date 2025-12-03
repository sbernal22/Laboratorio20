ingreso_mensual = float(input("Ingrese el ingreso mensual: "))
ingreso_anual = ingreso_mensual * 14
impuesto_total = 0
if ingreso_anual > 0:
    monto = min(ingreso_anual, 20000)
    impuesto = 0
    impuesto_total += impuesto
    print("Impuesto por tramo:", impuesto)
if ingreso_anual > 20000:
    monto = min(ingreso_anual - 20000, 30000)
    impuesto = monto * 10 / 100
    impuesto_total += impuesto
    print("Impuesto por tramo:", impuesto)
if ingreso_anual > 50000:
    monto = min(ingreso_anual - 50000, 50000)
    impuesto = monto * 20 / 100
    impuesto_total += impuesto
    print("Impuesto por tramo:", impuesto)
if ingreso_anual > 100000:
    monto = ingreso_anual - 100000
    impuesto = monto * 30 / 100
    impuesto_total += impuesto
    print("Impuesto por tramo:", impuesto)
tasa_efectiva = (impuesto_total / ingreso_anual) * 100

print("Total de impuestos:", impuesto_total)
print(f"Tasa efectiva real: {tasa_efectiva:.2f}%")