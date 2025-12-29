from scipy import stats
import numpy as np


def t_test(group1, group2):
    return stats.ttest_ind(group1, group2)


def chi_square_test():
    observed = np.array([[20, 30], [25, 25]])
    return stats.chi2_contingency(observed)


def correlation_test(x, y):
    return stats.pearsonr(x, y)


def normality_test(data):
    return stats.shapiro(data)
