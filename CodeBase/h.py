import matplotlib.pyplot as plt

def histograma(datos):
    plt.figure(figsize=(8, 6))
    plt.hist(datos, bins=6, edgecolor='black') 
    plt.title('Histograma')
    plt.xlabel('Datos')
    plt.ylabel('Frecuencia')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
