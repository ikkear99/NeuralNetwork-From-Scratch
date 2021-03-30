from builtins import set, print

import numpy as np

class MLP:
    def __init__(self, num_input = 3, num_hidden = [3,5], num_output = 2):
        self.num_input = num_input
        self.num_hidden = num_hidden
        self.num_output = num_output
        layers = [self.num_input] + self.num_hidden + [self.num_output]

        self.weights = []
        for i in range(len(layers) - 1):
            w = np.random.rand(layers[i], layers[i+1])
            self.weights.append(w)

    # Lan truyen ve phia truoc
    def forward_propagate(self, inputs):
        activations = inputs
        for w in self.weights:
            # Tinh next input
            net_inputs = np.dot(activations, w)

            # Tinh toan activations
            activations = self._Sigmoid(net_inputs)
        return activations

    # Sigmoid function
    def _Sigmoid(self, x):
        return 1/(1+np.exp(-x))

if __name__ == '__main__':

    # Khoi tao
    mlp = MLP()

    # Khoi tao input
    inputs = np.random.rand(mlp.num_input)

    # Tinh toan output
    outputs = mlp.forward_propagate(inputs)

    # Ket qua
    print("Output = ", format(inputs))
    print("Output = ", format(outputs))