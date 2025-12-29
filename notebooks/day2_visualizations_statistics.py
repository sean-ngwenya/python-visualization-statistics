"""
Day 2: Visualization & Statistics
Connecting SPSS knowledge to Python
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set style
sns.set_style("whitegrid")

print("=" * 70)
print(" VISUALIZATION & STATISTICS")
print("=" * 70)

# ============================================================================
# 1. BASIC PLOTS (30 min)
# ============================================================================
print("\n1. CREATING BASIC PLOTS")
print("-" * 70)

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X")
plt.ylabel("Sin(X)")
plt.grid(True)

# Scatter plot
plt.subplot(2, 3, 2)
x_scatter = np.random.rand(50) * 10
y_scatter = 2 * x_scatter + np.random.randn(50) * 2
plt.scatter(x_scatter, y_scatter, alpha=0.6)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")

# Histogram
plt.subplot(2, 3, 3)
data = np.random.normal(100, 15, 1000)
plt.hist(data, bins=30, edgecolor="black")
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Bar plot
plt.subplot(2, 3, 4)
categories = ["A", "B", "C", "D"]
values = [23, 45, 56, 78]
plt.bar(categories, values, color=["red", "blue", "green", "orange"])
plt.title("Bar Plot")
plt.xlabel("Category")
plt.ylabel("Value")

# Box plot
plt.subplot(2, 3, 5)
data_groups = [
    np.random.normal(100, 10, 100),
    np.random.normal(110, 15, 100),
    np.random.normal(120, 12, 100),
]
plt.boxplot(data_groups, labels=["Group 1", "Group 2", "Group 3"])
plt.title("Box Plot")
plt.ylabel("Value")

# Pie chart
plt.subplot(2, 3, 6)
sizes = [30, 25, 20, 25]
labels = ["Category A", "Category B", "Category C", "Category D"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart")

plt.tight_layout()
plt.savefig("day2_basic_plots.png", dpi=300)
print("✅ Saved: day2_basic_plots.png")

# ============================================================================
# 2. STATISTICS IN PYTHON (Like SPSS!) (45 min)
# ============================================================================
print("\n2. STATISTICS (Connecting to SPSS knowledge)")
print("-" * 70)

# Generate sample data
np.random.seed(42)
group1 = np.random.normal(75, 10, 30)  # Mean=75, SD=10
group2 = np.random.normal(80, 10, 30)  # Mean=80, SD=10

# Descriptive statistics
print("\nDESCRIPTIVE STATISTICS")
print("-" * 40)
print(f"Group 1: Mean={np.mean(group1):.2f}, SD={np.std(group1, ddof=1):.2f}")
print(f"Group 2: Mean={np.mean(group2):.2f}, SD={np.std(group2, ddof=1):.2f}")

# T-test (comparing two groups)
print("\nT-TEST (Independent samples)")
print("-" * 40)
t_stat, p_value = stats.ttest_ind(group1, group2)
print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
if p_value < 0.05:
    print("Result: Significant difference (p < 0.05)")
else:
    print("Result: No significant difference (p >= 0.05)")

# Chi-square test
print("\nCHI-SQUARE TEST")
print("-" * 40)
# Example: Preference by gender
observed = np.array(
    [
        [20, 30],  # Male: Prefer A, Prefer B
        [25, 25],
    ]
)  # Female: Prefer A, Prefer B

chi2, p_val, dof, expected = stats.chi2_contingency(observed)
print(f"Chi-square: {chi2:.4f}")
print(f"p-value: {p_val:.4f}")
print(f"Degrees of freedom: {dof}")
print(f"Expected frequencies:\n{expected}")

# Correlation
print("\nCORRELATION")
print("-" * 40)
x = np.random.rand(100) * 10
y = 2 * x + np.random.randn(100) * 3  # y correlates with x

correlation, p_val = stats.pearsonr(x, y)
print(f"Pearson correlation: {correlation:.4f}")
print(f"p-value: {p_val:.4f}")

# Normal distribution test
print("\nNORMALITY TEST (Shapiro-Wilk)")
print("-" * 40)
normal_data = np.random.normal(0, 1, 100)
stat, p_val = stats.shapiro(normal_data)
print(f"Test statistic: {stat:.4f}")
print(f"p-value: {p_val:.4f}")
if p_val > 0.05:
    print("Data appears normally distributed")
else:
    print("Data may not be normally distributed")

# ============================================================================
# 3. VISUALIZING STATISTICS (30 min)
# ============================================================================
print("\n3. STATISTICAL VISUALIZATIONS")
print("-" * 70)

plt.figure(figsize=(15, 5))

# Distribution comparison
plt.subplot(1, 3, 1)
plt.hist(group1, bins=15, alpha=0.5, label="Group 1", edgecolor="black")
plt.hist(group2, bins=15, alpha=0.5, label="Group 2", edgecolor="black")
plt.title("Distribution Comparison")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()

# Box plot comparison
plt.subplot(1, 3, 2)
plt.boxplot([group1, group2], labels=["Group 1", "Group 2"])
plt.title("Box Plot Comparison")
plt.ylabel("Value")

# Correlation scatter
plt.subplot(1, 3, 3)
plt.scatter(x, y, alpha=0.6)
plt.title(f"Correlation (r={correlation:.3f})")
plt.xlabel("X")
plt.ylabel("Y")
# Add trend line
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--", alpha=0.8, label="Trend line")
plt.legend()

plt.tight_layout()
plt.savefig("day2_statistical_plots.png", dpi=300)
print("\n✅ Saved: day2_statistical_plots.png")

# ============================================================================
# 4. PANDAS + STATISTICS (15 min)
# ============================================================================
print("\n4. PANDAS WITH STATISTICS")
print("-" * 70)

# Create DataFrame
df = pd.DataFrame(
    {"Group": ["A"] * 30 + ["B"] * 30, "Score": np.concatenate([group1, group2])}
)

print("\nDataFrame summary by group:")
print(df.groupby("Group")["Score"].describe())

# Seaborn for advanced visualization
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
sns.violinplot(data=df, x="Group", y="Score")
plt.title("Violin Plot")

plt.subplot(1, 3, 2)
sns.boxplot(data=df, x="Group", y="Score")
plt.title("Box Plot")

plt.subplot(1, 3, 3)
sns.stripplot(data=df, x="Group", y="Score", alpha=0.5)
plt.title("Strip Plot")

plt.tight_layout()
plt.savefig("day2_seaborn_plots.png", dpi=300)
print("✅ Saved: day2_seaborn_plots.png")

plt.show()  # Display all plots

print("\n" + "=" * 70)
print(" ✅ VISUALIZATION & STATISTICS COMPLETE!")
print("=" * 70)
print("\nKey Takeaways:")
print("  • NumPy = Arrays & matrices (like SPSS data)")
print("  • Pandas = DataFrames (like SPSS spreadsheets)")
print("  • Matplotlib = Plots (like SPSS charts)")
print("  • SciPy.stats = Statistical tests (like SPSS analyze)")
print("\nYou now have Python equivalents for SPSS operations!")
