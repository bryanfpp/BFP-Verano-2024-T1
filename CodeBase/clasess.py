def get_class_info(clases, frecuancia):
    """
    Obtiene información sobre un conjunto de clases.
    
    Parámetros:
    class_boundaries (list): Una lista que contiene los límites de las clases.
                            Por ejemplo: [0, 10, 20, 30, 40, 50]
    frequencies (list): Una lista con las frecuencias de cada clase.
                       Debe tener el mismo número de elementos que class_boundaries.
    
    Devuelve:
    lower_bounds (list): Una lista con los límites inferiores de cada clase.
    upper_bounds (list): Una lista con los límites superiores de cada clase.
    class_marks (list): Una lista con las marcas de clase de cada clase.
    class_freqs (list): Una lista con las frecuencias de cada clase.
    """
    lower_bounds = clases[:-1]
    upper_bounds = clases[1:]
    class_marks = [(lower + upper) / 2 for lower, upper in zip(lower_bounds, upper_bounds)]
    class_freqs = frecuancia
    
    return lower_bounds, upper_bounds, class_marks, class_freqs