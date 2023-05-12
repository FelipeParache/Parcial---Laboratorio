from funciones_string import generar_separador
from funciones_string import generar_encabezado
from funciones_numericas import sanitizar_entero
from funciones_principales import obtener_datos
from funciones_principales import listar_cantidad_por_raza
from funciones_principales import listar_personajes_por_raza
from funciones_principales import listar_personajes_por_habilidad
from funciones_principales import jugar_batalla
from funciones_principales import guardar_json
from funciones_principales import leer_json

def imprimir_menu(path: str) -> None:
    '''
    Brief: Muestra en consola un menú con distintas opciones.
    Parameters: 
        path -> Ruta del archivo que se usa en la opción 1 del menú.
    '''
    print("\nMENU DRAGON BALL Z:\n"
          f"# 1 - Traer datos desde el archivo: {path}\n"
          "# 2 - Listar cantidad por raza\n"
          "# 3 - Listar personajes por raza\n"
          "# 4 - Listar personajes por habilidad\n"
          "# 5 - Jugar batalla\n"
          "# 6 - Guardar JSON con personajes por raza y habilidad\n"
          "# 7 - Mostrar los personajes guardados en el JSON\n"
          "# 8 - Salir del programa\n"
          f"{generar_separador('-', 60)}")

def dbz_menu_principal(path: str) -> int:
    '''
    Brief: Muestra un menú de opciones y permite elegir una opción
    ingresando un número de la lista.
    Luego, devuelve la opción elegida como un entero.
    Parameters:
        path -> Ruta del archivo que se usa en la opción 1 del menú.
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
    Brief: Recibe una lista y segun la respuesta del usuario, muestra una parte del programa
    Parameters:
        lista_heroes -> lista sobre la cual voy a hacer la busqueda
    Return: None
    '''
    path_json = ""
    respuesta = dbz_menu_principal(path_json)

    while respuesta != 8:

        match(respuesta):
            case 1:
                generar_encabezado("1: Datos obtenidos con éxito")
                datos_obtenidos = obtener_datos(path)
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
                break
            case _:
                generar_encabezado("ERROR. No existe ese dato")

        respuesta = dbz_menu_principal(path_json)
