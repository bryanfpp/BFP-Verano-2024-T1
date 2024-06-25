def ordenar_abs(clase_original):
    
    clase_sorted= []

    for elemento in clase_original:
        if elemento not in clase_sorted:
            clase_sorted.append(elemento)

    for i in range(len(clase_sorted)):

        for j in range(i+1, len(clase_sorted)):
            if clase_sorted[j] < clase_sorted[i]:
                clase_sorted[j], clase_sorted[i] = clase_sorted[i], clase_sorted[j]
    
    return clase_sorted