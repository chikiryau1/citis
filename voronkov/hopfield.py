import math
import numpy as np


class Hopfield:
    def __init__(self, weights, vector):
        self.result = normalize(vector)
        self.weights = normalize(weights)
        self.error = 0
        self.energy = 0
        self.vector = vector

    def train(self):
        v = normalize(np.dot(self.weights, self.vector))
        self.error = error_value(v, self.vector)
        # self.energy = energy(self.weights, v)
        # print(self.error, self.energy)
        if self.error < 0.00001:

        # if self.energy < 0.00001:

            self.result = v
        else:
            self.vector = v
            self.train()
        

def normalize(vector):
    return np.dot(vector, 1 / np.linalg.norm(vector))


def error_value(vector1, vector2):
    distance = 0
    for i in range(len(vector1)):
        distance += (vector1[i] - vector2[i])**2
    
    return math.sqrt(distance)


def energy(weights, vector):
    sum = 0

    for i in range(weights.shape[0]):
        for j in range(weights.shape[1]):
            # print(vector[i], vector[j])
            sum += weights[i][j] * vector[i] * vector[j]

    return 0.5 * sum
