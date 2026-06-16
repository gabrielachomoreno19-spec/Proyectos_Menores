usuario1 = None 
usuario2 = None
usuario3 = None
contrasena1 = None
contrasena2 = None
contrasena3 = None 

while True: 
    try: 
        menu1 = 0

        while menu1 not in [1, 2, 3]: 
            print("____MENU____")
            print("1) Ingrese sesión")
            print("2) Registrar usuario")
            print("3) Salir")
            menu1 = int(input("Ingrese una opcion: "))
            if menu1 not in [1, 2, 3]: 
                print("Opcion no valida intente de nuevo")

        if menu1 == 1: 
            if usuario1 == None and usuario2 == None and usuario3 == None:
                print("Es necesario registrar un usuario antes ")
                menu1 = 0
                break
            
            usuario_input = input("Ingrese su nombre de usuario: ")
            contrasena_input = input("Ingrese su contraseña: ")

            sesion_activa = False
            if usuario1 is not None and usuario_input == usuario1 and contrasena_input == contrasena1: 
                sesion_activa = True
            elif usuario2 is not None and usuario_input == usuario2 and contrasena_input == contrasena2: 
                sesion_activa = True
            elif usuario3 is not None and usuario_input == usuario3 and contrasena_input == contrasena3: 
                sesion_activa = True
            else: 
                print("Ingreso algun valor incorrecto")

            if sesion_activa: 
                while True: 
                    print("_____Menu_____")
                    print("1) Realizar llamada")
                    print("2) Enviar correro electronico")
                    print("3) cerrar sesion ")
                    menu2 = int(input("Ingrese una opción: "))

                    if menu2 == 1: 
                        try:
                            numero_telefono = input("Ingrese un numero de telefono")
                            if len(numero_telefono) == 9 and numero_telefono.startswith("9"):
                                print(f"Llamando al numero: {numero_telefono}......")
                                print("Llamada exitosa ")
                            else: 
                                print("Error al ingresar un numero de telefono: ")
                        except Exception as e: 
                            print(f"Error encontrado {e}")

                    elif menu2 == 2: 
                        tieneArroba = False
                        correo = input("Ingrese un correo electronico")
                        for i in correo: 
                            if i == "@":
                                tieneArroba = True
                                break
                        if tieneArroba: 
                            mensaje = input("Escriba aca su mensaje: ")
                            print(f"Correo enviado a {correo} con el mensaje {mensaje}")
                        else: 
                            print("Correo no valido ")
                    
                    elif menu2 == 3: 
                        print("Cerrando secion........")
                        break
        elif menu1 == 2:
            print("Registro de usuario")
            if usuario1 == None:
                usuario1 = input("Ingrese su nombre de usuario: ")
                contrasena1 = input("ingrese su contraseña ")
            elif usuario2 == None: 
                usuario2 = input("Ingrese su nombre de usuario: ")
                contrasena2 = input("ingrese su contraseña ")
            elif usuario3 == None: 
                usuario3 = input("Ingrese su nombre de usuario: ")
                contrasena3 = input("ingrese su contraseña ")
            else:
                print("Se alcanzo el limite de usuarios ")
        
        elif menu1 == 3: 
            print("Gracias por usar este programa ")
            break
        else: 
            print("Opcion no valida ")



    except ValueError:
        print("Valor mal ingresado, intente de nuevo")


