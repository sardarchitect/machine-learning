import matplotlib.pyplot as plt
import numpy as np

class LinearRegression():
    def __init__(self):
        print("Linear Regression Model Initialized")
        self.beta1 = 0
        self.beta2 = 0

    def fit_stats(self, X, y):
        self.beta1 = (np.sum((X - np.mean(X))*(y - np.mean(y))))
        self.beta1 /= (np.sum((X - np.mean(X))**2))
        self.beta2 = np.mean(y) - (self.beta1 * np.mean(X))
        print("Beta1:", self.beta1)
        print("Beta2:", self.beta2)
        self.plot_scatter(X, y)

    def fit_grad(self, X, y, lr=0.001, epochs=10000):
        n = float(len(X))
        for _ in range(epochs):
            y_pred = self.predict(X)
            d_beta1 = (-2/n) * np.sum(X * (y - y_pred)) 
            d_beta2 = (-2/n) * np.sum(y - y_pred)
            self.beta1 -= lr * d_beta1
            self.beta2 -= lr * d_beta2
        print("Beta1:", self.beta1)
        print("Beta2:", self.beta2)

    def plot_scatter(self, X, y):
        plt.figure(figsize=(10,8))
        plt.plot(X, self.predict(X))
        plt.scatter(X,y)
        plt.show()

    def predict(self, X):
        return np.dot(np.transpose(self.beta1), X) + self.beta2