import random
import numpy as np


# Goal: To first create a classifier that determines if a digit is 0


class ZeroDetector:

    def __init__(self):
        self.weights = np.random.randn(784)
        self.bias = np.random.randn()

    def sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-z))

    def predict(self, x):
        z = np.dot(self.weights, x) + self.bias
        return self.sigmoid(z)

    def train_example(self, x, target, learning_rate):

        # forward pass
        z = np.dot(self.weights, x) + self.bias
        a = self.sigmoid(z)

        # chain rule
        delta = 2 * (a - target) * a * (1 - a)
        grad_w = delta * x
        grad_b = delta

        self.weights -= learning_rate * grad_w
        self.bias -= learning_rate * grad_b

        return (a - target) ** 2

    def SGD(self, training_data, epochs, learning_rate):

        for epoch in range(epochs):

            random.shuffle(training_data)

            total_error = 0

            for x, digit in training_data:

                target = 1 if digit == 0 else 0

                total_error += self.train_example(
                    x,
                    target,
                    learning_rate
                )

            print(
                "Epoch:",
                epoch,
                "Error:",
                total_error
            )
