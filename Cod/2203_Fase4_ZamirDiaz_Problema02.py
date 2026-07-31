# Nombre del estudiante: Zamir Alexis Diaz Barbosa
# Grupo: 213022A_2203
# Programa: FUNDAMENTOS DE PROGRAMACIÓN

LIMITEBONO = 5000

MESES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

VENTASPORMES = {
    "enero": 1500, 
    "febrero": 2200, 
    "marzo": 1800
}

# AgregarVentas: Agrega un nuevo mes de ventas al diccionario.
def AgregarVentas(datosActuales, mes, monto):
    datosActuales[mes] = monto
    return list(datosActuales.values())

# RevisarBono: Verifica si el vendedor califica para un bono.
def RevisarBono(ventasTotales, limite):
    if ventasTotales > limite:
        montoBono = ventasTotales / limite
        print(f"¡Felicidades! Gana un bono de: {montoBono}")
    else:
        print("Siga esforzándose para el bono.")

# SolicitarDatos: Solicita un nombre y una cantidad al usuario.
def SolicitarDatos():
    nombreVendedor = input("Ingrese su nombre: ").strip()
    if not nombreVendedor:
        print("Nombre inválido.")
        exit()

    from datetime import datetime
    mesActual = MESES[datetime.now().month - 1]

    try:
        cantidadNueva = int(input(f"Ingrese las ventas de {mesActual}: "))
    except ValueError:
        print("Entrada inválida.")
        exit()

    if cantidadNueva < 0:
        print("Ventas no pueden ser negativas.")
        exit()

    return nombreVendedor, cantidadNueva, mesActual

contador = 1
while contador <= 3:
    print(f"\n--- Iteración {contador} ---")
    vendedor, nuevasVentas, mes = SolicitarDatos()
    VENTASPORMESNUEVO = AgregarVentas(VENTASPORMES, mes, nuevasVentas)
    totalAnual = sum(VENTASPORMESNUEVO)

    try:
        RevisarBono(totalAnual, LIMITEBONO)
        print(f"Ventas de {vendedor}: {totalAnual}. Ventas de {mes}: {VENTASPORMES[mes]}")
    except Exception as e:
        print("Ocurrió un problema en el cálculo final.")
    contador += 1 
    