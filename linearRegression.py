import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


class IA:
    def __init__(self):
        self.regressor = LinearRegression()
        self.scaler_X = StandardScaler()
        self.scaler_Y = StandardScaler()

    def treinar(self, X, Y):
        X = self.scaler_X.fit_transform(X)
        Y = self.scaler_Y.fit_transform(Y)
        self.regressor.fit(X, Y)

    def prever(self, X):
        X = self.scaler_X.transform(X)
        Y = self.regressor.predict(X)
        Y = self.scaler_Y.inverse_transform(Y)
        return Y


class Grafico:
    def __init__(self, X, Y, Z, pontos):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlabel('Nota dos alunos aprovados')
        self.ax.set_ylabel('Número de pesquisas no Google')
        self.ax.set_title('Probabilidade de aprovação')
        self.ax.grid(True)
        self.scatter = self.ax.scatter(pontos[:,0], pontos[:,1], color='red')
        self.contorno = self.ax.contourf(X, Y, Z, cmap='coolwarm')

    def plotar(self):
        self.fig.colorbar(self.contorno)
        plt.show()


# dados de treinamento
nota_aprovados = np.array([7, 8, 9, 6, 8.5, 7.5, 8.2, 7.8, 8.6, 9.2, 6.8, 7.2, 7.5, 8.8, 8.3, 9.5, 9, 8.7, 8.1]).reshape(-1, 1)
num_pesquisas = np.array([1000, 1200, 1500, 800, 1100, 900, 1000, 950, 1300, 1400, 750, 800, 850, 1150, 1050, 1600, 1550, 1450, 1250]).reshape(-1, 1)
media_aprovados = nota_aprovados.mean()

# treinamento do modelo
modelo = IA()
modelo.treinar(nota_aprovados, num_pesquisas)

# dados de entrada
nota_entrada = 8.2
num_pesquisas_entrada = 1100
dados_entrada = np.array([[nota_entrada, num_pesquisas_entrada]])

# previsão da probabilidade de aprovação
previsao = modelo.prever(dados_entrada)
probabilidade = previsao / num_pesquisas_entrada
probabilidade_normalizada = probabilidade / probabilidade.sum() * 100

# criação do gráfico
x_min, x_max = nota_aprovados.min() - 1, nota_aprovados.max() + 1
y_min, y_max = num_pesquisas.min() - 100, num_pesquisas.max() + 100
X, Y = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
coordenadas = np.vstack([X.ravel(), Y.ravel()])
Z = np.reshape(probabilidade_normalizada, X.shape)

# plotagem do gradiente
fig, ax = plt.subplots()
ax.set_xlabel('Média das notas dos alunos aprovados')
ax.set_ylabel('Número de pesquisas no Google')
ax.set_title('Probabilidade de aprovação')
ax.grid(True)
contorno = ax.contourf(X, Y, Z, cmap='coolwarm')
fig.colorbar(contorno)

# plotagem do scatter plot
pontos = np.hstack([nota_aprovados, num_pesquisas])
grafico = Grafico(X, Y, Z, pontos)
grafico.plotar()
