def sum_abs(fg):
    suma= []
    suma_total= []
    s = 0
    for elemen in fg:
        suma.append(elemen)
        s += elemen
        suma_total.append(s)
    return(suma_total)