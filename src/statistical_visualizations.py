import matplotlib.pyplot as plt
import numpy as np


def compare_distributions(group1, group2, x, y, correlation):
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.hist(group1, alpha=0.5)
    plt.hist(group2, alpha=0.5)
    plt.title("Distribution Comparison")

    plt.subplot(1, 3, 2)
    plt.boxplot([group1, group2])
    plt.title("Box Plot Comparison")

    plt.subplot(1, 3, 3)
    plt.scatter(x, y)
    z = np.polyfit(x, y, 1)
    plt.plot(x, np.poly1d(z)(x), "r--")
    plt.title(f"Correlation (r={correlation:.2f})")

    plt.tight_layout()
    plt.savefig("figures/day2_statistical_plots.png", dpi=300)
