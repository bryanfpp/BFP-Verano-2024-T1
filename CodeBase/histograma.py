import matplotlib.pyplot as plt

def crear_histograma(clases, fg):
    # Tomar los primeros 6 valores de cada arreglo
    clases_6 = clases[:6]
    fr_6 = fg[:6]
    
    # Crear el histograma
    plt.figure(figsize=(8, 6))
    plt.bar(clases_6, fr_6, edgecolor='black')
    plt.xlabel('Clase')
    plt.ylabel('Frecuencia Relativa')
    plt.title('Histograma')
    
    # Agregar etiquetas a las barras
    for i, freq in enumerate(fr_6):
        plt.text(i, freq + 0.01, f"{freq:.2f}", ha='center')
    
    plt.show()