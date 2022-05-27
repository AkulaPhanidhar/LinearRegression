from turtle import color
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("SampleData.csv")

def Los_function(m, b, points):
    total_error = 0

    for i in range(len(points)):
        x = points.iloc[i].Time
        y = points.iloc[i].Score
        total_error += (y - (m * x + b)) ** 2

    total_error / len(points)
    return total_error

def Gradient(m_now, b_now, points, lr):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].Time
        y = points.iloc[i].Score
        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - m_gradient * lr
    b = b_now - b_gradient * lr
    return m, b

m = 0
b = 0
lr = 0.001
epochs = 1000

for i in range(epochs):
    m, b = Gradient(m, b, data, lr)

error = Los_function(m, b, data)

print(f"[Error = {error}, m = {m}, b = {b}]")
plt.scatter(data.Time, data.Score, color="blue")
plt.plot(list(range(0, 11)), [m * x + b for x in range(0, 11)],color="red")
plt.show
