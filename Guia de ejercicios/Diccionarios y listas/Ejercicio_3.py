estudiantes = {}
for i in range (1): 
    print(f"---Estudiante numero {i + 1}---")
    nombre = input("Ingrese nombre del estudiante: ")
    lista_notas = []
    for j in range (3):
        nota = float(input(f"Ingrese la {j+1}° nota: "))
        lista_notas.append(nota)
    
    estudiantes[nombre] = lista_notas

for nombre, nota in estudiantes.items():
    print (nombre, sum(nota)/len(nota))
