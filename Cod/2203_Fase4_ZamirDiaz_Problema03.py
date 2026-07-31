# Nombre del estudiante: Zamir Alexis Diaz Barbosa
# Grupo: 213022A_2203
# Programa: FUNDAMENTOS DE PROGRAMACIÓN

# Datos iniciales de los empleados
DATOSEMPLEADOS = [
    {"nombre": "Ana García", "horas": 160, "tarifa": 15.5},
    {"nombre": "Luis Pérez", "horas": 150, "tarifa": 18.0},
    {"nombre": "Marta López", "horas": 165, "tarifa": 12.0}
]

# Porcentaje de descuento aplicado al salario bruto
TASADESCUENTO = 0.15

# Calcula el salario bruto dadas las horas trabajadas y la tarifa por hora
def CalcularBruto(horasTrabajadas, tarifaHora):
    return float(horasTrabajadas * tarifaHora)

# Calcula el salario neto aplicando el descuento correspondiente
def CalcularNeto(salarioBruto):
    descuento = salarioBruto * TASADESCUENTO
    return salarioBruto - descuento

# Genera e imprime un informe con el salario neto de cada empleado
def GenerarInforme(listaEmpleados):
    for empleado in listaEmpleados:
        nombre = empleado['nombre']
        horas = empleado['horas']
        tarifa = empleado['tarifa']
        salarioBruto = CalcularBruto(horas, tarifa)
        salarioNeto = CalcularNeto(salarioBruto)
        print(f"Informe de {nombre}: Salario Neto: ${salarioNeto:.2f}")

GenerarInforme(DATOSEMPLEADOS)