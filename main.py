from statistic1 import Distribucion
import utilities as u

def imprimir_resultados():
    
    distribucion = Distribucion()
    print("Distribución marginal de X Px: \n")
    u.imprimir_arregloNx1(distribucion.marginal_X)
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    print("Distribución marginal de Y Py: \n")
    u.imprimir_arreglo1xN(distribucion.marginal_Y)
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

    esperanza_X = distribucion.esperanza_marginal_X(distribucion.valores_X,distribucion.marginal_X)
    esperanza_Y = distribucion.esperanza_marginal_Y(distribucion.valores_Y,distribucion.marginal_Y)

    print("\nValor esperado de X: \n")
    print(esperanza_X)
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    print("\nValor esperado de Y: \n")
    print(esperanza_Y)
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

    probabilidad_condicional_X_Y = distribucion.probabilidad_condicional_X_Y(distribucion.probabilidades_conjunta, distribucion.marginal_Y)
    probabilidad_condicional_Y_X = distribucion.probabilidad_condicional_Y_X(distribucion.probabilidades_conjunta, distribucion.marginal_X)

    print("\nProbabilidad condicional P(x|y): \n")
    u.imprimir_arregloNxM(probabilidad_condicional_X_Y)
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    print("\nProbabilidad condicional P(y|x): \n")
    u.imprimir_arregloNxM(probabilidad_condicional_Y_X)
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

    esperanza_condicional_X_Y=distribucion.esperanza_condicional_X_Y(probabilidad_condicional_X_Y, distribucion.valores_X)
    esperanza_condicional_Y_X=distribucion.esperanza_condicional_Y_X(probabilidad_condicional_Y_X, distribucion.valores_Y)

    print("\nValor esperado de X|Y: \n")
    print(esperanza_condicional_X_Y)
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    print("\nValor esperado de Y|X: \n")
    print(esperanza_condicional_Y_X)
    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

    esperanza_conjunta= distribucion.esperanza_conjunta(distribucion.valores_X, distribucion.valores_Y, distribucion.probabilidades_conjunta)
    covarianza = distribucion.covarianza(esperanza_X, esperanza_Y, esperanza_conjunta)
    desviacion_X = distribucion.desviacion_X(distribucion.valores_X, distribucion.marginal_X, esperanza_X)
    desviacion_Y = distribucion.desviacion_Y(distribucion.valores_Y, distribucion.marginal_Y, esperanza_Y)
    coeficiente_correlacion = distribucion.coeficiente_correlacion(covarianza, desviacion_X, desviacion_Y)

    print("\nCoeficiente de correlación: \n")
    print(coeficiente_correlacion)

    


if __name__ == "__main__":
    imprimir_resultados()