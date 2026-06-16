#14.	Pide al usuario su edad y si tiene licencia.
#  Solo si tiene ambas condiciones puede conducir. Usa un if anidado.

edad = int(input("Ingrese su edad"))
licencia = True

if edad > 18 and licencia: 
    print("usted puede conducir ")
else: 
    print("Usted no puede conducir ")
