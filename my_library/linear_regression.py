import numpy as np

def MSELoss(Y, Y_pred):
    return Y - Y_pred

X = np.array([[1],[2],[3],[4]])
Y = np.array([[3], [5], [7], [9]])

class LinearRegression():
    def __init__(self):
        print("Linear Regression Model Initialized")
        self.beta1 = 0
        self.beta2 = 0

    def fit_stats(self, X, Y):
        self.beta1 = (np.sum((X - np.mean(X))*(Y - np.mean(Y))))
        self.beta1 /= (np.sum((X - np.mean(X))**2))
        self.beta2 = np.mean(Y) - (self.beta1 * np.mean(X))
        print("Beta1:", self.beta1)
        print("Beta2:", self.beta2)

    def fit_grad(self, X, Y, lr=0.001, epochs=10000):
        n = float(len(X))
        for _ in range(epochs):
            Y_pred = self.predict(X)
            d_beta1 = (-2/n) * np.sum(X * (Y - Y_pred)) 
            d_beta2 = (-2/n) * np.sum(Y - Y_pred)
            self.beta1 -= lr * d_beta1
            self.beta2 -= lr * d_beta2
        print("Beta1:", self.beta1)
        print("Beta2:", self.beta2)

    def predict(self, X):
        return np.dot(np.transpose(self.beta1), X) + self.beta2

stats_model = LinearRegression()
stats_model.fit_stats(X, Y)
print(stats_model.predict(50))

grad_model = LinearRegression()
grad_model.fit_grad(X, Y)
print(grad_model.predict(50))