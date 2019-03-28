def obtener_complemento(base):
    # retorna caracter
    pass


def generar_cadena_complementaria(adn):
    com = ''
    if int == type(adn):
        raise TypeError('No puede tener numeros')
    for letra in adn:
        com += obtener_complemento(letra)
    return com


def calcular_correspondencia(adn1, adn2):
    # retorna num
    pass


def corresponden(adn1, adn2):
    return generar_cadena_complementaria(adn1) == adn2


def es_cadena_valida(adn):
    pass


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
