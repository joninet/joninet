codigoMorse = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

def Morce(palabra):
    #join lo que hace es unir los elemenfos generados por el for
    #el metodo get es propio de los diccionarios y devuelve lo que vos le indiques cuando no encuentra
    return " ".join(codigoMorse.get(x, "   ") for x in palabra.upper())

print(Morce("Hola Mundo"))