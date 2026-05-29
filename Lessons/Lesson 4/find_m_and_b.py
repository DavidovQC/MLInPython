
import matplotlib.pyplot as plt
import time

data = [
    [650, 158000],
    [700, 149000],
    [750, 171000],
    [800, 182000],
    [850, 176000],
    [900, 205000],
    [950, 198000],
    [1000, 225000],
    [1050, 214000],
    [1100, 247000],
    [1150, 238000],
    [1200, 271000],
    [1250, 259000],
    [1300, 291000],
    [1350, 278000],
    [1400, 315000],
    [1450, 301000],
    [1500, 336000],
    [1550, 322000],
    [1600, 358000],
    [1650, 341000],
    [1700, 381000],
    [1750, 366000],
    [1800, 402000],
    [1850, 389000],
    [1900, 431000],
    [1950, 417000],
    [2000, 455000],
    [2100, 472000],
    [2200, 515000]
]

x_mean = sum(d[0] for d in data) / len(data)
data_norm = [[xi - x_mean, yi] for xi, yi in data]

# Target:
# Slope: 223.76518911518056
# Intercept: -6695.960978949194

learning_rate = 1e-8
vec = [0, 0]


def derivative(f, x, h=1e-4):
    return (f(x + h) - f(x)) / h


def gradient(f, point, h=1e-4):
    grad = []

    for i in range(len(point)):
        shifted = point.copy()
        shifted[i] += h

        partial = (f(shifted) - f(point)) / h
        grad.append(partial)

    return grad


def compute_error(vec):
    error = 0
    m = vec[0]
    b = vec[1]
    for xi, yi in data:
        error += ((m * xi + b) - yi)**2
    return error


# start w/  range(100000000), see how many orders of magnitude you are off, and add them
# epochs = 100000000
# for step in range(epochs):
#     grad = gradient(compute_error, vec)

#     for i in range(len(vec)):

#         dE_dxi = grad[i]
#         vec[i] -= learning_rate * dE_dxi
#         error = compute_error(vec)
#         if step % 123456 == 0:
#             print()
#             print("Vector:", vec)
#             print("dE_dxi", dE_dxi)
#             print("Error", error)
#             print((step * 100)/epochs, "%")  # percent


epochs = 100000000
start_time = time.time()

for step in range(epochs):
    grad = gradient(compute_error, vec)

    for i in range(len(vec)):

        dE_dxi = grad[i]
        vec[i] -= learning_rate * dE_dxi

    error = compute_error(vec)

    if step % 123456 == 0 and step > 0:

        elapsed = time.time() - start_time
        progress = step / epochs

        estimated_total = elapsed / progress
        remaining = estimated_total - elapsed

        hours = int(remaining // 3600)
        minutes = int((remaining % 3600) // 60)
        seconds = int(remaining % 60)

        print()
        print("Vector:", vec)
        print("dE_dxi", dE_dxi)
        print("Error", error)
        print(progress * 100, "%")
        print(f"Time remaining: {hours}h {minutes}m {seconds}s")

print(vec)

test_model

# print(vec)
# train instead on a subset of the data, then try the model on missing elements
