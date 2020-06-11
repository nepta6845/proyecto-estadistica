from scipy.stats.contingency import margins
import numpy as np




class Distribucion():
    # Se ingresan los valores de las variables X,Y
    valores_X = [0, 1, 2]
    valores_Y = [0, 1, 2]

    # Se ingresan los valores de las probabilidades conjuntas
    probabilidades_conjunta= np.array([[1/9, 2/9, 1/9],
                                    [2/9, 2/9, 0],
                                    [1/9, 0, 0 ]])

    marginal_Y , marginal_X = margins(probabilidades_conjunta) # pylint: disable=unbalanced-tuple-unpacking

    def esperanza_marginal_X(self, valores_X, marginal_X):
        sumatoria=0
        for i in range(0,len(valores_X)):
            sumatoria=sumatoria + valores_X[i]*marginal_X[0][i]
        return sumatoria

    def esperanza_marginal_Y(self, valores_Y, marginal_Y):
        sumatoria=0
        for i in range(0,len(valores_Y)):
            sumatoria=sumatoria + valores_Y[i]*marginal_Y[i][0]
        return sumatoria


    def esperanza_conjunta(self, valores_X, valores_Y, probabilidades_conjunta):
        sumatoria=0
        for i in range(0, len(probabilidades_conjunta)):
            for j in range(0, len(probabilidades_conjunta[i])):
                sumatoria= sumatoria + valores_X[j]*valores_Y[i]* probabilidades_conjunta[i][j]
        return sumatoria


    def covarianza(self, esperanza_X, esperanza_Y, esperanza_conjunta):
        return esperanza_conjunta - (esperanza_X * esperanza_Y)


    def probabilidad_condicional_X_Y(self, probabilidades_conjunta, marginal_Y):
        matriz_condicional = probabilidades_conjunta.copy()
        for i in range(0,len(marginal_Y)):
            for j in range(0,len(probabilidades_conjunta[i])):
                resualtado = probabilidades_conjunta[i][j]/marginal_Y[i][0]
                matriz_condicional[i][j]=resualtado
        return matriz_condicional

    def probabilidad_condicional_Y_X(self, probabilidades_conjunta, marginal_X):
        matriz_condicional = probabilidades_conjunta.copy()
        for i in range(0,len(marginal_X[0])):
            for j in range(0,len(probabilidades_conjunta)):
                resualtado = probabilidades_conjunta[j][i]/marginal_X[0][i]
                matriz_condicional[j][i]=resualtado
        return matriz_condicional

    
    def esperanza_condicional_X_Y(self, probabilidad_condicional_X_Y, valores_X):
        vector_condicional=[]
        for i in range(0,len(valores_X)):
            sumatoria=0
            for j in range(0,len(probabilidad_condicional_X_Y)):
                sumatoria = sumatoria + probabilidad_condicional_X_Y[j][i]*valores_X[i]
            vector_condicional.append(sumatoria)
        return vector_condicional

    
    def esperanza_condicional_Y_X(self, probabilidad_condicional_Y_X, valores_Y):
        vector_condicional=[]
        for i in range(0,len(valores_Y)):
            sumatoria= 0
            for j in range(0,len(probabilidad_condicional_Y_X[i])):
                sumatoria = sumatoria + probabilidad_condicional_Y_X[i][j]*valores_Y[i]
            vector_condicional.append(sumatoria)
        return vector_condicional

    def desviacion_X(self, valores_variable, marginal_valores, esperanza_X):
        sumatoria=0
        for i in range(0,len(valores_variable)):
            sumatoria=sumatoria + valores_variable[i]**2*(marginal_valores[0][i])
        return np.sqrt(sumatoria-esperanza_X**2)

    def desviacion_Y(self, valores_variable, marginal_valores, esperanza_Y):
        sumatoria=0
        for i in range(0,len(valores_variable)):
            sumatoria=sumatoria + valores_variable[i]**2*(marginal_valores[i][0])
        return np.sqrt(sumatoria-esperanza_Y**2)

    def coeficiente_correlacion(self, covarianza, desviacion_X, desviacion_Y):
        return covarianza/desviacion_X*desviacion_Y

