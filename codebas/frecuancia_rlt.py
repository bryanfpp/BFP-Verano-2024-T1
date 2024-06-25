def fr_abs(frecuancia_absoluta):
    fr = []
    fas = sum(frecuancia_absoluta)
    for elemento in frecuancia_absoluta:
        fr.append(elemento / fas)
    return(fr)