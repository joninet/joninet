#Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directa

def decAbin(num: int):
    numBin = ""
    while num > 0:
        binDiv = num % 2
        numBin = numBin + str(binDiv)
        num = num // 2

    return numBin[::-1]

print(decAbin(123))
