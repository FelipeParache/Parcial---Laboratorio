import re
import json
from datetime import datetime
from funciones_listar import personajes_por_atributos
from funciones_listar import listar_atributos
from funciones_listar import listar_personajes_habilidad_json
from funciones_numericas import promediar_ataque_pelea
from funciones_batalla import usuario_elegir_personaje
from funciones_batalla import maquina_elegir_personaje
from funciones_batalla import registrar_batalla

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
            personaje["id"] = line_personaje[0].strip()
            personaje["nombre"] = line_personaje[1].strip()
            personaje["raza"] = line_personaje[2]
            if personaje["raza"] in razas_excluidas:
                personaje["raza"] = line_personaje[2].split()
            else:
                personaje["raza"] = re.split(
                    r"\-", line_personaje[2].strip())
            personaje["poder_de_pelea"] = line_personaje[3].strip()
            personaje["poder_de_ataque"] = line_personaje[4].strip()
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
