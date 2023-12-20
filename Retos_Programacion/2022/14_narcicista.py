"""Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información al respecto."""

def Narcisista(numero):
    numStr=str(numero)
    cant=len(numStr)
    esNarci=sum(int(x) ** cant for x in numStr)
    # al final se pone el for y al principio la operacion dentro del for
    return numero == esNarci

numero_ejemplo1 = 153
numero_ejemplo2 = 25

print(f"{numero_ejemplo1} es un número de Armstrong: {Narcisista(numero_ejemplo1)}")
print(f"{numero_ejemplo2} es un número de Armstrong: {Narcisista(numero_ejemplo2)}")
