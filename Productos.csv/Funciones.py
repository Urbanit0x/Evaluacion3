import csv
filename = 'inventario.csv'
def menu ():
    print("-Bienvenidos al Sistema de Gestion de inventario-")
    print("[1-] Agregar productos al inventario:")
    print("[2-] Leer el inventario:")
    print("[3-] Clasificar y exportar productor:")
    print("[4-] Salir:")
    opcion = input("Elija una opcion: ")
    return opcion

def Agregar_producto ():
    print(input(float("Ingrese el ID del prodcto")))
    print(input("Ingrese el nombre del producto: "))
    print(input("Ingrese la categoria del producto: [E][T][C]"))
    print(input(float("Ingrese el valor del producto:")))
    with open ('inventario.csv', 'a', newline='') as ID_producto:
        escritor_producto = csv.writer(ID_producto)
        escritor_producto.writerow(ID_producto )
    with open ('inventario.csv', 'a', newline='') as Nombre_producto:
        escritor_producto = csv.writer(Nombre_producto)
        escritor_producto.writerow(Nombre_producto )
    with open ('inventario.csv', 'a', newline='') as Categoria_producto:
        escritor_producto = csv.writer(Categoria_producto)
        escritor_producto.writerow(Categoria_producto)
    with open ('inventario.csv','a', newline='') as Valor_producto:
        escritor_producto = csv.writer(Valor_producto)
        escritor_producto.writerow(Valor_producto)

def Leer_inventario():
    with open('inventario.csv', 'r', newline='') as Nombre_producto: 
        leer_producto = csv.reader(Nombre_producto)
        for row in leer_producto: 
            ID_producto = row [0]
            Nombre_producto = row[1]
            Categoria_producto = row[2]
            Valor_producto = row[3]
        print(f"ID:{ID_producto}, Nombre: {Nombre_producto}, Categoria: {Categoria_producto}, Valor: {Valor_producto}")

         
def Clasificar_Exportar():
    Textil = []
    Electronica = []
    Calzado = []

    
    with open('inventario.csv','r',newline='') as Nombre_producto:
        leer_producto = csv.reader (Nombre_producto)
        for row in leer_producto:
            




      

     







while True:
    opcion = menu()  
    if opcion == '1':
        Agregar_producto()  
    elif opcion == '2':
        Leer_inventario()  
    elif opcion == '3':
        Clasificar_Exportar()  
    elif opcion == '4':
        break 
    else:
        print("Opción no válida. Intente de nuevo.")

