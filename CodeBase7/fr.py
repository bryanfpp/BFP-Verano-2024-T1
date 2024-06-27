def fr_abs(frecuancia):
    fr = []
    fas = sum(frecuancia)
    for elemento in frecuancia:
        fr.append(elemento / fas)
    return(fr)