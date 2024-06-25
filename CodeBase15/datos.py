

def procesar_cadenas(mi_arreglo):
    procesadas = []
    for cadena in mi_arreglo:
        cadena_limpia = cadena.strip().upper()
        procesadas.append(cadena_limpia)
        
    return procesadas