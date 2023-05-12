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
        lista_atributos -> un diccionario donde cada clave es un atributo y
        el valor es una lista de los personajes que pertenecen a esa atributo.
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
    Prameters
        lista -> Una lista de diccionarios que representan personajes.
    Return: Un diccionario con los siguientes valores:
        personajes -> Una lista de diccionarios que representan
        a los personajes que tienen la raza y habilidad ingresadas.
        ingreso_raza -> La raza ingresada por el usuario.
        ingreso_habilidad -> La habilidad ingresada por el usuario.
    '''
    personajes = []
    separador = " + "

    lista_habilidades = personajes_por_atributos(lista, 'habilidades')
    lista_raza = personajes_por_atributos(lista, 'raza')

    ingreso_habilidad = input("Ingrese una habilidad de algun personaje de DBZ: ")
    while ingreso_habilidad not in lista_habilidades:
        ingreso_habilidad = input(
            "ERROR: no se encuentra en la lista. Ingrese una habilidad nuevamente: ")

    ingreso_raza = input("Ingrese la raza de algun personaje de DBZ: ")
    while ingreso_raza not in lista_raza:
        ingreso_raza = input("ERROR: no se encuentra en la lista. Ingrese una raza nuevamente: ")

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
