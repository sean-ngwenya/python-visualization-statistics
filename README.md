# Python Visualization & Statistics

## Overview

This repository demonstrates how **statistical analysis and data visualization concepts traditionally performed in SPSS** can be implemented using **Python**.

It focuses on:
- Visualizing data using Matplotlib and Seaborn
- Performing statistical tests using SciPy
- Connecting classical statistics concepts to Python-based workflows
- Integrating NumPy and Pandas with statistical analysis

The project is structured to reflect **real analytical workflows**, not isolated plotting examples.

---

## Learning Objectives

By completing this repository, I demonstrate the ability to:
- Create publication-quality visualizations in Python
- Apply descriptive and inferential statistics programmatically
- Perform hypothesis testing using SciPy
- Visualize statistical results clearly
- Translate SPSS-style analysis into Python code
- Combine NumPy, Pandas, Matplotlib, Seaborn, and SciPy effectively

---

## Repository Structure
```
python-visualization-statistics/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── outputs/
│   ├── day2_basic_plots.png
│   ├── day2_statistical_plots.png
│   └── day2_seaborn_plots.png
│
├── src/
│   ├── __init__.py
│   ├── basic_plots.py
│   ├── descriptive_statistics.py
│   ├── hypothesis_testing.py
│   ├── statistical_visualizations.py
│   └── pandas_statistics.py
│
└── main.py
```

---

## Key Topics Covered

### 1. Data Visualization (Matplotlib & Seaborn)
- Line plots
- Scatter plots
- Histograms
- Bar charts
- Box plots
- Pie charts
- Distribution comparisons
- Correlation plots with trend lines

### 2. Descriptive Statistics
- Mean
- Standard deviation
- Variance
- Distribution inspection

### 3. Inferential Statistics (SciPy)
- Independent samples t-test
- Chi-square test of independence
- Pearson correlation
- Normality testing (Shapiro–Wilk)

### 4. Statistical Visualization
- Distribution comparisons
- Group comparisons
- Correlation visualization
- Violin plots
- Strip plots
- Box plots with Seaborn

### 5. Pandas + Statistics
- Group-based statistical summaries
- Descriptive statistics using `groupby`
- Visualizing grouped data

---

## SPSS → Python Concept Mapping

| SPSS Component           | Python Equivalent            |
|--------------------------|------------------------------|
| Data View                | Pandas DataFrame             |
| Charts                   | Matplotlib / Seaborn         |
| Analyze → Descriptives   | NumPy / Pandas               |
| Analyze → Compare Means  | SciPy `ttest_ind`            |
| Crosstabs                | Pandas + SciPy Chi-square    |
| Correlations             | SciPy `pearsonr`             |

---

## How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/sean-ngwenya/python-visualization-statistics.git
cd python-visualization-statistics
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Project
```bash
python main.py
```

All generated plots will be saved in the `outputs/` directory.

---

## Technologies Used

- Python 3
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy
- Git & GitHub
- Linux (Pop!_OS)
- VS Code

---

## Learning Context

This repository builds on:
- Python Fundamentals
- NumPy (Scientific Computing)
- Pandas (Data Manipulation)

It forms the statistical and visualization foundation required for:
- Data analysis
- Machine learning
- AI model evaluation

---

## License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this code with attribution.

---

## Author

**Sean Craig Ngwena**  
BSc AI & ML Student  
GitHub: [https://github.com/sean-ngwenya](https://github.com/sean-ngwenya)
