""" * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo."""

def Poligono(tipo,*args):
    if tipo == "Triangulo":
        base,altura=args
        area=(base * altura) // 2
        return f"el area de un Triangulo es {area}"
    elif tipo == "Cuadrado" or tipo == "Rectangulo":
        base,altura=args
        area = (base * altura)
        return f"el area de un {tipo} es {area}"
    else:
        return f"Tipo no disponible"

    
print(Poligono("Cuxadrado", 13, 4))
