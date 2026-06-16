frutas = ["manzana", "pera", "manzana", "uva", "pera", "manzana"]


cont_frutas= {}
for fruta in frutas:
    if fruta in cont_frutas: 
        cont_frutas[fruta] += 1
    else: 
        cont_frutas[fruta] = 1

for nombre_fruta, contador in cont_frutas.items():
    print (f"{nombre_fruta} :  {contador}") 
    