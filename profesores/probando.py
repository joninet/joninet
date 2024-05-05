from helpers.funciones_db import FuncionesDB

verDb = FuncionesDB()

alumnos = verDb.mostrarTabla("alumnos")
parciales = verDb.mostrarTabla("parciales")
colegios = verDb.mostrarTabla("colegios")
materias = verDb.mostrarTabla("materias")
grados = verDb.mostrarTabla("grados")
notas2 = verDb.mostrarTabla("notas")

resultados=[]

for x in notas2:
    codigo = x[0]
    fecha = x[1]
    nota = x[2]
    rec1 = x[3]
    rec2 = x[4]
    rec3 = x[5]
    for alumno in alumnos:
        if alumno[0] == x[6]:
            alumno_nombre = alumno[2]
    for parcial in parciales:
        if parcial[0] == x[7]:
            parcial_nombre = parcial[1]
            for materia in materias:
                if materia[0] == parcial[2]:
                    materia_nombre=materia[1]
                    for colegio in colegios:
                        if colegio[0] == materia[2]:
                            colegio_nombre = colegio[1]
                    for grado in grados:
                        if grado[0] == materia[3]:
                            grado_nombre = grado[1] + grado[2]

    resultados.append({
    "codigo": codigo,
    "fecha": fecha,
    "nota": nota,
    "rec1": rec1,
    "rec2": rec2,
    "rec3": rec3,
    "alumno_nombre": alumno_nombre,
    "parcial_nombre": parcial_nombre,
    "materia_nombre": materia_nombre,
    "colegio_nombre": colegio_nombre,
    "grado_nombre": grado_nombre})

