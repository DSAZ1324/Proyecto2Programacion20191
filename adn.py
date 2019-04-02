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
    TypeError: 1 no es una base

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
    >>> calcular_correspondencia('CGTA','GCTT')
    50.0
    >>> calcular_correspondencia('ATAT','CGAT')
    0.0

    :param adn1: str con el adn a intrucir
    :param adn2: str con la segunda prueba de adn
    :return: num con el procentaje de la cadena
    """
    ubicacion = 0
    porcentaje = 0

    if len(adn1) == len(adn2):
        for i in adn1:
            if corresponden(i, adn2[ubicacion]):
              porcentaje += 1
              ubicacion += 1
        return porcentaje * 100 / len(adn2)
    return 0.0



def corresponden(adn1, adn2):
    """
    (str, str) -> bool

    Valida si dos cadenas de ADN corresponden entre su base y complementaria

    >>> corresponden('AAAA', 'TTTT')
    True

    >>> corresponden('atg', 'ttt')
    False

    :param adn1: str que representa la cadena base de ADN
    :param adn2: str que representa la cadena complementaria de ADN
    :return: bool que representa si la cadena complementaria corresponde a la de base
    """
    if not es_cadena_valida(adn2):
        raise ValueError(adn2 + ' no es una base')
    return generar_cadena_complementaria(adn1) == adn2


def es_cadena_valida(adn):
    """
    (str) -> boolean
  con esta funcion se quiere validar que las cadena sea valida a la base dada

    >>> es_cadena_valida('ATCG')
    False
    >>> es_cadena_valida('MNBP')
    False

    :param adn: La cadena ingresada a evaluar
    :return: True si la cadena de ADN es valida, False si no se cumple
    """
    for letra in adn:
        base = es_base(letra)
        if base == True:
            return True
        if base != True:
            return False
        

def es_base(caracter):
    """
    (str of len == 1) -> bool

    Valida si un caracter es una base

    >>> es_base('t')
    True

    >>> es_base('u')
    False

    :param caracter: str que representa el caracter complementario
    :return: bool que representa si es una base valida
    """
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
    false
    >>> es_subcadena('atat', '1234')
    Traceback (most recent call last):
    ..
    ValueError: 1234 no se pueden enteros

    :param adn1: str con la cadena 1
    :param adn2: str con la cadena 2
    :return: si la secuencia de la cadena 2 es subcadena de l secuencia de la cadena 1
    """
    if not es_cadena_valida(adn2):
        raise ValueError('no se pueden enteros')
    if not es_cadena_valida(adn1):
        raise ValueError('no se pueden enteros')
    if adn2 in adn1:
        return True
    elif adn2 not in adn1:
        return False


def reparar_dano(adn, complementaria):
    """
    (str, str) -> str

    Valida dos cadenas y corrige si algun caracter no corresponde

    >>> reparar_dano('atg', 'aag')
    'tac'

    >>> reparar_dano('atg', 'tac')
    'No presenta errores'

    :param adn: str que representa la cadena base
    :param complementaria: str que representa la cadena complementaria
    :return: str que representa la cadena corregida o de no tener errores devuelve un mensaje
    """
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
    ['ta', 'ata']

    >>> obtener_secciones('ATGCTACAG', 3)
    ['ATG', 'CTA', 'CAG']


    :param adn: str con la cadena de adn
    :param n: int con el numero de secciones que se quiere dividir
    :return: str con el resultado de las secciones
    """
    suma_cadenas = len(adn)//n
    division_seccion = []
    for group in range(n):
        resultado_cadena = ""
        cantidad_cadena = suma_cadenas
        if group == n-1 and len(adn) % n != 0:
            cantidad_cadena = suma_cadenas + len(adn)%n
        for caracter in range(cantidad_cadena):
            base_cadena = grupo * suma_cadenas + caracter
            resultado_cadena = resultado_cadena + adn[base_cadena]
        division_seccion.append(resultado_cadena)
    return division_seccion





def obtener_complementos(lista_adn):
    """
    (list of str) -> list of str

    Recibe una lista de adn y devuelve la lista de adn complementario

    >>> obtener_complementos(['aaa', 'agt', 'AAA'])
    ['ttt', 'tca', 'TTT']

    >>> obtener_complementos(['AGT', 'ATG', 'aaa'])
    ['TCA', 'TAC', 'ttt']

    :param lista_adn: list of str que representa una lista de ADN
    :return: list of str que representa una lista de ADN complementario
    """
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
    soluccion = ''
    for cadena in lista_adn:
        soluccion = (generar_cadena_complementaria(cadena))
        for caracter in cadena:
            soluccion = soluccion + caracter
    return soluccion


def complementar_cadenas(lista_adn):
    """
    (list of str) -> str

    Dada una lista de ADN retorna una cadena de ADN complementaria

    >>> complementar_cadenas(['aaa', 'ttt', 'ccc'])
    'tttaaaggg'

    >>> complementar_cadenas(['AGT', 'GCC', 'TTT'])
    'TCACGGAAA'

    :param lista_adn: list of str que representa la lista de ADN
    :return: str que representa una cadena de ADN complementaria
    """
    com = ''
    for cadena in lista_adn:
        com += generar_cadena_complementaria(cadena)
    return com
