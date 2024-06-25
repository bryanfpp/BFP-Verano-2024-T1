
def get_unique_names(procesadas):
    # Crear un conjunto (set) para eliminar los nombres duplicados
    unique_names = set(procesadas)
    
    # Convertir el conjunto a una lista y ordenarla
    sorted_names = sorted(list(unique_names))
    
    return sorted_names