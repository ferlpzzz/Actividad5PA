while True:
    print("----Menú Principal----")
    print("1- Ingresar listas de ventas")
    print("2- Mostrar todas las ventas")
    print("3- Calcular la venta mas alta y mas baja")
    print("4- Calcular promedio de ventas")
    print("5- Calcular cuantos dias superaron los Q1000.00")
    print("6- Buscar una venta específica")
    print("7- Clasificar cada venta")
    print("8- Salir")

    option = input("Ingrese una opcion: ")
    sales = []
    match option:
        case "1":
            sale = int(input("Ingrese la venta:"))
            sales.append(sale)

