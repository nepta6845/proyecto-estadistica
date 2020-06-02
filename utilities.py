def imprimir_arregloNx1(arreglo):
    for i in  range(0,len(arreglo)):
        if (i < len(arreglo)-1):
            print(arreglo[i][0],"  ", end = '')
        else:
             print(arreglo[i][0])


def imprimir_arreglo1xN(arreglo):
    for i in  range(0,len(arreglo[0])):
        if (i < len(arreglo[0])-1):
            print(arreglo[0][i],"  ", end = '')
        else:
             print(arreglo[0][i])



def imprimir_arregloNxM(arreglo):
    for i in  range(0,len(arreglo)):
        for j in  range(0,len(arreglo[i])):
            if (j < len(arreglo[i])-1):
                print(arreglo[i][j],"   ", end = '')
            else:
                print(arreglo[i][j])