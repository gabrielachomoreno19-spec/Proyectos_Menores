personas = {}

for i in range (3): 
    print(f"Ingrese el usuario {i+1}: ")
    nombre = input("Ingrese nombre: ")
    contacto = input("ingrese numero de contacto: ")
    personas[nombre] = contacto
    
for nombre, contacto in personas.items():
    print(nombre )  