import re

def sanitizar_entero(numero_str: str) -> int:
    '''
    Brief: Recibe un string como parámetro, lo verifica para saber
    si es un número positivo o negativo y lo transforma en un entero.
    Parameters:
        numero_str -> String a verificar para saber si es un número positivo o negativo.
    Return: 
        int -> Si numero_str es un número positivo.
        -1 -> Si numero_str no es un número válido.
        -2 -> Si numero_str es un número negativo.
        -3 -> Si numero_str no es un string. 
    '''
    if type(numero_str) == str:
        numero_str = numero_str.strip()

        if len(numero_str) and re.search(r"^-{0,1}[0-9]*$", numero_str) is not None:

            if numero_str[0] == "-":
                return -2

            return int(numero_str)

        return -1

    return -3

def promediar_ataque_pelea(personaje: dict) -> float:
    '''
    Brief: Calcula el promedio entre dos atributos de un personaje.
    Parameters:
        personaje -> Un diccionario que contiene las claves 'poder_de_ataque' y 'poder_de_pelea'.
    Return:
        promedio_poder_ataque_pelea -> Un número que representa el promedio entre
        'poder_de_ataque' y 'poder_de_pelea' del personaje.
    '''
    suma_ataque_pelea = 0
    poder_ataque = sanitizar_entero(personaje['poder_de_ataque'])
    poder_pelea = sanitizar_entero(personaje['poder_de_pelea'])
    suma_ataque_pelea = poder_ataque + poder_pelea

    promedio_poder_ataque_pelea = suma_ataque_pelea / 2
    return promedio_poder_ataque_pelea