import numpy as np
import matplotlib.pyplot as plt


def create_basic_plots():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(15, 10))

    plt.subplot(2, 3, 1)
    plt.plot(x, y)
    plt.title("Line Plot")

    plt.subplot(2, 3, 2)
    xs = np.random.rand(50) * 10
    ys = 2 * xs + np.random.randn(50) * 2
    plt.scatter(xs, ys, alpha=0.6)
    plt.title("Scatter Plot")

    plt.subplot(2, 3, 3)
    data = np.random.normal(100, 15, 1000)
    plt.hist(data, bins=30, edgecolor="black")
    plt.title("Histogram")

    plt.subplot(2, 3, 4)
    plt.bar(["A", "B", "C", "D"], [23, 45, 56, 78])
    plt.title("Bar Plot")

    plt.subplot(2, 3, 5)
    groups = [
        np.random.normal(100, 10, 100),
        np.random.normal(110, 15, 100),
        np.random.normal(120, 12, 100),
    ]
    plt.boxplot(groups)
    plt.title("Box Plot")

    plt.subplot(2, 3, 6)
    plt.pie([30, 25, 20, 25], labels=["A", "B", "C", "D"], autopct="%1.1f%%")
    plt.title("Pie Chart")

    plt.tight_layout()
    plt.savefig("figures/day2_basic_plots.png", dpi=300)
