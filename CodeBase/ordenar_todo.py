def fac_to(repeticion, clase_sorted, clases_originales):
    fa_sorted = []
    for elemento in clase_sorted:
        idx = clases_originales.index(elemento)
        fas = repeticion[idx]
        fa_sorted.append(fas)
        
    return fa_sorted