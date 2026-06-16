#13.	Pide al usuario que ingrese una nota. Según el valor, muestra: “Insuficiente” (<4),
#  “Suficiente” (4–5), “Bueno” (5–6), “Excelente” (6–7). Usa elif.

nota = int(input("Ingrese una nota "))
if nota > 1 and nota <4: 
    print ("nota insuficiente ")
elif nota >= 4 and nota < 5: 
    print ("Nota suficiente ")
elif nota >= 5 and nota < 6: 
    print ("Nota buena ")
elif nota >= 6 and nota <= 7: 
    print ("nota excelente")
else: 
    print ("nota no valida")