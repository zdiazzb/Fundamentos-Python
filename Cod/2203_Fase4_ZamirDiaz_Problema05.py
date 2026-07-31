# Nombre del estudiante: Zamir Alexis Diaz Barbosa
# Grupo: 213022A_2203
# Programa: FUNDAMENTOS DE PROGRAMACIÓN

# Matriz de datos del proyecto: 
# Columna 0: ID de Tarea 
# Columna 1: Estado ("Completado", "Pendiente", "En Curso") 
# Columna 2: Recurso Asignado 

DATOSPROYECTO = [ 
    [101, "Completado", "Ana"], 
    [102, "Pendiente", "Luis"], 
    [103, "En Curso", "Ana"], 
    [104, "Pendiente", "Marta"] 
] 

INDICEESTADO = 1
INDICERECURSO = 2

def ContarTareaPorEstado(matriz, estadoObjetivo):  
    try:
        if not matriz:
            exit()
        
        contador = 0 

        for tarea in matriz: 
            if tarea[INDICEESTADO] == estadoObjetivo:  
                contador += 1 
        return contador
    
    except IndexError:
        return "Error: La matriz no tiene la estructura esperada"
    except Exception as e:
        return f"Error inesperado: {str(e)}"

def ObtenerAsignacionRecurso(matriz): 
    try:
        if not matriz:
            exit()
            
        filas = len(matriz) 
        columnas = len(matriz[0]) 
        asignacionPorColumna = [] 

        for j in range(columnas):  
            columnaActual = [matriz[i][j] for i in range(filas)]  
            asignacionPorColumna.append(columnaActual) 

        return asignacionPorColumna[INDICERECURSO]
    
    except IndexError:
        return "Error: No existe la columna solicitada"
    except Exception as e:
        return f"Error inesperado: {str(e)}"

try:
    estadoBuscado = "Pendiente" 
    conteoPendientes = ContarTareaPorEstado(DATOSPROYECTO, estadoBuscado) 
    asignaciones = ObtenerAsignacionRecurso(DATOSPROYECTO) 

    print(f"Número de tareas '{estadoBuscado}': {conteoPendientes}") 
    print(f"Asignación de recursos (por columna): {asignaciones}")

except Exception as e:
    print(f"Error crítico: {str(e)}") 