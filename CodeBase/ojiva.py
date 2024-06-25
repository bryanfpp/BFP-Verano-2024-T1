import matplotlib.pyplot as plt

def crear_ojiva(datos):
    """
    Genera la gráfica de la ojiva a partir de los primeros 6 datos de una lista.

    Args:
        datos (list): Lista de datos numéricos.

    Returns:
        None
    """
    # Tomar solo los primeros 6 números de la lista de datos
    datos = datos[:6]

    # Ordenar los datos de menor a mayor
    datos.sort()

    # Calcular las frecuencias acumuladas
    frecuencia_acumulada = [100 * sum(datos[:i+1]) / sum(datos) for i in range(len(datos))]

    # Agregar 0 al inicio para que inicie desde el eje y=0
    datos.insert(0, 0)
    frecuencia_acumulada.insert(0, 0)

    # Graficar la ojiva
    plt.figure(figsize=(8, 6))
    plt.plot(datos, frecuencia_acumulada, marker='o', linestyle='-')
    plt.title('Ojiva')
    plt.xlabel('Datos')
    plt.ylabel('Porcentaje acumulado')
    plt.grid(True)
    plt.xticks(datos)
    plt.yticks([i for i in range(0, 101, 10)])
    plt.tight_layout()
    plt.show()