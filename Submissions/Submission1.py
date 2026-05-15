def dotProduct(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same length")

    total = 0

    for i in range(len(v1)):
        total += v1[i] * v2[i]

    return total


class Perceptron:
    def __init__(self, weights, threshold):
        self.length = len(weights)
        self.weights = weights
        self.threshold = threshold

    def predict(self, inputs):
        if len(inputs) != self.length:
            raise ValueError("Incorrect number of inputs")

        value = dotProduct(inputs, self.weights)

        return value >= self.threshold


def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h


def gradient(f, point, h=1e-5):
    grad = []

    for i in range(len(point)):
        shifted = point.copy()
        shifted[i] += h

        partial = (f(shifted) - f(point)) / h
        grad.append(partial)

    return grad


v1 = [1, 2, 3]
v2 = [-4, -5, -6]

print(dotProduct(v1, v2))

p = Perceptron(
    weights=[0.5, -1, 2],
    threshold=1
)

print(p.predict(v2))


def f(x):
    return x ** 2


print(derivative(f, 3, h=1e-11))


def g(vars):
    return vars[0]**2 + vars[1]*vars[2]


point = [1, 2, 3]

print(gradient(g, point))
