#5.	Dadas tres variables: nota1, nota2 y nota3 (float), 
# calcula el promedio y declara una variable booleana que indique si el estudiante aprobó (nota mínima: 4.0).

nota1 = int(input("Ingrese una nota: "))
nota2 = int(input("Ingrese una nota: "))
nota3 = int(input("Ingrese una nota: "))
promedio = (nota1+nota2+nota3)/3
aprobado = promedio >= 4

if promedio >= 4: 
    print(f"El estudiante aprobo con proemdio {promedio}")
    print(aprobado)
else: 
    print("El estudiante reprobo ")