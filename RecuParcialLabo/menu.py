from os import system
from funciones_string import *
from funciones_numericas import sanitizar_entero
from funciones_principales import *

def imprimir_menu(path: str) -> None:
    '''
    Brief: Muestra en consola un menú con distintas opciones.
    Parameters: 
        path -> Ruta del archivo CSV que contiene los datos de los personajes.
    '''
    print("\nMENU DRAGON BALL Z:\n"
          f"# DATOS YA OBTENIDOS {path}\n"
          "# 2 - Listar cantidad por raza\n"
          "# 3 - Listar personajes por raza\n"
          "# 4 - Listar personajes por habilidad\n"
          "# 5 - Jugar batalla\n"
          "# 6 - Guardar JSON con personajes por raza y habilidad\n"
          "# 7 - Mostrar los personajes guardados en el JSON\n"
          "# 8 - Mostrar aumento de poder Saiyan\n"
          "# 9 - Ordenar de menor a mayor o viceversa los personajes por atributo\n"
          "# 10 - Generar y mostrar el codigo de cada uno de los personajes\n"
          "# 11 - Salir del programa\n"
          f"{generar_separador('-', 75)}")

def dbz_menu_principal(path: str) -> int:
    '''
    Brief: Muestra un menú de opciones y permite elegir una opción
    ingresando un número de la lista.
    Luego, devuelve la opción elegida como un entero.
    Parameters:
        path -> Ruta del archivo CSV que contiene los datos de los personajes.
    Return:
        int -> Un entero que representa la opción elegida por el usuario en el menú.
        -1 -> Si el usuario ingresó un valor no numérico. 
    '''
    imprimir_menu(path)

    respuesta = input(
        "Ingrese un numero de la lista para ver los resultados: ")

    if respuesta.isdigit():
        respuesta = sanitizar_entero(respuesta)
        return respuesta
    else:
        return -1

def dbz_app(path: str) -> None:
    '''
    Brief: Programa de base de datos de personajes de Dragon Ball Z.
    Permite cargar los datos desde un archivo CSV,
    realizar consultas y acciones como guardar los datos en un archivo JSON o generar un CSV.
    Parameters:
        path -> Ruta del archivo CSV que contiene los datos de los personajes.
    '''
    path_json = ""
    respuesta = ""

    while respuesta != 1:
        respuesta = sanitizar_entero(input("Ingrese el número 1 para cargar los datos: "))

    generar_encabezado("1: Datos obtenidos con éxito")
    datos_obtenidos = obtener_datos(path)

    while respuesta != 11:
        respuesta = dbz_menu_principal(path_json)
        system('clear')
        match(respuesta):
            case 2:
                generar_encabezado("2: Listar cantidad por raza")
                listar_cantidad_por_raza(datos_obtenidos)
            case 3:
                generar_encabezado("3: Listar personajes por raza")
                listar_personajes_por_raza(datos_obtenidos)
            case 4:
                generar_encabezado("4: Listar personajes por habilidad")
                listar_personajes_por_habilidad(datos_obtenidos)
            case 5:
                generar_encabezado("5: Jugar batalla")
                jugar_batalla(datos_obtenidos)
            case 6:
                generar_encabezado("6: Guardar JSON con personajes por raza y habilidad")
                path_json = guardar_json(datos_obtenidos)
            case 7:
                generar_encabezado("7: Mostrar los personajes guardados en el JSON")
                leer_json(path_json)
            case 8:
                generar_encabezado("8: Generar CSV con los Saiyans actualizados")
                guardar_csv_saiyans(datos_obtenidos)
            case 9:
                prompt_usuario = ususario_ingreso_atributo()
                generar_encabezado(f"9: Lista de personajes ordenada por {prompt_usuario[0]}")
                ordenar_personajes_por_atributo(datos_obtenidos, prompt_usuario[0], prompt_usuario[1])
            case 10:
                generar_encabezado("10: Lista de personajes actualizada con los codigos")
                agregar_codigos_personajes(datos_obtenidos)
            case _:
                if respuesta == 11:
                    pass
                elif respuesta == 1:
                    generar_encabezado("1: Datos ya obtenidos")
                else:
                    generar_encabezado("ERROR. No existe ese dato")
