
import matplotlib.pyplot as plt
#   Today we will implement linear regression on some data
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


learning_rate = 1e-9
m = 0


def derivative(f, x, h=1e-4):
    return (f(x + h) - f(x)) / h


def gradient(f, point, h=1e-5):
    grad = []

    for i in range(len(point)):
        shifted = point.copy()
        shifted[i] += h

        partial = (f(shifted) - f(point)) / h
        grad.append(partial)

    return grad


def compute_error(m):
    error = 0
    for pt in data:
        error += ((m * pt[0]) - pt[1])**2
    return error


for i in range(10000):
    dE_dm = derivative(compute_error, m)
    m -= learning_rate * dE_dm
    error = compute_error(data, m)

    print()
    print("dE_dm", dE_dm)
    print("Slope", m)
    print("Current error", error)

    if dE_dm == 0:
        print("Steps:", i)
        break


# Plot line

x = []
y = []

for pt in data:
    x.append(pt[0])
    y.append(pt[1])


def find_best_fit_slope(data):
    sumXY = 0
    sumX2 = 0
    for x, y in data:
        sumXY += x*y
        sumX2 += x**2

    return sumXY / sumX2


print("True best fit slope is", find_best_fit_slope(data))

plt.scatter(x, y)

plt.xlabel("Square Feet")
plt.ylabel("Price")
plt.title("House Prices vs Square Footage")

# Domain of the line:
x_line = [min(x), max(x)]
# Range:
y_line = [m * x for x in x_line]

plt.plot(x_line, y_line, color='red')

plt.show()
