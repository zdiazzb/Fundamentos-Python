# Nombre del estudiante: Zamir Alexis Diaz Barbosa
# Grupo: 213022A_2203
# Programa: FUNDAMENTOS DE PROGRAMACIÓN

# Constantes
PRECIOS = [2500, 2000, 3800, 4500, 1800]
PRODUCTOS = ["Vaso de helado", "Choco cono", "Paleta Drácula", "Polet", "Platillo"]

# Almacena los helados comprados
conteoCompras = {}

# Representa el total de dinero gastado en la compra
totalGastado = 0

# Representa el total de helados comprados
heladosComprados = 0

# Representa el dinero que el usuario tiene disponible para comprar
dineroDisponible = 0

# Función encargada de solicitar al usuario el dinero disponible para la compra
def SolicitarDineroDisponible():
    try:
        global dineroDisponible
        dineroIngresado = input("Ingrese el dinero disponible para la compra: ")
        dineroDisponible = float(dineroIngresado.replace('.', ''))
        
        if dineroDisponible <= 0:
            print("Error: El presupuesto debe ser mayor a 0")
            exit()

        valorMinimo = min(PRECIOS)
        if dineroDisponible < min(PRECIOS):
            print(f"Error: El valor minimo aceptado es: {valorMinimo}")
            exit()

    except ValueError:
        print("Error: Ingrese un valor numérico válido.")
        exit()

SolicitarDineroDisponible()     

# Función encargada de mostrar el menú disponible
def MostrarMenu(): 
    print("\n.: Menu :.")
    print("\n1: Vaso de helado ($2.500)\n2: Choco cono ($2.000)\n3: Paleta Drácula ($3.800)\n4: Polet ($4.500)\n5: Platillo ($1.800)\n0: FINALIZAR COMPRA")

MostrarMenu()

# Función encargada de acumular información de los helados comprados
def AcumularInformacion(producto, precio):
    if producto not in conteoCompras:
        conteoCompras[producto] = 0
    
    global heladosComprados
    heladosComprados += 1
    conteoCompras[producto] += 1

    global totalGastado
    totalGastado += precio

    global dineroDisponible
    dineroDisponible -= precio

# Función encargada de procesar los elementos seleccionados a comprar
def ProcesarCompra():
    while dineroDisponible > min(PRECIOS):
        print(f"\nPresupuesto disponible: ${dineroDisponible:,.0f}")
        
        try:
            opcionIngresada = input("Seleccione el helado que desea comprar (0-5): ")
            opcionSeleccionada = int(opcionIngresada)

        except ValueError:
            print("Error: Ingrese un número de opción válido.")
            continue

        if opcionSeleccionada == 0:
            print("\n.: Finalizando compras :.")
            break
            
        if not (opcionSeleccionada >= 1 and opcionSeleccionada <= 5):
            print("Error: Ese tipo de helado no existe en el menú.")
            continue

        indiceProducto = opcionSeleccionada - 1
        precioProducto = PRECIOS[indiceProducto]
        
        puedeComprar = dineroDisponible >= precioProducto
        
        if not puedeComprar:
            print(f"Fondos insuficientes.")
            break;
                
        AcumularInformacion(PRODUCTOS[indiceProducto], precioProducto)

ProcesarCompra()

# Función encargada de mostrar el resultado de la información obtenida
def MostrarResultados():
    if heladosComprados > 0:
        print(f"\n* Total de helados comprados: {heladosComprados}")
        
        print(f"* Valor total gastado: ${totalGastado:,.0f}")

        valorPromedio = totalGastado / heladosComprados
        print(f"* Valor promedio por helado: ${valorPromedio:,.0f}")

        for producto, cantidad in conteoCompras.items():
            print(f"* {producto}: {cantidad} unidad(es)")

        print(f"* Dinero sobrante: ${dineroDisponible:,.0f}")
        
    if heladosComprados == 0:
        print("* No se compraron helados.")

MostrarResultados()