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
