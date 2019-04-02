def obtener_complemento(base):
    """
    str -> str

    'Recibe una letra y retorna su complemento'
    >>> obtener_complemento('A')
    'T'
    >>> obtener_complemento('G')
    'C'
    >>> obtener_complemento('T')
    'A'
    >>> obtener_complemento('C')
    'G'

    :param base: str introducir base de la cadena
    :return: El complemento de la candena del ADN
    """

    if es_base(base):
        if base == 'A':
            return 'T'
        if base == 'a':
            return 't'
        elif base == 'T':
            return 'A'
        elif base == 't':
            return 'a'
        elif base == 'G':
            return 'C'
        elif base == 'g':
            return 'c'
        elif base == 'C':
            return 'G'
        elif base == 'c':
            return 'g'
    if not es_base(base):
        raise ValueError(str(base) + ' no es una base')


def generar_cadena_complementaria(adn):
    com = ''
    if int == type(adn):
        raise TypeError('No puede tener numeros')
    if float == type(adn):
        raise TypeError('No puede tener numeros')
    for letra in adn:
        com += obtener_complemento(letra)
    return com


def calcular_correspondencia(adn1, adn2):
    """
    (str, str) -> float

    calcular el porcentaje de la correspondecia del adn

    >>> calcular_correspondencia('agtc','tcag')
    100.0
    >>> calcular_correspondencia('CGTA','GCGC')
    50.0
    >>> calcular_correspondencia('ATAT','CGAT')
    0.0

    :param adn1: str con el adn a intrucir
    :param adn2: str con la segunda prueba de adn
    :return: num con el procentaje de la cadena
    """
    ubicacion = 0
    porciento_adn = 0

    if not es_cadena_valida(adn2):
        raise ValueError(adn2 + ' no es una base')
    if not es_cadena_valida(adn1):
        raise ValueError(adn1 + ' no es una base')
    if len(adn1) == len(adn2):
        for i in adn1:
            if corresponden(i, adn2[ubicacion]):
                porciento_adn += 1
                ubicacion += 1
        return porciento_adn * 100 / len(adn1)


def corresponden(adn1, adn2):
    if not es_cadena_valida(adn2):
        raise ValueError(adn2 + ' no es una base')
    return generar_cadena_complementaria(adn1) == adn2


def es_cadena_valida(adn):
    """
    (str) -> boolean
  con esta funcion se quiere validar que las cadena sea valida a la base dada

    >>> es_cadena_valida('ATCG')
    True
    >>> es_cadena_valida('MNBP')
    False

    :param adn: La cadena ingresada a evaluar
    :return: True si la cadena de ADN es valida, False si no se cumple
    """
    if int == type(adn):
        raise TypeError(str(adn) + ' no es una base')
    if float == type(adn):
        raise TypeError(str(adn) + ' no es una base')
    for letra in adn:
        base = es_base(letra)
        if base == True:
            return True
        if base != True:
            return False

          
def es_base(caracter):
    if int == type(caracter):
        raise TypeError(str(caracter) + ' no es una base')
    if float == type(caracter):
        raise TypeError(str(caracter) + ' no es una base')
    if len(caracter) != 1:
        raise ValueError(caracter + ' tiene mas de 1 caracter')
    base = ['A', 'a', 'C', 'c', 'G', 'g', 'T', 't']
    if caracter in base:
        return True
    if caracter not in base:
        return False


def es_subcadena(adn1, adn2):
    """
    (str, str) -> boolean
    funcion que nos permite definir la subcadena de una secuencia dada

    >>> es_subcadena('atcgta', 'gta')
    True
    >>> es_subcadena('atcg', 'tta')
    False

    :param adn1: str con la cadena 1
    :param adn2: str con la cadena 2
    :return: si la secuencia de la cadena 2 es subcadena de l secuencia de la cadena 1
    """
    if int == type(adn2):
        raise TypeError(str(adn2) + ' no es pueden enteros')
    if int == type(adn1):
        raise TypeError(str(adn1) + ' no se pueden enteros')
    if float == type(adn1):
        raise TypeError(str(adn1) + ' no se pueden enteros')
    if adn2 in adn1:
        return True
    elif adn2 not in adn1:
        return False


def reparar_dano(adn, complementaria):
    if int == type(complementaria):
        raise TypeError('No puede tener numeros')
    if not es_cadena_valida(complementaria):
        raise ValueError(complementaria + ' no es una cadena valida')
    if corresponden(adn, complementaria):
        return "No presenta errores"
    elif not corresponden(adn, complementaria):
        return generar_cadena_complementaria(adn)


def obtener_secciones(adn, n):
    """
    (str, int) -> list of str
    validar las secciones de una cadena de adn

    >>> obtener_secciones('atata', 2)
    ['at', 'ata']

    >>> obtener_secciones('ATGCTACAG', 3)
    ['ATG', 'CTA', 'CAG']

    :param adn: str con la cadena de adn
    :param n: int con el numero de secciones que se quiere dividir
    :return: str con el resultado de las secciones
    """
    if not es_cadena_valida(adn):
        raise ValueError(adn + ' no se pueden enteros')
    if str == type(n):
        raise ValueError('No puede tener letras')
    if float == type(n):
        raise TypeError('No puede tener enteros')
    suma_cadenas = len(adn) // n
    division_seccion = []
    for group in range(n):
        resultado_cadena = ""
        cantidad_cadena = suma_cadenas
        if group == n - 1 and len(adn) % n != 0:
            cantidad_cadena = suma_cadenas + len(adn) % n
        for caracter in range(cantidad_cadena):
            base_cadena = group * suma_cadenas + caracter
            resultado_cadena = resultado_cadena + adn[base_cadena]
        division_seccion.append(resultado_cadena)
    return division_seccion


def obtener_complementos(lista_adn):
    com = []
    for cadena in lista_adn:
        com.append(generar_cadena_complementaria(cadena))
    return com


def unir_cadena(lista_adn):
    """
    (list of str) -> str
    funcion que permita concatenar una lista dada

    >>> unir_cadena(['ATCGTA', 'TAGCAT'])
    'ATCGTATAGCAT'
    >>> unir_cadena(['gcat', 'cgta'])
    'gcatcgta'


    :param lista_adn: list of str que representa la cadenas de adn en una lista
    :return:str con la union de las dos cadenas
    """
    com = ''
    for cadena in lista_adn:
        com = (generar_cadena_complementaria(cadena))
        for caracter in cadena:
            com = com + caracter
    return com


def complementar_cadenas(lista_adn):
    com = ''
    for cadena in lista_adn:
        com += generar_cadena_complementaria(cadena)
    return com