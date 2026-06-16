#6.	Crea un sistema de validación para ingresar a una fiesta: pide edad y si tiene entrada (sí o no).
#  Permite el ingreso solo si tiene ambos requisitos.


ticket = False

while not ticket:
    try: 
        edad = int(input("Ingrese su edad "))
        if edad < 18: 
            print("Los menores de 18 años no pueden pasar")
            break

        entrada = input("Tiene una entrada (si o no)").lower()
        while entrada != "si" and entrada != "no": 
            entrada = input("Tiene una entrada (si o no)").lower() 
            if entrada == "no": 
                entrada = input("Desea obtener gratis una entrada? (si o no)").lower()
                if entrada == "no":
                    break
        
        ticket = edad >= 18 and entrada == "si"

       
        
    except ValueError:
        print("Ingrese una edad correcta")
    
if ticket: 
    print("bienvendio")
elif edad < 18: 
    print ()
else: 
    print("No se puede pasar sin entrada")
    