import numpy as np
import loss
import models
import data
import plot

X, y = data.get_sample_data()

# model = models.LinearRegression()
# model.fit_stats(X, y)
# print(model.predict(5))

model = models.LinearRegression()
model.fit_grad(X, y)
print(model.predict(5))