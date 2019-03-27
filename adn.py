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
    ValueError: Z No es una base
    >>> obtener_complemento(1)
    Traceback (most recent call last):
    ...
    ValueError: 1 no es una base

    :param base: str introducir base de la cadena
    :return: El complemento de la candena del ADN
    """
    if int == type(base):
        raise ValueError(str(base) + " no es una base")
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
    else:
        raise ValueError(base + " No es una base")





def generar_cadena_complementaria(adn):
    """
    str -> str

    Transforma una cadena de ADN a su cadena complementaria

    >>> generar_cadena_complementaria('agtc')
    'tcag'

    >>> generar_cadena_complementaria('AAA')
    'TTT'

    #>>> generar_cadena_complementaria('1')
    Traceback (most recent call last):
    ..
    TypeError: La cadena no puede tener numeros

    #>>> generar_cadena_complementaria('z')
    Traceback (most recent call last):
    ..
    TypeError: Revise la cadena de ADN

    :param adn: str que representa una cadena de ADN
    :return: str que representa la cadena complementaria de ADN
    """
    complementario = {'a': 't', 'A': 'T', 't': 'a', 'T': 'A', 'c': 'g', 'C': 'G', 'g': 'c', 'G': 'C'}
    com = ''
    for letra in adn:
        com += complementario[letra]
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
    """
    (str, str) -> bool

    Valida si dos cadenas de ADN corresponden entre su base y complementaria

    >>> corresponden('AAAA', 'TTTT')
    True

    >>> corresponden('atg', 'ttt')
    False

    #>>> corresponden('1', 't')
    Traceback (most recent call last):
    ..
    TypeError: La cadena no puede estar compuesta por numeros

    #>>> corresponden('z', 'a')
    Traceback (most recent call last):
    ..
    TypeError: Las Cadenas de ADN no son validas

    :param adn1: str que representa la cadena b
    ase de ADN
    :param adn2: str que representa la cadena complementaria de ADN
    :return: bool que representa si la cadena complementaria corresponde a la de base
    """
    return generar_cadena_complementaria(adn1) == adn2


def es_cadena_valida(adn):
    pass


def es_base(caracter):
    """
    (str of len == 1) -> (str of len == 1)

    Valida un caracter y retorna la base correspondiente

    >>> es_base('t')
    'a'

    >>> es_base('C')
    'G'

    ·>>> es_base('u')
    Traceback (most recent call last):
    ..
    TypeError: El caracter no pertenece a el codigo del ADN

    #>>> es_base('1')
    Traceback (most recent call last):
    ..
    TypeError: no se pueden ingresar numeros

    :param caracter: str que representa el caracter complementario
    :return: str que representa el caracter base
    """
    complementario = {'a': 't', 'A': 'T', 't': 'a', 'T': 'A', 'c': 'g', 'C': 'G', 'g': 'c', 'G': 'C'}
    return complementario[caracter]


def es_subcadena(adn1, adn2):
    pass


def reparar_dano(adn, complementaria):
    """
    str -> str

    Valida dos cadenas y corrige si algun caracter no corresponde

    >>> reparar_dano('atg', 'aag')
    'tac'

    >>> reparar_dano('atg', 'tac')
    'No presenta errores'

    :param adn: str que representa la cadena base
    :param complementaria: str que representa la cadena complementaria
    :return: str que representa la cadena corregida o de no tener errores devuelve un mensaje
    """
    if corresponden(adn, complementaria):
        return "No presenta errores"
    elif not corresponden(adn, complementaria):
        return generar_cadena_complementaria(adn)


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    """
    (list of str) -> list of str

    Recibe una lista de adn y devuelve la lista de adn complementario

    >>> obtener_complementos(['aaa', 'agt', 'AAA'])
    ['ttt', 'tca', 'TTT']

    :param lista_adn: list of str que representa una lista de ADN
    :return: list of str que representa una lista de ADN complementario
    """
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    """
    (list of str) -> str

    Dada una lista de ADN retorna una cadena de ADN complementaria

    >>> lista_adn(['aaa', 'tga'])
    'tttact'

    >>> lista_adn(['TGG', 'aaa', 'TTT'])
    'ACCtttAAA'

    :param lista_adn: list of str que representa la lista de ADN
    :return: str que representa una cadena de ADN complementaria
    """
    pass
