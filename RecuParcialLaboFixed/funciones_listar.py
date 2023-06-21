# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=consider-using-enumerate
# pylint: disable=unidiomatic-typecheck
# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long
def personajes_por_atributos(lista: list, valor: str) -> list:
    '''
    Brief: Toma como entrada una lista de personajes y devuelve un diccionario
    con la cantidad de personajes que hay por cada atributo.
    Parameters:
        lista -> Una lista de diccionarios, donde cada diccionario
        representa un personaje con sus características.
        valor -> Un string que representa la característica
        por la cual se van a listar los personajes.
    Return:
        lista_atributos_personaje -> un diccionario donde cada clave es un atributo y
        el valor es una lista de los personajes que pertenecen a ese atributo.
    '''
    if type(lista) is list and len(lista) > 0:
        lista_atributos_personaje = {}
        for personaje in lista:
            atributos = personaje[valor]
            if type(atributos) == list:
                for elemento in atributos:
                    if elemento not in lista_atributos_personaje:
                        lista_atributos_personaje[elemento] = []
                    lista_atributos_personaje[elemento].append(personaje)
            else:
                if atributos not in lista_atributos_personaje:
                    lista_atributos_personaje[atributos] = []
                lista_atributos_personaje[atributos].append(personaje)

        return lista_atributos_personaje
    return []

def listar_atributos(lista: list, valor: str) -> list:
    '''
    Brief: Recibe como parametros una lista y un string que representa
    el nombre del atributo a listar.
    Retorna una lista con los valores del atributo.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
        valor -> String que representa el atributo a listar.
    Return: 
        lista_atributos -> Lista que contiene los valores del atributo correspondiente.
    '''
    if type(lista) is list and len(lista) > 0:
        lista_atributos = []
        for personaje in lista:
            atributo = personaje[valor]
            if type(atributo) == list:
                for item in atributo:
                    lista_atributos.append(item)
            else:
                lista_atributos.append(atributo)
        return lista_atributos
    return []

def listar_personajes_habilidad_json(lista: list) -> dict:
    '''
    Brief: Recibe una lista de personajes y solicita al usuario
    el ingreso de una habilidad y una raza. Luego retorna un diccionario
    con una lista de los personajes que tienen la habilidad y raza ingresadas
    con su poder de ataque y habilidades, sin incluir la habilidad ingresada.
    Prameters:
        lista -> Una lista de diccionarios que representan personajes.
    Return: Un diccionario con los siguientes valores:
        personajes -> Una lista de diccionarios que representan
        a los personajes que tienen la raza y habilidad ingresadas.
        ingreso_raza -> La raza ingresada por el usuario.
        ingreso_habilidad -> La habilidad ingresada por el usuario.
    '''
    if lista is None or len(lista) <= 0:
        print("ERROR. Lista vacía o inexistente")

    personajes = []
    separador = " + "

    lista_habilidades = listar_atributos(lista, 'habilidades')
    lista_raza = listar_atributos(lista, 'raza')

    ingreso_habilidad = input("Ingrese una habilidad de algun personaje de DBZ: ").capitalize()
    while ingreso_habilidad not in lista_habilidades:
        ingreso_habilidad = input(
            "ERROR: no se encuentra en la lista. Ingrese una habilidad nuevamente: ").capitalize()

    ingreso_raza = input("Ingrese la raza de algun personaje de DBZ: ").capitalize()
    while ingreso_raza not in lista_raza:
        ingreso_raza = input("ERROR: no se encuentra en la lista."
                             "Ingrese una raza nuevamente: ").capitalize()

    for personaje in lista:
        if ingreso_habilidad in personaje['habilidades'] and ingreso_raza in personaje['raza']:

            nombre = personaje['nombre']
            poder_de_ataque = personaje['poder_de_ataque']
            habilidades = personaje['habilidades']
            habilidades.remove(ingreso_habilidad)
            habilidades_join = separador.join(habilidades)

            personajes.append({'nombre': nombre,
                               'poder_de_ataque': poder_de_ataque, 
                               'habilidades': habilidades_join})

    return {'personajes': personajes,
            'ingreso_raza': ingreso_raza, 
            'ingreso_habilidad': ingreso_habilidad}

def listar_saiyans(lista: list) -> list:
    '''
    Brief: Retorna una lista de todos los personajes de la raza Saiyan.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
    Return: Una lista de diccionarios, donde cada diccionario
    representa un personaje de la raza Saiyan.
    '''
    if type(lista) is list and len(lista) > 0:
        lista_saiyan = []
        for personaje in lista:
            for raza in personaje['raza']:
                if raza == 'Saiyan':
                    lista_saiyan.append(personaje)
        return lista_saiyan
    return []

def aumento_de_poder_saiyans(lista: list) -> list:
    '''
    Brief: Toma una lista de personajes y devuelve
    una lista con los aumentos de poder de pelea y ataque de los personajes con raza Saiyan.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
    Return: Una lista de dos listas que representan los aumentos
    de poder de pelea y ataque de los personajes Saiyan.
    '''
    if type(lista) is list and len(lista) > 0:
        lista_saiyan = listar_saiyans(lista)
        aumentos_poder_pelea = []
        aumentos_poder_ataque = []
        for personaje in lista_saiyan:
            aumento_poder_pelea = personaje['poder_de_pelea'] * 1.5
            aumento_poder_ataque = personaje['poder_de_ataque'] * 1.7
            aumentos_poder_pelea.append(str(aumento_poder_pelea))
            aumentos_poder_ataque.append(str(aumento_poder_ataque))

        return[aumentos_poder_pelea, aumentos_poder_ataque]
    return []

def transformacion_dios_saiyan(lista: list) -> list:
    '''
    Brief: Agrega la habilidad "Transformación nivel dios"
    a la lista de habilidades de todos los personajes de raza Saiyan.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
    Return: Una lista que contiene las habilidades actualizadas de los Saiyans en listas.
    '''
    if type(lista) is list and len(lista) > 0:
        lista_saiyan = listar_saiyans(lista)
        habilidades_actualizadas = []
        for personaje in lista_saiyan:
            habilidades = personaje['habilidades']
            habilidades.append("Transformación nivel dios")
            habilidades_actualizadas.append(habilidades)
        return habilidades_actualizadas
    return []

def actualizar_habilidades_poderes_saiyan(lista: list) -> list:
    '''
    Brief: Actualiza los poderes y habilidades de los personajes de la lista_saiyan,
    incrementando su poder de pelea y poder de ataque en un 50% y 70% y
    añadiendo la habilidad "Transformación nivel dios" a su lista de habilidades.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
    Return: Una lista con los personajes de raza Saiyan actualizados.
    '''
    if type(lista) and len(lista) > 0:
        lista_saiyans_actualizados = []
        lista_pelea = []
        lista_ataque = []
        lista_saiyan = listar_saiyans(lista)
        lista_poderes_actualizados = aumento_de_poder_saiyans(lista)
        lista_habilidades_actualizadas = transformacion_dios_saiyan(lista)

        for pelea in lista_poderes_actualizados[0]:
            lista_pelea.append(pelea)

        for ataque in lista_poderes_actualizados[1]:
            lista_ataque.append(ataque)

        for i in range(len(lista_saiyan)):
            personaje = lista_saiyan[i]
            personaje['poder_de_pelea'] = lista_pelea[i]
            personaje['poder_de_ataque'] = lista_ataque[i]
            personaje['habilidades'] = lista_habilidades_actualizadas[i]
            lista_saiyans_actualizados.append(personaje)

        return lista_saiyans_actualizados
    return []

def ordenamiento_personajes(lista: list, atributo: str) -> None:
    '''
    Brief: Ordena la lista de personajes en base a un atributo específico.
    Parameters:
        lista -> Una lista de diccionarios que representan personajes.
        atributo -> El atributo por el cual se ordenará la lista.
    '''
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i][atributo] > lista[j][atributo]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
