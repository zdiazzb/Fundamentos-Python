# Nombre del estudiante: Zamir Alexis Diaz Barbosa
# Grupo: 213022A_2203
# Programa: FUNDAMENTOS DE PROGRAMACIÓN

# Constantes
TOTAL_FANATICOS = 3

# Representa el listado de posibles articulos que el usuario puede ingresar
articulosValidos = ["camiseta", "chaqueta", "gorra", "morral"]

# Almacena los articulos disponibles con la cantidad de elecciones
conteoArticulos = {"camiseta": 0, "chaqueta": 0, "gorra": 0, "morral": 0}

# Almacena los equipos favoritos de cada usuario
conteoEquipos = {}

# Almacena las edades de cada usuario
edadesEquipos = {}

# Representa la cantidad total de dias que van al estadio los tres usuarios
diasTotalEstadio = 0

# Función encargada de tomar los datos ingresados por cada usuario y sumarlos a los objetos de acumulación
def AcumularInformacion(equipo, articulo, edad, dias):
    if equipo not in conteoEquipos:
        conteoEquipos[equipo] = 0
        edadesEquipos[equipo] = 0
        
    conteoEquipos[equipo] += 1
    conteoArticulos[articulo] += 1

    edadesEquipos[equipo] += edad   

    global diasTotalEstadio
    diasTotalEstadio += dias

# Función encargada de solicitar los datos a de los usuarios
def SolicitarDatos():

    for i in range(TOTAL_FANATICOS):        
        print(f"\nInformación fanatico #{i + 1}:")

        equipoIngresado = input("Equipo de fútbol favorito: ").lower()
        if equipoIngresado == "":
            print("Error: El nombre del equipo no puede estar vacío.")
            exit()
            
        articuloIngresado = input("Artículo preferido (camiseta, chaqueta, gorra, morral): ").lower()            
        if articuloIngresado not in articulosValidos:
            print("Error: Artículo deportivo no reconocido. Intente de nuevo.")
            exit()
            
        try:
            edadIngresada = int(input("Edad del fanático: "))
            if(edadIngresada <= 0):
                print("Error: La edad debe ser mayor a 0 y los días no pueden ser negativos.")
                exit()

        except ValueError:
            print("Error: El valor ingresado debe ser estrictamente numérico.")
            exit()


        try:  
            diasAsisteEstadio = int(input("Días al año que asiste al estadio: "))        
            if diasAsisteEstadio < 0:
                print("Error: Los días no pueden ser negativos.")
                exit()

        except ValueError:
            print("Error: El valor ingresado debe ser estrictamente numérico.")
            exit()
            
        AcumularInformacion(equipoIngresado, articuloIngresado, edadIngresada, diasAsisteEstadio)


SolicitarDatos()
print("\n.: Fin de solicitud de datos :.")

# Función encargada de mostrar los resultados en pantalla
def MostrarResultados():
    
    for equipo, cantidadFanaticos in conteoEquipos.items():
        edadPromedioEquipo = int(edadesEquipos[equipo] / cantidadFanaticos)
        print(f"* El equipo {equipo} tiene {cantidadFanaticos} fanático(s) y su edad promedio es de {edadPromedioEquipo} años")
        
    articuloFavorito = ""
    maxVotos = 0
    for articulo, votosxArticulo in conteoArticulos.items():
        if votosxArticulo > maxVotos:
            maxVotos = votosxArticulo
            articuloFavorito = articulo
            
        elif votosxArticulo == maxVotos and votosxArticulo > 0:
            articuloFavorito = articuloFavorito + ", " + articulo
            
    print(f"* Artículo(s) preferido(s) por los fanáticos: {articuloFavorito}, con un total de {maxVotos} votos.")
    
    promedioDias = int(diasTotalEstadio / TOTAL_FANATICOS)
    print(f"* El promedio de días de asistencia al estadio es {promedioDias} días.")

print(".: Inicia procesamiento de información :.\n")
MostrarResultados()