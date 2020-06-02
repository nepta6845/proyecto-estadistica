from statistic1 import Distribucion

def imprimir_resultados():
    
    distribucion = Distribucion()

    print(distribucion.marginal_X.T)
    print(distribucion.marginal_Y)

    esperanza_X = distribucion.esperanza_marginal_X(distribucion.valores_X,distribucion.marginal_X)
    esperanza_Y = distribucion.esperanza_marginal_Y(distribucion.valores_Y,distribucion.marginal_Y)
    esperanza_conjunta= distribucion.esperanza_conjunta(distribucion.valores_X, distribucion.valores_Y, distribucion.probabilidades_conjunta)
    covarianza = distribucion.covarianza(esperanza_X, esperanza_Y, esperanza_conjunta)
    probabilidad_condicional_X_Y = distribucion.probabilidad_condicional_X_Y(distribucion.probabilidades_conjunta, distribucion.marginal_Y)
    probabilidad_condicional_Y_X = distribucion.probabilidad_condicional_Y_X(distribucion.probabilidades_conjunta, distribucion.marginal_X)
    desviacion_X = distribucion.desviacion_X(distribucion.valores_X, distribucion.marginal_X, esperanza_X)
    desviacion_Y = distribucion.desviacion_Y(distribucion.valores_Y, distribucion.marginal_Y, esperanza_Y)
    coeficiente_correlacion = distribucion.coeficiente_correlacion(covarianza, desviacion_X, desviacion_Y)
    

    


if __name__ == "__main__":
    imprimir_resultados()