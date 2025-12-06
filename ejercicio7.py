estudiantes = []
def agregar_estudiante():
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    promedio = float(input("Ingrese promedio: "))
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }
    estudiantes.append(estudiante)
def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
    else:
        print("Lista de estudiantes:")
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Promedio: {estudiante['promedio']}")
def mostrar_mejor_promedio():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados")
    else:
        mejor = estudiantes[0]
        for estudiante in estudiantes:
            if estudiante['promedio']>mejor['promedio']:
                mejor = estudiante
        print("Mejor estudiante:")
        print(f"Nombre: {mejor['nombre']}, Edad: {mejor['edad']}, Promedio: {mejor['promedio']}")
def buscar_por_nombre():
    nombre = input("Ingrese nombre a buscar: ")
    encontrado = False
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre:
            print("Estudiante encontrado:")
            print(f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Promedio: {estudiante['promedio']}")
            encontrado = True
            break
    if not encontrado:
        print("Estudiante no encontrado")
def eliminar_por_nombre():
    nombre = input("Ingrese nombre a eliminar: ")
    encontrado = False

    for i in range(len(estudiantes)):
        if estudiantes[i]['nombre'] == nombre:
            estudiantes.pop(i)
            print("Estudiante eliminado")
            encontrado = True
            break
    if not encontrado:
        print("Estudiante no encontrado")
while True:
    print("Menú")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Mostrar estudiante con mejor promedio")
    print("4. Buscar por nombre")
    print("5. Eliminar por nombre")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        mostrar_mejor_promedio()
    elif opcion == "4":
        buscar_por_nombre()
    elif opcion == "5":
        eliminar_por_nombre()
    elif opcion == "6":
        break
    else:
        print("Opción inválida")