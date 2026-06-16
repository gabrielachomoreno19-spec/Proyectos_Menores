# 3. Pide al usuario que ingrese su año de nacimiento (como entero) y calcula su edad aproximada. Usa una variable bool para indicar si es mayor de edad y muestra el resultado.
año_de_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2026 - año_de_nacimiento
es_mayor_de_edad = edad >= 18
print(f"Su edad es: {edad} años.")
if es_mayor_de_edad:
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")