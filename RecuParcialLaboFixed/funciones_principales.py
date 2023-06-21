# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=consider-using-enumerate
# pylint: disable=unidiomatic-typecheck
# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long
import re
import json
from datetime import datetime
from funciones_listar import *
from funciones_numericas import *
from funciones_batalla import *
from funciones_string import generar_codigo_personaje

def obtener_datos(path: str) -> list:
    '''
    Brief: Recibe una ruta de un archivo en formato CSV, la lee y
    procesa para devolver una lista de diccionarios con la información de cada personaje.
    Parameters:
        path -> Ruta del archivo CSV que contiene la información de los personajes.
    Return:
        lista_personajes -> Una lista de diccionarios,
        donde cada diccionario representa la información de un personaje. 
    '''
    with open(path, "r", encoding="utf-8") as archivo:
        lista_personajes = []
        razas_excluidas = ["Shin-jin", "Three-Eyed-People"]

        for line in archivo:
            line_personaje = re.split(",|\n", line)
            personaje = {}
            personaje["id"] = sanitizar_entero(line_personaje[0].strip())
            personaje["nombre"] = line_personaje[1].strip()
            personaje["raza"] = line_personaje[2]
            if personaje["raza"] in razas_excluidas:
                personaje["raza"] = line_personaje[2].split()
            else:
                personaje["raza"] = re.split(
                    r"\-", line_personaje[2].strip())
            personaje["poder_de_pelea"] = sanitizar_entero(line_personaje[3].strip())
            personaje["poder_de_ataque"] = sanitizar_entero(line_personaje[4].strip())
            personaje["habilidades"] = re.split(
                r"\s\|\$\%|\|\$\%", line_personaje[5].strip())
            lista_personajes.append(personaje)
        return lista_personajes

def listar_cantidad_por_raza(lista: list) -> str:
    '''
    Brief: Recibe una lista de personajes y devuelve una cadena de caracteres que
    indica la cantidad de personajes que hay por cada raza en la lista.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
    Return:
        acumulador_razas -> Una cadena de caracteres que indica
        la cantidad de personajes que hay por cada raza en la lista.
    '''
    if lista is None or len(lista) <= 0:
        print("ERROR. Lista vacía o inexistente")
    raza_personajes = personajes_por_atributos(lista, 'raza')
    acumulador_texto_razas = ""

    for raza in raza_personajes:
        cantidad = len(raza_personajes[raza])
        acumulador_texto_razas += f"\nHay {cantidad} personajes de raza {raza}\n"
    return print(acumulador_texto_razas)

def listar_personajes_por_raza(lista: list) -> str:
    '''
    Brief: Recibe una lista de diccionarios que representan personajes y
    devuelve una cadena de caracteres con información sobre
    el poder de ataque de cada personaje por raza.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
    Return:
        acumulador_texto_razas -> Una cadena de caracteres que representa
        información sobre el nombre y poder de ataque de cada personaje por raza.
    '''
    if lista is None or len(lista) <= 0:
        print("ERROR. Lista vacía o inexistente")
    raza_personajes = personajes_por_atributos(lista, 'raza')
    acumulador_texto_razas = ""
    acumulador_texto_nombre_ataque = ""

    for raza in raza_personajes:
        acumulador_texto_razas += f"\n{raza.upper()}:\n"
        for personaje in raza_personajes[raza]:
            acumulador_texto_nombre_ataque += f"* {personaje['nombre']} | Poder de ataque {personaje['poder_de_ataque']}\n"
        acumulador_texto_razas += acumulador_texto_nombre_ataque
        acumulador_texto_nombre_ataque = ""

    return print(acumulador_texto_razas)

def listar_personajes_por_habilidad(lista: list) -> str:
    '''
    Brief: Recibe una lista de diccionarios, 
    solicita al usuario que ingrese una habilidad de un personaje y
    devuelve una cadena de texto con los nombres de los personajes que poseen la habilidad ingresada 
    junto con el promedio de su poder de ataque y pelea.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
    Return:
        acumulador_texto_habilidad -> Una cadena de texto con los nombres de los personajes
        que poseen la habilidad ingresada junto con el promedio de su poder de ataque y pelea.
    '''
    if lista is None or len(lista) <= 0:
        print("ERROR. Lista vacía o inexistente")

    lista_habilidades = listar_atributos(lista, 'habilidades')
    acumulador_texto_habilidad = ""

    habilidad_ingresada = input("Ingrese una habilidad de un personaje DBZ: ")
    while habilidad_ingresada not in lista_habilidades:
        habilidad_ingresada = input(
            "ERROR. Ingrese una habilidad de un personaje DBZ nuevamente: ")

    print(f"\n{habilidad_ingresada.upper()}")

    for personaje in lista:
        if habilidad_ingresada in personaje['habilidades']:
            promedio_ataque_pelea = promediar_ataque_pelea(personaje)
            acumulador_texto_habilidad += f"* {personaje['nombre']} | Promedio poder de ataque y pelea {promedio_ataque_pelea}\n"
    return print(acumulador_texto_habilidad)

def jugar_batalla(lista: list) -> str:
    '''
    Brief: Simula una batalla entre el usuario y la máquina, 
    donde se eligen personajes al azar de una lista de personajes, 
    y se determina quién gana según el poder de ataque de cada personaje.
    Luego, registra el resultado de la batalla en un archivo de texto.
    Prameters
        lista -> Una lista de diccionarios que representan personajes.
    Return:
        resultado -> Una cadena que indica el resultado de la batalla y la fecha en la que ocurrió.
    '''
    if lista is None or len(lista) <= 0:
        print("ERROR. Lista vacía o inexistente")

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    lista_poder_ataque = listar_atributos(lista, 'poder_de_ataque')
    lista_nombres = listar_atributos(lista, 'nombre')

    print("PREPÁRESE PARA LA BATALLA!\n")
    personaje_elegido = usuario_elegir_personaje(lista_nombres, lista_poder_ataque)
    personaje_maquina = maquina_elegir_personaje(lista_nombres, lista_poder_ataque)
    nombre_elegido = personaje_elegido[0]
    nombre_maquina = personaje_maquina[0]
    poder_elegido = personaje_elegido[1]
    maquina_poder = personaje_maquina[1]

    if poder_elegido > maquina_poder:
        print(f"Felicitaciones! Ganaste la batalla con {nombre_elegido}.\n")
        resultado = f"Batalla del: {fecha}\n* Ganó el usuario con: {nombre_elegido}\n* Perdió la máquina con: {nombre_maquina}\n\n"
    elif poder_elegido < maquina_poder:
        print(f"Que lástima! Perdiste la batalla. La máquina ha ganado con {nombre_maquina}.\n")
        resultado = f"Batalla del: {fecha}\n* Ganó la máquina con: {nombre_maquina}\n* Perdió el usuario con: {nombre_elegido}\n\n"
    else:
        print("La batalla terminó en empate.\n")
        resultado = f"Batalla del: {fecha}\n* Hubo empate entre el usuario {nombre_elegido} y la máquina {nombre_maquina}\n\n"

    return registrar_batalla(resultado)

def guardar_json(lista: list) -> str:
    '''
    Brief: Recibe una lista de personajes y guarda en un archivo json
    los personajes que tienen la habilidad y raza ingresadas por el usuario,
    exceptuando la habilidad ingresada.
    Prameters
        lista -> Una lista de diccionarios que representan personajes.
    Return:
        nombre_json -> Un string que contiene el nombre del archivo json generado.
    '''
    if lista is None or len(lista) <= 0:
        print("ERROR. Lista vacía o inexistente")

    diccionario_json = listar_personajes_habilidad_json(lista)

    habilidad = re.sub(" ", "_", diccionario_json['ingreso_habilidad'])
    raza = diccionario_json['ingreso_raza']

    nombre_json = f'{raza}_{habilidad}.json'

    with open(nombre_json, "w", encoding = "utf-8") as archivo_json:
        json.dump(diccionario_json['personajes'], archivo_json, ensure_ascii = False, indent = 4)

        return nombre_json

def leer_json(path: str) -> None:
    '''
    Brief: Lee y muestra los datos de un archivo JSON que contiene
    información de los personajes.
    La ruta del archivo se obtiene a través de la función guardar_json.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
    '''
    with open(path, "r", encoding = "utf-8") as archivo_json:
        data_json = json.load(archivo_json)

    for personaje in data_json:
        nombre = personaje['nombre']
        poder_de_ataque = personaje['poder_de_ataque']
        habilidades = personaje['habilidades']

        print(f"\n* {nombre} - {poder_de_ataque} - {habilidades}")

def guardar_csv_saiyans(lista: list) -> None:
    '''
    Brief: Guarda los datos actualizados de los personajes de raza Saiyan en un archivo CSV.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
    '''
    lista_saiyans_actualizados = actualizar_habilidades_poderes_saiyan(lista)
    separador_razas = '-'
    separador_habilidades = ' | '

    if type(lista_saiyans_actualizados) is list and len(lista_saiyans_actualizados) > 0:

        with open("saiyans_actualizados.csv", "a", encoding = "utf-8") as archivo_csv:

            for personaje in lista_saiyans_actualizados:
                linea = (f"{personaje['id']},{personaje['nombre']},"
                         f"{separador_razas.join(personaje['raza'])},"
                         f"{personaje['poder_de_pelea']},{personaje['poder_de_ataque']},"
                         f"{separador_habilidades.join(personaje['habilidades'])}")

                archivo_csv.writelines(f"{linea}\n")

def ordenar_personajes_por_atributo(lista: list, atributo: str, ascendente: bool) -> None:
    '''
    Brief: Ordena la lista de personajes por un atributo específico y muestra los personajes en orden ascendente o descendente.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
        atributo -> El atributo por el cual se ordenará la lista.
        ascendente -> Indica si la lista se debe ordenar en forma ascendente (True) o descendente (False).
    '''
    if type(lista) is list and len(lista) > 0:
        ordenamiento_personajes(lista, atributo)

        if not ascendente:
            lista.reverse()

        for personaje in lista:
            print(f"\nID: {personaje['id']} - "
                f"NOMBRE: {personaje['nombre']} - "
                f"RAZA: {personaje['raza']} - "
                f"PELEA: {personaje['poder_de_pelea']} - "
                f"ATAQUE: {personaje['poder_de_ataque']} - "
                f"HABILIDAD: {personaje['habilidades']}")

def agregar_codigos_personajes(lista: list) -> None:
    '''
    Brief: Agrega los códigos generados a los personajes de la lista
    como una nueva clave en el diccionario.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
    '''
    if type(lista) is list and len(lista) > 0:
        for personaje in lista:
            codigo_personaje = generar_codigo_personaje(personaje)
            personaje['codigo'] = codigo_personaje
            print(f"{personaje}\n")
