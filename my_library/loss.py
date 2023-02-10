import numpy as np

def mae_loss(Y, Y_pred):
    return (np.abs(Y - Y_pred) / len(Y))
