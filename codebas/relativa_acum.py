def sum_abs(relativa):
    suma= []
    suma_total= []
    s = 0
    for elemen in relativa:
        suma.append(elemen)
        s += elemen
        suma_total.append(s)
    return(suma_total)