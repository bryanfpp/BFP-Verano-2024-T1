def frecuancia_abs(datos):
   
    clase_original,frecuencia= [],[]

    for elemento in datos:    
        if elemento not in clase_original:
            clase_original.append(elemento)
            frecuencia.append(1)
        else:
            inde = clase_original.index(elemento)
            frecuencia[inde] += 1
            
    return clase_original,frecuencia
        