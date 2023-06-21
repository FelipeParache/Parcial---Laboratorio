# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=consider-using-enumerate
# pylint: disable=unidiomatic-typecheck
# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long
from funciones_numericas import determinar_valor_maximo

def generar_separador(patron: str, largo: int, imprimir = True) -> str:
    '''
    Brief: La función recibe un patrón, un largo y un booleano que indica si 
    se debe imprimir el separador generado. 
    La función retorna un separador generado por la repetición del patrón ingresado
    por la cantidad de veces indicada en el largo.
    Parameters:
        patron -> Patrón que se repite para generar el separador.
        largo -> Cantidad de veces que se repite el patrón.
        imprimir -> Indica si se debe imprimir el separador.
    Return:
        separador -> Retorna el separador generado si el parámetro imprimir es True.
        patron -> Si el parámetro es False, retorna el patron ingresado. 
        N/A -> Si los valores ingresados para el patrón o largo
        no cumplen con las condiciones indicadas.
    '''
    if 1 < len(patron) > 2 or 1 < largo > 235:
        return print("N/A")
    else:
        separador = patron * largo
        if imprimir:
            return separador
        else:
            return patron

def generar_encabezado(titulo: str) -> str:
    '''
    Brief: Genera un encabezado con un título en mayúsculas, separado por un separador.
    Parameters:
        titulo -> Título que se desea colocar en el encabezado.
    Return: Cadena de caracteres que representa el encabezado generado,
    con el título en mayúsculas y separado por un separador.
    '''
    separador = generar_separador("*", 180)
    return print(f"\n{separador}\n{titulo.upper()}\n{separador}\n")

def ususario_ingreso_atributo() -> list:
    '''
    Brief: Solicita al usuario que ingrese un atributo para ordenar
    la lista y el sentido ascendente o descendente.
    Return: Una lista con dos elementos:
        atributo -> El atributo por el cual se ordenará la lista.
        asdendente -> Indica si la lista se debe ordenar en forma ascendente (True) o descendente (False).
    '''
    atributo = input("Ingrese un atributo para ordenar la lista: ").lower()
    while atributo != 'id' and atributo != 'nombre' and atributo != 'raza' and atributo != 'poder_de_pelea' and atributo != 'poder_de_ataque' and atributo != 'habilidades':
        atributo = input("ERROR, no existe ese atributo. "
                         "Ingrese un atributo para ordenar la lista nuevamente: ").lower()

    ascendente = input("Quiere que la lista se ordene de forma ascendente o descendente "
                       "(ingrese ascendente o descendente): ").lower()
    while ascendente != 'ascendente' and ascendente != 'descendente':
        ascendente = input("ERROR. Ingrese nuevamente si quiere que la lista "
                           "se ordene de forma ascendente o descendente: ").lower()

    if ascendente == "ascendente":
        ascendente = True
    else:
        ascendente = False

    return [atributo, ascendente]

def extraer_inicial_personaje(nombre_personaje: str) -> str:
    '''
    Brief: Extrae la inicial del nombre de un personaje.
    Parameters:
        nombre_personaje -> El nombre del personaje
        del cual se extrae la inicial del nombre.
    Return:
        inicial -> La inicial del personaje.
    '''
    if len(nombre_personaje) > 0:
        inicial = nombre_personaje[0]
        return inicial
    return "N/A"

def generar_codigo_personaje(personaje: dict) -> str:
    '''
    Brief: Genera el código para un personaje, con su inicial, un valor máximo y su ID.
    Parameters:
        personaje -> Diccionario que contiene la información del personaje.
    Return:
        codigo_personaje -> El código generado para el personaje.
    '''
    inicial = extraer_inicial_personaje(personaje['nombre']) # K
    valor_max = determinar_valor_maximo(personaje['poder_de_pelea'], personaje['poder_de_ataque']) # AD-9000
    personaje_id = str(personaje['id'])

    separador = '-'

    inicial_valor_max = separador.join([inicial, valor_max]) # K-AD-9000

    ceros_necesarios = 17 - len(inicial_valor_max)
    personaje_id = personaje_id.zfill(ceros_necesarios) # 00000022

    codigo_personaje = separador.join([inicial_valor_max, personaje_id]) # K-AD-9000-00000022

    return codigo_personaje
