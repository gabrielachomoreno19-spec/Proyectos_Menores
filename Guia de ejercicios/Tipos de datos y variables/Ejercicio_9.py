#9.	Declara una variable con tu nombre completo. Extrae solo el primer nombre y crea una nueva variable que 
# almacene el saludo “Hola, [nombre]”.

nombre_completo = input("Ingresa tu nombre completo ")
partes = nombre_completo.split()
primer_nombre = partes[0]

print(f"Hola {primer_nombre} ")