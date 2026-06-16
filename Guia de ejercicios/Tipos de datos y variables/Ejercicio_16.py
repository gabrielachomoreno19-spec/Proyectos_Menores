#16.Pide al usuario que ingrese un número del 1 al 12. 
# Muestra a qué mes del año corresponde. Si no está en el rango, muestra “Mes inválido”.
mes = int(input("Ingrese un número (1-12): "))

if mes == 1:
    print("Enero")
elif mes == 2:
    print("Febrero")
elif mes == 3:
    print("Marzo")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Mayo")
elif mes == 6:
    print("Junio")
elif mes == 7:
    print("Julio")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Septiembre")
elif mes == 10:
    print("Octubre")
elif mes == 11:
    print("Noviembre")
elif mes == 12:
    print("Diciembre")
else:
    print("Mes inválido")