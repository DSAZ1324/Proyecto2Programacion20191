def obtener_complemento(base):
    # retorna caracter
    pass


def generar_cadena_complementaria(adn):
    """
    str -> str

    Transforma una cadena de ADN a su cadena complementaria

    >>> generar_cadena_complementaria('agtc')
    'tcag'

    >>> generar_cadena_complementaria('AAA')
    'TTT'

    :param adn: str que representa una cadena de ADN
    :return: str que representa la cadena complementaria de ADN
    """
    complementario = {'a': 't', 'A': 'T', 't': 'a', 'T': 'A', 'c': 'g', 'C': 'G', 'g': 'c', 'G': 'C'}
    com = ''
    for letra in adn:
        com += complementario[letra]
    return com


def calcular_correspondencia(adn1, adn2):
    # retorna num
    pass


def corresponden(adn1, adn2):
    """
    (str, str) -> bool

    Valida si dos cadenas de ADN corresponden entre su base y complementaria

    >>> corresponden('AAAA', 'TTTT')
    True

    >>> corresponden('atg', 'ttt')
    False

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
    pass
