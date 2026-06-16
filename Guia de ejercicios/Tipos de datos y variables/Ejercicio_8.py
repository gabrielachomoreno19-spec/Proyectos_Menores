#8.	Simula un sistema de entrada a un evento. Declara una variable edad (int), 
# tiene_entrada (bool) y nombre_evento (str). Imprime si puede o no entrar.

edad = 20 
nombre_evento = "Evento sigma"
tiene_entrada = False

if tiene_entrada == False: 
    print("Usted no tiene entrada,¿Desea comprar una?")
    respuesta = int(input("1: para si / 2: para no: "))
    if respuesta == 1: 
        tiene_entrada = True
        print("Compra realizada")

if tiene_entrada and edad > 18: 
    print(f"Bienvenido al {nombre_evento}")