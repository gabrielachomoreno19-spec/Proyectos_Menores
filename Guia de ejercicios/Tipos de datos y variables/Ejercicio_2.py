# 2. Declara tres variables: una booleana que indique si tienes hambre, un número entero con la cantidad de horas desde tu última comida y un float con el nivel de hambre del 1.0 al 10.0. Imprime un mensaje distinto según el nivel de hambre.
tengo_hambre = True
horas_desde_ultima_comida = 5
nivel_de_hambre = 7.5
if nivel_de_hambre >= 8.0:
    print("¡Tengo mucha hambre!")
elif nivel_de_hambre >= 5.0:
    print("Tengo algo de hambre.")
else:
    print("No tengo hambre.")


    