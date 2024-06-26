import matplotlib.pyplot as plt

def generar_diagrama_barras(frecuancia,unique_names):
    plt.barh(unique_names,frecuancia ,
            height = 0.8, edgecolor= "k") 

    plt.gca().invert_yaxis() # Invertir el sentido del eje y
    plt.yticks(unique_names, fontsize = 10,rotation=45) # Etiquetar marcas de clase 
    plt.xlabel("Frecuencia absoluta ", fontsize = 15) # Etiqueta del eje y
    plt.ylabel("Marcas de clase", fontsize = 15) # Etiqueta del eje x
    plt.title("Diagrama de barras", fontsize = 20) # Titulo
    plt.grid() # Activar cuadricula
    plt.show() # Mostrar grafico