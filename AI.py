import numpy as np

class LinearRegression:

    def __init__(self, X, Y):
        # X e Y para treino (60% do total para treino)
        self.X = X[:int(len(X)*0.6)] 
        self.Y = Y[:int(len(Y)*0.6)] 

        # X e Y para validação (40% do total para teste)
        self.X_val =  X[int(len(X)*0.6):] 
        self.Y_val = Y[int(len(Y)*0.6):] 

        # Média de X e Y
        self.mean_XY = np.mean([self.X, self.Y], axis=1)

        # dX e dY
        self.dX = self.X - self.mean_XY[0]
        self.dY = self.Y - self.mean_XY[1]

        # Multiplicação entre dX e dY
        self.sum_XY = np.dot(self.dX, self.dY)

        # Potencializa dX
        self.pow_X = np.sum(np.power(self.dX, 2))
    
        self.a = 0
        self.b = 0

    def training(self):
        """ Método que encontra o coeficiente angular (b) e o coeficiente linear (a)
        
        """

        self.b = self.sum_XY/self.pow_X
        self.a = self.mean_XY[1] - self.b*self.mean_XY[0]
        print("MSE: ",self.MSE())

    def MSE(self):
        """ Metodo que calcula o erro quadrático médio do inglês (Mean Squared Error)
        """

        test = np.array([self.predict(float(y)) for y in self.Y_val])
        return ((test - self.X_val)**2).mean()



    def predict(self, x):
        if type(x) not in [float, np.float64]:
            raise ValueError("O argumento de previsão precisa ser um ponto flutuante.")
        return self.b*x + self.a

    def r_squared(self):
        y_pred = np.array([self.predict(x) for x in self.X], dtype=np.float64)
        ss_res = np.sum(np.power(self.Y - y_pred, 2))
        ss_tot = np.sum(np.power(self.Y - np.mean(self.Y), 2))
        r_squared = 1 - (ss_res / ss_tot)
        return r_squared


# Exmeplo futuramente será retirado (espenrando a integração do programa)

if __name__ == "__main__":
    a = LinearRegression(X=np.array([1.1,1.3,1.5,2.0,2.2,2.9,3.0,3.2,3.2,3.7,3.9,4.0,4.0,4.1,4.5,4.9,5.1,5.3,5.9,6.0,6.8,7.1,7.9,8.2,8.7,9.0,9.5,9.6,10.,10.5]), Y=np.array([39343.00,46205.00,37731.00,43525.00,39891.00,56642.00,60150.00,54445.00,64445.00,57189.00,63218.00,55794.00,56957.00,57081.00,61111.00,67938.00,66029.00,83088.00,81363.00,93940.00,91738.00,98273.00,101302.00,113812.00,109431.00,105582.00,116969.00,112635.00,122391.00,121872.00]))
    a.training()
    print(a.predict(11.0))
    print(a.r_squared())
