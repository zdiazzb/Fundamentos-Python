# Nombre del estudiante: Zamir Alexis Diaz Barbosa
# Grupo: 213022A_2203
# Programa: FUNDAMENTOS DE PROGRAMACIÓN

FILAS = 5
ASIENTOSPORFILA = 10

# Función para inicializar la sala de cine
def InicializarSala():
    sala = [[0] * ASIENTOSPORFILA for _ in range(FILAS)]
    return sala

# Función para mostrar el estado de la sala
def MostrarSala(sala):
    print("\n--- Estado de la Sala ---")
    for f in range(FILAS): 
        print(f"F{f+1}:", end=" ")
        for estado in sala[f]:
            if estado == 0:
                simbolo = " D"
            elif estado == 1:
                simbolo = " V"
            elif estado == 2:
                simbolo = " R"
            print(simbolo, end="")
        print()

# Función para validar si la fila y el asiento son válidos
def ValidarAsiento(fila, asiento):
    if 1 <= fila <= 5 and 1 <= asiento <= 10:
        return 1
    return 0 

# Función para obtener el precio del asiento según la fila
def ObtenerPrecio(fila):
    if fila in (1, 2):
        return 8000
    elif fila in (3, 4):
        return 6000
    elif fila == 5:
        return 4000
    return 0

# Función para vender un asiento
def VenderAsiento(sala, fila, asiento):
    if ValidarAsiento(fila, asiento) == 0:
        return 0
    
    indice_fila = fila - 1
    indice_asiento = asiento - 1 
    
    if sala[indice_fila][indice_asiento] == 0:
        sala[indice_fila][indice_asiento] = 1
        return ObtenerPrecio(fila)
    return 0

# Función para devolver un asiento
def DevolverAsiento(sala, fila, asiento):
    if ValidarAsiento(fila, asiento) == 0:
        return 0
    
    indice_fila = fila - 1
    indice_asiento = asiento - 1
    precio_base = ObtenerPrecio(fila)

    if sala[indice_fila][indice_asiento] == 1:
        sala[indice_fila][indice_asiento] = 2
        penalidad = precio_base * 0.20
        return penalidad
    elif sala[indice_fila][indice_asiento] == 2:
        sala[indice_fila][indice_asiento] = 0
        return -1
    return 0

# Función principal del menú  
def MenuPrincipal():
    sala_cine = InicializarSala()
    ingreso_neto = 0
    total_penalidades = 0
    opcion = 0
    
    while opcion != 4:
        print("\n==============================")
        print("  Menú: Cine Full               ")
        print("================================")
        print("1. Venta de Asiento.")
        print("2. Recolección/Devolución de Asiento.")
        print("3. Mostrar Estado de la Sala.")
        print("4. Salir.")
        
        try:
            opcion = int(input("¿Cuál es su opción? "))
        except ValueError:
            print("Opción no válida.")
            continue
            
        if opcion == 1:
            print("\n--- VENTA DE ENTRADAS ---")
            try:
                f = int(input("Ingrese el número de Fila (1-5): "))
                a = int(input("Ingrese el número de Asiento (1-10): "))
            except ValueError:
                print("Fila o Asiento deben ser números enteros.")
                continue
                
            precio_venta = VenderAsiento(sala_cine, f, a)
            
            if precio_venta != 0:
                ingreso_neto += precio_venta
                print(f"Venta exitosa. Asiento F{f}-A{a} vendido por {precio_venta}.")
            else:
                print("Error en la venta. Asiento ocupado o fuera de rango.")
                
        elif opcion == 2:
            print("\n--- RECOLECCIÓN/DEVOLUCIÓN ---")
            try:
                f = int(input("Ingrese el número de Fila (1-5): "))
                a = int(input("Ingrese el número de Asiento (1-10): "))
            except ValueError:
                print("Fila o Asiento deben ser números enteros.")
                continue
                
            resultado = DevolverAsiento(sala_cine, f, a)
            
            if resultado > 0:
                total_penalidades += resultado
                print(f"Devolución solicitada para F{f}-A{a}. Penalidad aplicada: {resultado}.")
            elif resultado == -1:
                print(f"Devolución completada para F{f}-A{a}. El asiento está disponible nuevamente.")
            else:
                print(f"El asiento F{f}-A{a} no se puede procesar (puede que ya esté libre o fuera de rango).")
                
        elif opcion == 3:
            MostrarSala(sala_cine)
            
        elif opcion == 4:
            print("\n--- RESUMEN DEL DÍA ---")
            print(f"Ingreso Total Neto: {ingreso_neto}")
            print(f"Total de Penalidades Acumuladas: {total_penalidades}")
            print("¡Gracias por usar el sistema!")
            
        else:
            print("Opción no reconocida.")
 
if __name__ == "__main__":
    MenuPrincipal()