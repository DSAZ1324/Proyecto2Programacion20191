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
    >>> obtener_complemento('Z')
    Traceback (most recent call last):
     ...
    ValueError: Z no es una base
    >>> obtener_complemento(1)
    Traceback (most recent call last):
    ...
    ValueError: 1 no es una base

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
    for letra in adn:
        com += obtener_complemento(letra)
    return com


def calcular_correspondencia(adn1, adn2):
    """
    (str, str) -> num

    calcular el porcentaje de la correspondecia del adn

    >>> calcular_correspondencia('ATATTACGGC','TATAATGCCG')
    100.0
    >>> calcular_correspondencia('ATATATCGGC','TATAATGCCG')
    80.0
    >>> calcular_correspondencia('ATATATCGGC','CGATTTACGA')
    20.0

    :param adn1: str con el adn a intrucir
    :param adn2: str con la segunda prueba de adn
    :return: num con el procentaje de la cadena
    """


def corresponden(adn1, adn2):
    return generar_cadena_complementaria(adn1) == adn2


def es_cadena_valida(adn):
    """
    str) -> boolean
  con esta funciopn se quiere validar que las cadena sea valida a la base dada

    >>> es_cadena_valida('ATCG')
    True
    >>> es_cadena_valida('MNHY')
    False

    :param adn: La cadena ingresada a evaluar
    :return: True si la cadena de ADN es valida, False si no se cumple
    """
    if not es_base('T'):
        return
    return False


def es_base(caracter):
    base = ['A', 'a', 'C', 'c', 'G', 'g', 'T', 't']
    if caracter in base:
        return True
    if caracter not in base:
        return False


def es_subcadena(adn1, adn2):
    pass


def reparar_dano(adn, complementaria):
    if corresponden(adn, complementaria):
        return "No presenta errores"
    elif not corresponden(adn, complementaria):
        return generar_cadena_complementaria(adn)


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    com = []
    for cadena in lista_adn:
        com.append(generar_cadena_complementaria(cadena))
    return com


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adnn):
    com = ''
    for cadena in lista_adnn:
        com += generar_cadena_complementaria(cadena)
    return com
