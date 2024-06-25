def sum_abs(frec):
    suma= []
    suma_total= []
    s = 0
    for elemen in frec:
        suma.append(elemen)
        s += elemen
        suma_total.append(s)
    return(suma_total)