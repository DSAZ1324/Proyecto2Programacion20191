def obtener_complemento(base):
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
    if not es_cadena_valida(adn2):
        raise ValueError(adn2 + ' no es una base')
    return generar_cadena_complementaria(adn1) == adn2


def es_cadena_valida(adn):
    for letra in adn:
        base = es_base(letra)
        if base:
            return True
        if not base:
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
    pass


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
    pass


def obtener_complementos(lista_adn):

    com = []
    for cadena in lista_adn:
        com.append(generar_cadena_complementaria(cadena))
    return com


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):

    com = ''
    for cadena in lista_adn:
        com += generar_cadena_complementaria(cadena)
    return com
