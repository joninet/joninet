""" Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
 - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"""

def invert(word):
    for x in reversed(word):
        print(x, end=(" "))
invert("Hola Mundo")
