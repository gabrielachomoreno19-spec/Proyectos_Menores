ventas = {"Diego" : [],
          "Laura" : [],
          "Carlos" : []
          }
acceso = True
while acceso:    
    try:
            print("----Menu Ventas----")
            print("""1. Registrar venta
2. Ver total vendido por vendedor
3. Ver ventas de un vendedor
4. Mostrar vendedor con más ventas
5. Salir""")
            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1: 
                print("\n----Registrar venta----")
                print("-- Seleccion un vendedor --")
                print("1. Diego")
                print("2. Laura")
                print("3. Carlos")
                vendedor_opc = int(input("Ingrese el numero del vendedor: "))
                if vendedor_opc == 1:
                    vendedor_elegido = "Diego"
                elif vendedor_opc == 2:
                    vendedor_elegido = "Laura"
                elif vendedor_opc == 3:
                    vendedor_elegido = "Carlos"
                else:
                    print("Vendedor no válido.")
                    continue

                monto = int(input("Ingrese el monto de la venta: "))
                ventas[vendedor_elegido].append(monto)
                print("Venta registrada con exito")
            if opcion == 2: 
                print("\n-- Seleccion un vendedor --")
                print("1. Diego")
                print("2. Laura")
                print("3. Carlos")
                vendedor_opc = int(input("Ingrese el numero del vendedor: "))
                if vendedor_opc == 1: 
                    total_diego = sum(ventas['Diego'])
                    print(f"Diego ha vendido en total: ${total_diego}")
                if vendedor_opc == 2:
                    total_Laura = sum(ventas['Laura'])
                    print(f"Laura ha vendido en total: ${total_Laura}")
                if vendedor_opc == 3: 
                    total_carlos = sum(ventas["Carlos"])
                    print(f"Carlos ha vendido en total: ${total_carlos}")
                else: 
                    print("Selcción no valida")
            if opcion == 3: 
                print("\n-- Seleccion un vendedor --")
                print("1. Diego")
                print("2. Laura")
                print("3. Carlos")
                vendedor_opc = int(input("Ingrese el numero del vendedor: "))
                if vendedor_opc == 1:
                    vendedor_elegido = "Diego"
                elif vendedor_opc == 2:
                    vendedor_elegido = "Laura"
                elif vendedor_opc == 3:
                    vendedor_elegido = "Carlos"
                else:
                    print("Vendedor no válido.")
                    continue
                
                lista_ventas = ventas[vendedor_elegido]
                print (f"El vendedor/a {vendedor_elegido} vendio: {lista_ventas}")
            if opcion == 4: 
                mejor_vendedor = max(ventas, key=ventas.get)
                print("El mejor vendedor es:", mejor_vendedor)
            
                    
    except ValueError:
        print("Ingrese un valor correcto")