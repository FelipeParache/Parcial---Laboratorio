import random

def usuario_elegir_personaje(lista_nombres: list, lista_poder: list) -> list:
    '''
    Brief: Recibe dos listas, una con los nombres de los personajes y
    otra con los poderes de ataque.
    Pide al usuario que ingrese el nombre del personaje y
    verifica que esté en la lista de personajes.
    Devuelve una lista con el nombre y el poder de ataque del personaje elegido.
    Parameters:
        lista_nombres -> Lista con los nombres de los personajes.
        lista_poder -> lista de con los poderes de ataque correspondientes a cada personaje.
    Return:
        list -> Lista con el nombre del personaje elegido y su poder de ataque.
    '''
    if len(lista_nombres) > 0 and len(lista_poder) > 0:
        personaje_elegido = input("Ingrese su personaje: ").capitalize()
        while personaje_elegido not in lista_nombres:
            personaje_elegido = input(
                "ERROR: El personaje ingresado no se encuentra en la lista de personajes."
                " Ingrese su personaje nuevamente: ").capitalize()

        index_elegido = lista_nombres.index(personaje_elegido)
        poder_elegido = lista_poder[index_elegido]
        print(f"\n* Elegiste a {personaje_elegido} con un poder de ataque de {poder_elegido}.\n")
        return [personaje_elegido, poder_elegido]
    return []

def maquina_elegir_personaje(lista_nombres: list, lista_poder: list) -> list:
    '''
    Brief: Recibe dos listas, una con los nombres de los personajes y
    otra con los poderes de ataque.
    Elige aleatoriamente un nombre dentro de la lista.
    Devuelve una lista con el nombre y el poder de ataque del personaje elegido.
    Parameters:
        lista_nombres -> Lista con los nombres de los personajes.
        lista_poder -> lista de con los poderes de ataque correspondientes a cada personaje.
    Return:
        list -> Lista con el nombre del personaje elegido y su poder de ataque.
    '''
    if len(lista_nombres) > 0 and len(lista_poder) > 0:
        personaje_maquina = random.choice(lista_nombres)
        index_maquina = lista_nombres.index(personaje_maquina)
        maquina_poder = lista_poder[index_maquina]
        print(f"* La máquina eligió a {personaje_maquina} con un poder de ataque de {maquina_poder}.\n")
        return [personaje_maquina, maquina_poder]
    return []

def registrar_batalla(registrar: str) -> None:
    '''
    Brief: Toma un registro de batalla en formato de cadena y lo agrega a un archivo de texto.
    Parameters:
        registrar -> Una cadena que contiene el registro
        de la batalla que se quiere agregar al archivo.
    '''
    with open("registro_batallas.txt", "a", encoding = "utf-8") as texto:
        texto.write(registrar)
