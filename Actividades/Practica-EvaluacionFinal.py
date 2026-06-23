import random
habitaciones = {
    "SI-123": {
        "codigo": "SI-123",
        "numero": 101,
        "tipo": "Simple",
        "estado": "Disponible"
    }
}
def menu():
    try:
        print("""----MENU----
1.- Registrar habitación
2.- Mostrar habitación
3.- buscar habitación
4.- Reservar habitación
5.- Liberar habitación
6.- Modificar habitación
7.- Eliminar habitación
8.- Salir 
    """)
        opcion = int(input("Ingrese una opción: "))
        return opcion
    except ValueError:
        print("Ingrese un numero entero, Intentelo de nuevo.")
def registrar_habitacion(nueva_habitacion):


    try: 
        print ("*****Registrar Habitacion*****")
        numero_habitacion = int(input("Ingrese el numero de la habitacion: "))
        print ("1.- Simple / 2.- Doble / 3.- Suite")
        tipo_habitacion = input("Ingrese el tipo de habitacion que desea (escriba ej. simple): ").lower()
        if tipo_habitacion == "simple" or tipo_habitacion == "doble" or tipo_habitacion == "suite": 
            codigo = (f"{tipo_habitacion[:2].upper()}-{random.randint(100,999)}")
            print (codigo)
            estado = "Disponible"
            nueva_habitacion[codigo] = {"Codigo":codigo, "numero" : numero_habitacion, "tipo" : tipo_habitacion, "estado" : estado }
        else:
            print("Ingrese un tipo de habitacion valido")
    except ValueError:
        print("Ingrese un numero entero para el numero de habitacion.")
def mostrar_habitacion(habitaciones):
    print("------Lista de habitaciones------")
    for codigo, datos in habitaciones.items():
        print(f"Codigo: {codigo}")
        print(f"Numero de habitacion: {datos["numero"]}")
        print(f"Tipo: {datos["tipo"]}")
        print(f"Estado : {datos["estado"]}")
        print("_________________________________________")
def buscar_habitacion(habitaciones):
    print("_____________Buscar Habitaciones______________")
    codigo_buscar = input("Ingrese el codigo de la habitacion a buscar: ")
    for codigo, datos in habitaciones.items(): 
        if codigo_buscar == codigo:
            print(f"Codigo: {codigo}")
            print(f"Numero de habitacion: {datos["numero"]}")
            print(f"Tipo: {datos["tipo"]}")
            print(f"Estado : {datos["estado"]}")
            print("_________________________________________")
        else:
            print("Habitacion no encontrada. ")
def reservar_habitacion(habitaciones):
    print("------Reservar habitaciones------")
    codigo_buscar = input("Ingrese el codigo de la habitacion que quiere reservar: ")
    for codigo in habitaciones:
        if codigo_buscar == codigo:
            if habitaciones[codigo]["estado"] == "Disponible":
                habitaciones[codigo]["estado"] = "Ocupado"
                print(f"{codigo} ahora esta ocupada")
            else:
                print("habitación ya está ocupada")
        else: 
            print("La habitacion no existe")
def liberar_habitacion(habitaciones):
    print("------Liberar Habitaciones-------")
    codigo_buscar = input("Ingrese el codigo de la habitacion que quiere liberar: ")
    for codigo in habitaciones:
        if codigo_buscar == codigo:
            if habitaciones[codigo]["estado"] == "Ocupado":
                habitaciones[codigo]["estado"] = "Disponible"
                print(f"{codigo} ahora esta libre")
            else:
                print("La habitacion ya esta libre")
        else: 
            print("La habitacion no existe.")
def modificar_habitacion(habitaciones):
    try:
        print("-------Modificar habitacion------")
        codigo_buscar = input("Ingrese el codigo de la habitacion que quiere modificar: ")
        for codigo in habitaciones:
            if codigo_buscar == codigo:
                nuevonumero = int(input("Ingrese el nuevo numero de habitacion"))
                print ("1.- Simple / 2.- Doble / 3.- Suite")
                nuevotipo = input("Ingrese el tipo de habitacion que desea (escriba ej. simple): ").lower()
                if nuevotipo == "simple" or nuevotipo == "doble" or nuevotipo == "suite":
                    habitaciones[codigo]["numero"] = nuevonumero
                    habitaciones[codigo]["tipo"] = nuevotipo
                    print("Habitacion modificada con exito")
                else: 
                    print("Ingrese un tipo de habitacion valido")
    except ValueError:
        print("Ingrese un numero entero para el numero de habitación")
def eliminar_habitacion(habitaciones):
    print("------Eliminar habitacion-----")
    codigo_buscar = input("Ingrese el codigo de la habitacion que quiere eliminar: ")
    if codigo_buscar in habitaciones:
        del habitaciones[codigo_buscar]
acceso = True
while acceso:
    opcion = menu()
    if opcion == 1:
        registrar_habitacion(habitaciones)
    if opcion == 2:
        mostrar_habitacion(habitaciones)
    if opcion == 3:
        buscar_habitacion(habitaciones)
    if opcion == 4:
        reservar_habitacion(habitaciones)
    if opcion == 5:
        liberar_habitacion(habitaciones)
    if opcion == 6: 
        modificar_habitacion(habitaciones)
    if opcion == 7: 
        eliminar_habitacion(habitaciones)
    if opcion == 8: 
        print("Gracias por usar ")
        acceso = False