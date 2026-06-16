#15.	Solicita una clave secreta. Si la clave es incorrecta tres veces,
#  muestra un mensaje de “Acceso bloqueado”. Usa if dentro de un control de intentos.
clave = "12345"
intentos = 0
acceso = False

while intentos < 3: 
    entrada = input(f"Ingrese la contraseña intento {intentos+1}: ")
    if entrada == clave: 
        print ("Contraseña correcta!!")
        acceso = True
        break
    else: 
        print ("Contraseña incorrecta!!")
        intentos = intentos + 1

if acceso:
    print("Bienvendio sigma")