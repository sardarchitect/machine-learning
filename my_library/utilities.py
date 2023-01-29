import numpy as np
import matplotlib.pyplot as plt

def normalize(a):
    norm = [((i)-min(a))/(max(a)-min(a)) for i in a]
    return norm

def sigmoid(x):
    return 1/(1+np.exp(-1*x))

def gaussian(x, mu, sigma):
    return np.exp(-1*((x - mu)**2 /(2*sigma**2)))/(sigma*np.sqrt(2*np.pi))

def pdf(data, decimals):
    data_binned = sorted(data.round(decimals))
    data_dict = {}
    for i in data_binned:
        if i in data_dict:
            data_dict.update({i:data_dict[i]+1})
            continue
        else:
            data_dict.update({i:1})
    return data_dict