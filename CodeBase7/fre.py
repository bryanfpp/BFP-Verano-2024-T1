def contar_nombres_unicos(mi_arreglo):
    """
    Recibe un arreglo de nombres y devuelve dos arreglos: 
    uno con los nombres únicos y otro con sus frecuencias.
    """
    frecuencia = {}
    
    # Recorrer el arreglo de nombres
    for nombre in mi_arreglo:
        # Si el nombre ya está en el diccionario, incrementar su frecuencia
        if nombre in frecuencia:
            frecuencia[nombre] += 1
        # Si el nombre no está en el diccionario, agregarlo con frecuencia 1
        else:
            frecuencia[nombre] = 1
    
    # Crear dos listas separadas: una de nombres y otra de frecuencias
    nombres_unicos = list(frecuencia.keys())
    frecuencias = list(frecuencia.values())
    
    return nombres_unicos, frecuencias