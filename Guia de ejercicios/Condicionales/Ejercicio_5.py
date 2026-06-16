#5.	Pide al usuario que ingrese su nota final (entre 1.0 y 7.0). 
# Muestra: “Reprobado” si es menor a 4.0, “Aprobado” si es mayor o igual a 4.0.
nota = 1
programa = True

while programa: 
    if nota >=1 and nota <=7: 
        nota = int(input("Ingrese su nota: "))
        if nota >= 4: 
            print("Aprobo")
        else: 
            print("Reprobo")
        salir = int(input("Ingrese 0 para salir o cualquier numero para ingresar otra nota: "))   
        if salir == 0: 
            programa = False
