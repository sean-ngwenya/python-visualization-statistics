import numpy as np
from src.basic_plots import create_basic_plots
from src.inferential_statistics import t_test, correlation_test
from src.pandas_statistics import pandas_group_analysis


def main():
    np.random.seed(42)

    group1 = np.random.normal(75, 10, 30)
    group2 = np.random.normal(80, 10, 30)

    create_basic_plots()

    t_stat, p_val = t_test(group1, group2)
    print("T-test:", t_stat, p_val)

    summary = pandas_group_analysis(group1, group2)
    print(summary)


if __name__ == "__main__":
    main()
