def fr_abs(fre_or):
    fr = []
    fas = sum(fre_or)
    for elemento in fre_or:
        fr.append(elemento / fas)
    return(fr)