#2.	Solicita la edad de una persona y muestra un mensaje que diga si es menor o mayor de edad.

edad = 0
la_verdad = edad == 0
while la_verdad:
    try:
        edad = int(input("Ingrese edad: "))
        if edad >= 18:
            print("es mayor de edad")
            la_verdad = False
        elif edad <=18 and edad >=1:
            print("Es menor de edad")
            la_verdad = False
    except ValueError :
        print (f"Error detectado")