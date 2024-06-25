def obtener_limites(fa_sorted):

    if not fa_sorted:
        return [0], [0], [0]
    
    limite_inferior = [min(fa_sorted)]
    limite_superior = [max(fa_sorted)]
    
    # Calcular la marca de clase
    rango = limite_superior[0] - limite_inferior[0]
    num_clases = len(fa_sorted)  # Número de clases que se utilizarán
    amplitud_clase = rango / num_clases
    marca_clase = [limite_inferior[0] + amplitud_clase / 2]
    
    return limite_inferior, limite_superior, marca_clase