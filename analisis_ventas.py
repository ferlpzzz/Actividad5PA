sales = []
while True:
    print("----Menú Principal----")
    print("1- Ingresar listas de ventas")
    print("2- Mostrar todas las ventas")
    print("3- Calcular la venta mas alta y mas baja")
    print("4- Calcular promedio de ventas")
    print("5- Calcular cuantos dias superaron los Q1000.00")
    print("6- Clasificar cada venta")
    print("7- Salir")

    option = input("Ingrese una opcion: ")
    match option:
        case "1":
            n= int(input("Ingrese cuantos dias desea ingresar: "))
            for i in range(0, n):
                while True:
                    try:
                        sale = int(input("Ingrese la venta: "))
                        if sale >= 0:
                            sales.append(sale)
                            break
                        else:
                            print("El número debe de ser positivo.")
                    except ValueError:
                        print("Debe ingresar un número entero.")
        case "2":
            if len(sales) == 0:
                print("No se han registrado ventas.")
            else:
                print("\nVentas Registradas:")
                for i, sale in enumerate(sales, 1):
                    print(f"Día #{i}: Q{sale}")
        case "3":
            if len(sales) == 0:
                print("No se han registrado ventas para analizar.")
            else:
                max_sale = min_sale = sales[0]
                for sale in sales:
                    if sale > max_sale:
                        max_sale = sale
                    if sale < min_sale:
                        min_sale = sale
                print(f"Venta más alta: Q{max_sale}")
                print(f"Venta más baja: Q{min_sale}")
        case "4":
            if len(sales) == 0:
                print("No se han registrado ventas para analizar.")
            else:
                average = sum(sales) / len(sales)
                print(f"El promedio de ventas es: Q{average:.2f}")
        case "5":
            if len(sales) == 0:
                print("No se han registrado ventas para analizar.")
            else:
                count = sum(1 for sale in sales if sale > 1000)
                print(f"Los días que superaron los Q1000 son: {count}")
        case "6":
            if len (sales) == 0:
                print("No se han registrado ventas para analizar.")
            else:
                print("\nClasificación de ventas: ")
                for i, sale in enumerate(sales, 1):
                    if sale > 1000:
                        classif = "Venta Alta"
                    elif sale >= 500:
                        classif = "Venta Media"
                    else:
                        classif = "Venta baja"
                    print(f"Día {i}: Q{sale} ({classif})")
        case "7":
            print("Muchas gracias por usar este programa")
            print("Cerrando programa...")
            break
        case _:
            print("Opción no válida, por favor ingresa una opción válida.")





