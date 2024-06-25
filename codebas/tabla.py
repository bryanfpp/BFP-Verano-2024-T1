# Imprimir tabla
def printTable(encabezados, contenido):
    
    from tabulate import tabulate
    if(len(encabezados) == len(contenido)):
        data = list(zip(*contenido))
        table = tabulate(data, headers=encabezados, tablefmt="orgtbl")
        print(table)
