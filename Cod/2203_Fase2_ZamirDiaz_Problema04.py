# Nombre del estudiante: Zamir Alexis Diaz Barbosa
# Grupo: 213022A_2203
# Programa: FUNDAMENTOS DE PROGRAMACIÓN

# Constantes
IVA = 0.19
RECARGOLUJO = 0.05

# Solicita el precio del producto
try:
    entrada = input("Ingrese el precio base del producto: ")
    entradaLimpia = entrada.replace('.', '').replace(',', '')

    precioIngresadoInp = float(entradaLimpia)

    if precioIngresadoInp <= 0:
        print("Error: El precio debe ser mayor a 0.")
        exit()    

except ValueError:
    print("Error: Asegurese que el valor ingresado contenga unicamente caracteres numericos")
    exit()

# Función encargada de validar si un código de producto es válido
def productoValido(codigoProducto):
    return codigoProducto >= 1 and codigoProducto <= 3

# Solicita el código de producto
try:
    codigoProductoInp = int(input("Ingrese el código de producto (1: Básico, 2: Estándar, 3: Lujo): "))
    if not productoValido(codigoProductoInp):
        print("Error: El código debe ser 1, 2 o 3.")
        exit()

except ValueError:
    print("Error: Los códigos de producto disponible son: 1, 2 o 3")

# Fución encargada de retornar el valor de un producto apartir de un código y precio de producto
def obtenerValorxProductor(codigoProducto, precioProducto):    
    valor = 0
    
    if codigoProducto == 1:
        valor = precioProducto
        
    if codigoProducto == 2:
        valorIva = precioProducto * IVA
        valor = precioProducto + valorIva
        
    if codigoProducto == 3:
        valorIva = precioProducto * IVA
        valorRecargo = precioProducto * RECARGOLUJO
        valor = precioProducto + valorIva + valorRecargo
        
    return valor

valorFinal = obtenerValorxProductor(codigoProductoInp, precioIngresadoInp)
print(f"El valor final del producto es: {valorFinal:,.2f}")