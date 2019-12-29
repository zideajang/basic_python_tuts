# coding=utf-8
'''

'''
import numpy as np

class SVM:

    def __init__(self, learning_rate=0.001, lambda_param=0.01,n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None