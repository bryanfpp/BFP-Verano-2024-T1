import matplotlib.pyplot as plt

def histograma(datos):
        # a. Histograma de seis clases
        plt.figure(figsize=(10,6))
        plt.hist(datos, bins=6, edgecolor='black')
        plt.xlabel('Valor')
        plt.ylabel('Frecuencia')
        plt.title('Histograma de los datos')
        plt.show()
        