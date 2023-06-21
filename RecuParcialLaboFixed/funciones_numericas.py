# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=consider-using-enumerate
# pylint: disable=unidiomatic-typecheck
# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long
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
    poder_ataque = personaje['poder_de_ataque']
    poder_pelea = personaje['poder_de_pelea']
    suma_ataque_pelea = poder_ataque + poder_pelea

    promedio_poder_ataque_pelea = suma_ataque_pelea / 2
    return promedio_poder_ataque_pelea

def determinar_valor_maximo(poder_de_pelea: int, poder_de_ataque: int) -> str:
    '''
    Brief: Determina el valor máximo entre el poder de pelea y 
    el poder de ataque de un personaje.
    Parameters:
        poder_de_pelea -> Entero que representa el poder de pelea del personaje.
        poder_de_ataque -> Entero que representa el poder de ataque del personaje.
    Return:
        valor -> El valor máximo de poder de pelea o ataque con su letra según corresponda.
    '''
    valor = ''
    if poder_de_ataque > poder_de_pelea:
        valor = f'D-{poder_de_ataque}'
    elif poder_de_ataque < poder_de_pelea:
        valor = f'A-{poder_de_pelea}'
    else:
        valor = f'AD-{poder_de_pelea}'
    return valor
