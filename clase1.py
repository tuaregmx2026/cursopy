import json
clientes = []
from datetime import datetime
fecha_actual = datetime.now().year

#***********************************************************************************
# Función para crear clientes
#***********************************************************************************
def crear_clientes():


    nombre = input("Ingrese el nombre del cliente: ")
    yearnac = int(input("Ingrese el año de nacimiento del cliente: "))
    
    edad = fecha_actual - yearnac

    cliente = {
        "nombre": nombre,
        "yearnac": yearnac,
        "edad":edad
    }

    clientes.append(cliente)
    guardar_clientes()

    return edad

#***********************************************************************************
# Función para guardar clientes
#***********************************************************************************
def guardar_clientes():

    with open("clientes.json", "w") as archivo:

        json.dump(
            clientes,
            archivo,
            indent=4
        )
def cargar_clientes():

    try:

        with open("clientes.json", "r") as archivo:

            return json.load(archivo)

    except FileNotFoundError:

        return []
#***********************************************************************************
# Función para crear el menú de opciones
#***********************************************************************************
def menu():

 while True:

    opciones = int(input(
        "1. Nuevo Cliente\n"
        "2. Listar Clientes\n"
        "3. Editar Cliente\n"
        "4. Buscar un Cliente\n"
        "5. Eliminar un Cliente\n"
        "6. Salir\n"
        "Ingrese una opción: "
    ))

    if opciones == 1:

        result = crear_clientes()

        print("Cliente creado exitosamente.")
        print(f"El cliente tiene {result} años.")
        
    elif opciones == 2:

        for cliente in clientes:
            print(f"Nombre Completo: {cliente['nombre']}, Año de nacimiento: {cliente['yearnac']}, Edad: {cliente['edad']}")
    
        
    elif opciones == 3:

        nombre = input("Ingrese el nombre del cliente a editar: ")
        for cliente in clientes:
            if cliente['nombre'] == nombre:
                nuevo_yearnac = int(input("Ingrese el nuevo año de nacimiento del cliente: "))
    
                nuevo_edad = fecha_actual - nuevo_yearnac

                cliente['yearnac'] = nuevo_yearnac
                cliente['edad'] = nuevo_edad

                print("Cliente editado exitosamente.")
                break
        else:
            print("Cliente no encontrado.")
        

    elif opciones == 4:
        encontrado = False

        nombre = input("Ingrese el nombre del cliente a buscar: ")
        
        for cliente in clientes:
            if cliente['nombre'] == nombre:
                encontrado = True
                print(f"Nombre Completo: {cliente['nombre']}, Año de nacimiento: {cliente['yearnac']}, Edad: {cliente['edad']}")
        if not encontrado:
            print("Cliente no encontrado.")
        
    elif opciones == 5:
        nombre = input("Ingrese el nombre del cliente a eliminar: ")
        
        for cliente in clientes:
            if cliente['nombre'] == nombre:
                clientes.remove(cliente)
                guardar_clientes()
                print("Cliente eliminado exitosamente.")
                break
        else:
            print("Cliente no encontrado.")
          
    elif opciones == 6:

        print("Bye.")
        exit()

    else:

        print("Opción inválida")
        
#***********************************************************************************
# Función para ejecutar el programa
#***********************************************************************************
clientes = cargar_clientes()


menu()

