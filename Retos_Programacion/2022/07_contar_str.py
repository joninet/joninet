""" * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente."""

def countStr(word):
    wordNew=word.lower()
    listLetter=[]
    for x in wordNew:
        if x not in (" .,-':;[]{}"):
            countP=wordNew.count(x)
            if x not in listLetter:
                print(f"Letter {x} = cant {countP}")
                listLetter.append(x)

countStr("Hola Mundo , l dd")
