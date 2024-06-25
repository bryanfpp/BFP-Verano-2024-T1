import matplotlib.pyplot as plt

def graficar_histograma(datos, bins=10,titulo="Histograma", etiqueta_x="Valores", etiqueta_y="Frecuencia"):
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.hist(datos, bins=bins)
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.show()
