import matplotlib.pyplot as plt

def crear_diagrama_pastel(unique_names, frecuancia, titulo="Diagrama de Pastel"):
   
    plt.figure(figsize=(8, 6))  # Tamaño de la figura (ancho, alto)
    plt.pie(frecuancia, labels=unique_names, autopct='%1.1f%%', startangle=140)
    plt.title(titulo)
    plt.axis('equal')  # Asegura que el pastel sea dibujado como un círculo
    plt.show()

# Ejemplo de uso:
etiquetas = ['Manzanas', 'Plátanos', 'Peras', 'Naranjas']
tamaños = [15, 30, 45, 10]  # Porcentajes (sumando 100)
crear_diagrama_pastel(etiquetas, tamaños, titulo="Ejemplo de Diagrama de Pastel")
