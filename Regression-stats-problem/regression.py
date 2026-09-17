import pandas as pd
import matplotlib.pyplot as plt

# Data
data = {
    "Xi": [24, 35, 64, 20, 33, 27, 42, 41, 22, 50, 36, 31],
    "Yi": [90, 65, 30, 60, 60, 80, 45, 45, 80, 35, 50, 45]
}

df = pd.DataFrame(data)

# Mean
x_mean = df["Xi"].mean()
y_mean = df["Yi"].mean()

# Beta
beta = ((df["Xi"] - x_mean) * (df["Yi"] - y_mean)).sum() / \
       ((df["Xi"] - x_mean) ** 2).sum()

# Alpha
alpha = y_mean - beta * x_mean

print(df)
print("X Mean =", round(x_mean, 2))
print("Y Mean =", round(y_mean, 2))
print("Beta =", round(beta, 2))
print("Alpha =", round(alpha, 2))

# Scatter plot
plt.scatter(df["Xi"], df["Yi"], label="Data Points")

# Regression line
x_line = df["Xi"]
y_line = alpha + beta * x_line

plt.plot(x_line, y_line, label="Regression Line")

# Labels
plt.xlabel("Xi")
plt.ylabel("Yi")
plt.title("Scatter Plot of Xi vs Yi")
plt.legend()
plt.grid(True)

plt.show()