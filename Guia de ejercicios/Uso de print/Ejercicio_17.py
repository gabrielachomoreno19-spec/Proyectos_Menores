#17.	Haz que el programa imprima una barra de progreso simple,
#  como: [#####-----] 50%, usando concatenación de strings y símbolos.

porcetnaje = int(input("Ingrese la cantidad de porcentaje en multiplos de 10: "))
total_barra = 10

barra_lleno = porcetnaje//10 
barra_vacia = total_barra-barra_lleno
barra = ("#" * barra_lleno) + ("-" * barra_vacia)
print (barra)
