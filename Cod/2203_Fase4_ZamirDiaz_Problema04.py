# Nombre del estudiante: Zamir Alexis Diaz Barbosa
# Grupo: 213022A_2203
# Programa: FUNDAMENTOS DE PROGRAMACIÓN

INVENTARIO = [ 
    {"producto": "Camisa Casual", "stock": 12, "ventas_prom": 5}, 
    {"producto": "Pantalón Denim", "stock": 4, "ventas_prom": 8}, 
    {"producto": "Chaqueta Lona", "stock": 8, "ventas_prom": 3} 
] 

STOCKMINIMOSEGURIDAD = 10  

# Función para calcular la cantidad a pedir
def CalcularPedido(stockActual, stockMinimo):
   
    try:
        stockVal = int(stockActual)
        minVal = int(stockMinimo)
    except Exception:
        return 0

    if stockVal < minVal:
        return minVal - stockVal
    return 0

# Función para clasificar la prioridad del pedido
def ClasificarPrioridad(stock):    
    try:
        nivel = int(stock)
    except Exception:
        nivel = 0

    if nivel < 5:
        return "Alta"
    
    if nivel < 10:
        return "Media"
    
    return "Baja"

# Función para generar el informe de inventario
def GenerarInformeInventario(datos):
    
    for item in datos:
        nombre = item.get('producto', 'Desconocido')
        stockActual = item.get('stock', 0)

        try:
            cantidadAPedir = CalcularPedido(stockActual, STOCKMINIMOSEGURIDAD)
            prioridadPedido = ClasificarPrioridad(stockActual)
            print(f"Producto: {nombre} | Prioridad: {prioridadPedido} | Pedir: {cantidadAPedir}")
        except Exception as e:
            print(f"Error procesando {nombre}: {e}")


GenerarInformeInventario(INVENTARIO)