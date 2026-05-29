
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


def derivative(f, x, h=1e-4):
    return ((f(x+h) - f(x))/h)


def compute_error(m):
    error = 0
    for (xi, yi) in data:
        error += (m * xi - yi)**2
    return error


learning_rate = 1e-9
m = 0

for i in range(300000):
    dE_dm = derivative(compute_error, m)
    m -= learning_rate * dE_dm
    error = compute_error(m)

    if (i % 1e5 == 0):
        print()
        print("dE_dm", dE_dm)
        print("Current slope:", m)
        print("Current error:", error)


def best_fit_slope(data):
    XY = 0
    X2 = 0
    for (xi, yi) in data:
        XY += xi * yi
        X2 += xi * xi

    return XY/X2


print("The best fit slope is:", best_fit_slope(data))
