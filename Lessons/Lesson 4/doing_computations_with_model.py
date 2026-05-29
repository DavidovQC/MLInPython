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

# Output for this code: Final vector: [221.24212331121177, -2858.1128331732125]
# the max error is: 21191.390630326234

# our m and b computed by the model (at 10000000 steps)
vec = [221.24212331121177, -2858.1128331732125]


def create_full_model(data, vec):
    m = vec[0]
    b = vec[1]

    model = []

    for xi, yi in data:
        model.append([xi, m * xi + b])

    return model


def model(sqft):
    m = vec[0]
    b = vec[1]

    return m * sqft + b


for (xi, yi) in create_full_model(data, vec):
    print(xi, yi)

print(model(1411))

# Aayush asked a great question, how are AI's so fast?
# Generally, it takes a long time (and a LOT of energy) to train an AI model.
