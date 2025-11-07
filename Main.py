import csv
import os
NOMBRE_ARCHIVO = "paises.csv"

def obtener_datos():
    
    lista_paises = []
        #Crea el archivo si no existe
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf_8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            #Escribe la primera fila del CSV, o sea, los encabezados
            escritor.writeheader()

            return lista_paises
    
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf_8") as archivo:
        #Lee el formato csv interpreta las columnas
        lector = csv.DictReader(archivo)
        #Recorre y crea un diccionario y agregar cada diccionario a la lista
        for fila in lector:
            lista_paises.append({"nombre": fila["nombre"], "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]), "continente": fila["continente"] })

    return lista_paises
        

#FUNC PARA AGREGAR PAIS AL CSV
def agregar_pais_archivo(pais):
    with open(NOMBRE_ARCHIVO, "a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writerow(pais)


#Func para ingresar paises (1)
def ingresar_pais():
    while True:
        print("\n")
        print("------ INGRESA UN PAIS ------")
        nombre = input("Ingrese el nombre del pais:  ").strip()

        #Comprueba si el pais ya existe
        if existe_dato(nombre):
            print("Este pais ya fue agregado previamente.")
            continue # Vuelve al inicio del while  
    
        if nombre == "":
            print("Error al ingresar el pais")
            continue

        nombre = nombre.lower()
        
        poblacion = input("Ingrese su poblacion: ").strip()
        #Comprueba que sea un numero valido
        if not validar_numero(poblacion):
            print("Error al ingresar el numero de poblacion")
            continue

        poblacion = int(poblacion)

        superficie = input("Ingrese su superficie: ").strip()

        if not validar_numero(superficie):
            print("Error al ingresar la superficie")
            continue

        superficie = int(superficie)

        continente = input("Ingrese el continente del pais:  ").strip()
    
        if continente == "":
            print("Error al ingresar el continente")
            continue

        continente = continente.lower()
        
        break

    agregar_pais_archivo({"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente })
    print("| Lista de paises actualizada! |")


#FUNC PARA ACTUALZIAR DATOS (2)
def actualizar_datos():
    lista_paises = obtener_datos()
    print("Actualizar los datos de Poblacion y Superficie")
    nombre = input("Ingresa el nombre del pais que desee actualizar los datos").strip().lower()
    
    nombre_pais_encontrado = None

    for paises in lista_paises:
        if paises["nombre"].lower() == nombre.lower():
            nombre_pais_encontrado = nombre
            break

    if not nombre_pais_encontrado:
        print(f"Error: El pais '{nombre}' no fue encontrado.")
        return

    poblacion = input(f"Ingrese la poblacion de {nombre} que desea actualizar: ")
    
    while not validar_numero(poblacion):
        print("Error al ingresar la poblacion.")
        ejemplares = input(f"Ingrese la poblacion de {nombre} que desea actualizar: ")

    ejemplares = int(ejemplares)

    





def existe_dato(dato):
    lista_paises = obtener_datos()

    for paises in lista_paises:
        if paises["nombre"].lower() == dato.strip().lower():
            return True
        
    return False


    #FUNC PARA VALIDAR NUMERO
def validar_numero(numero):
    numero = numero.strip()
    if numero.isdigit():
        numero = int(numero)
        return True
    
    return False


def mostrar_menu():
    while True:
        print("\n")
        print("******** MENU INFO PAISES ********")
        print("1 agregar un país")
        print("2 Actualizar datos de un país")
        print("3 Buscar un país")
        print("4 Filtrar países")
        print("5 Ordenar países")
        print("6 Mostrar estadísticas")
        print("7 Salir")
        print("*"*16)

        opcion_menu = input("Ingrese una opcion: ").strip()

        match opcion_menu:
            case "1":
                ingresar_pais()
            case "2":
                actualizar_datos()
            case "3":
                break#buscar_paises()
            case "4":
                break#filtrar_paises()
            case "5":
                break#ordenar_paises()
            case "6":
                break#mostrar_estadisticas()
            case "7":
                break#break()
            case __:
                print("La opcion seleccionada no es valida.")
mostrar_menu()