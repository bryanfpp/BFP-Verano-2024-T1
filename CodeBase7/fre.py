def contar_repeticiones_por_cadena(resultado):
    conteo = {}
    for cadena in resultado:
        if cadena in conteo:
            conteo[cadena] += 1
        else:
            conteo[cadena] = 1
    
    resultados = []
    for valor in conteo.values():
        resultados.append(valor)
    
    return resultados