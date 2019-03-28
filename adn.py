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
    """
    str -> str

    Transforma una cadena de ADN a su cadena complementaria

    >>> generar_cadena_complementaria('agtc')
    'tcag'

    >>> generar_cadena_complementaria('AAA')
    'TTT'

    >>> generar_cadena_complementaria(1)
    Traceback (most recent call last):
    ...
    TypeError: No puede tener numeros

    >>> generar_cadena_complementaria('z')
    Traceback (most recent call last):
    ..
    ValueError: z no es una base

    :param adn: str que representa una cadena de ADN
    :return: str que representa la cadena complementaria de ADN
    """
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
    complementorea = generar_cadena_complementaria(adn1)
    print (complementorea)

    total = len(adn2)
    print(total)
    coincidencias = 0
    cont = 0
    while (cont < total):
        if(adn2[cont] == complementorea[cont]):
            coincidencias = coincidencias + 1
        cont = cont + 1
        porcentaje = (coincidencias+100) / total
    return porcentaje


def corresponden(adn1, adn2):
    """
    (str, str) -> bool

    Valida si dos cadenas de ADN corresponden entre su base y complementaria

    >>> corresponden('AAAA', 'TTTT')
    True

    >>> corresponden('atg', 'ttt')
    False

    >>> corresponden('1', 't')
    Traceback (most recent call last):
    ..
    ValueError: 1 no es una base

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
    """
    str) -> boolean
  con esta funciopn se quiere validar que las cadena sea valida a la base dada

    >>> es_cadena_valida('ATCG')
    False
    >>> es_cadena_valida('MNBP')
    False

    :param adn: La cadena ingresada a evaluar
    :return: True si la cadena de ADN es valida, False si no se cumple
    """
    base = es_base
    if not es_base(base):
        return False
    return True


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
    com = []
    for cadena in lista_adn:
        com.append(generar_cadena_complementaria(cadena))
    return com


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adnn):
    """
    (list of str) -> str

    Dada una lista de ADN retorna una cadena de ADN complementaria

    >>> complementar_cadenas(['aaa', 'ttt', 'ccc'])
    'tttaaaggg'

    >>> complementar_cadenas(['AGT', 'GCC', 'TTT'])
    'TCACGGAAA'

    :param lista_adnn: list of str que representa la lista de ADN
    :return: str que representa una cadena de ADN complementaria
    """
    com = ''
    for cadena in lista_adnn:
        com += generar_cadena_complementaria(cadena)
    return com
