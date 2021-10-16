def palind(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    invert = palabra [::-1]
    if palabra == invert:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra: ')
    es_palin = palind(palabra)
    if es_palin == True:
        print('Es palíndromo')
    else:
        print('No es palíndromo')


if __name__ == '__main__':
    run()