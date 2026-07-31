# Nombre del estudiante: Zamir Alexis Diaz Barbosa
# Grupo: 213022A_2203
# Programa: FUNDAMENTOS DE PROGRAMACIÓN

# Representa la matriz de datos iniciales
registroLaboral = [
    ["Sergio Pedraza", 8, 8, 8, 8, 8],
    ["Carlos Perez", 9, 9, 8, 9, 8],
    ["Miguel Ojeda", 7, 8, 8, 7, 8],
    ["Marta Lopez", 10, 8, 9, 8, 10]
]

# Función encargada de clasificar la jornada de acuerdo al total del horas
def ClasificarJornada(totalHoras):
    
    if totalHoras > 40:
        #\033[31m y \033[0m: Permite aplicar color rojo al texto
        return "\033[31mSobretiempo\033[0m"
    
    #\033[32m y \033[0m: Permite aplicar color verde al texto
    return "\033[32mHorario estándar\033[0m"

# Función encargada de calcular las horas trabajadas y asignar una clasificación
def EvaluarJornadas(matrizHoras):

    resultadosProcesados = []
    
    for recurso in matrizHoras:

        nombreRecurso = recurso[0]
        totalHoras = sum(recurso[1:])
        tipoJornada = ClasificarJornada(totalHoras)
        
        resultadosProcesados.append({
            "Nombre": nombreRecurso,
            "Horas": totalHoras,
            "Clasificacion": tipoJornada
        })
        
    return resultadosProcesados

# Función encargada de ordenar las horas de mayor a menor
def OrdenarHoras(datosReporte):

    return sorted(datosReporte, key=lambda empleado: empleado['Horas'], reverse=True)

# Función encargada de mostrar el reporte del registro laboral 
def MostrarReporte(datosReporte): 

    if not datosFinales:
        print(".: No se encontraron registros para presentar :.\n")
        exit()

    print(f"\n{'Nombre':<14} | {'Horas Totales':^13} | {'Clasificación'}")
    print("==============================================")

    datosOrdenados = OrdenarHoras(datosReporte)

    for empleado in datosOrdenados:
        print(f"{empleado['Nombre']:<14} | {empleado['Horas']:^13} | {empleado['Clasificacion']}")


print("\n.: Inicia generación de reporte :.")

datosFinales = EvaluarJornadas(registroLaboral)
MostrarReporte(datosFinales)

print("\n.: Reporte generado con éxito :.\n")