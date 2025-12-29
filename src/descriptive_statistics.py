import numpy as np


def descriptive_stats(group1, group2):
    return {
        "group1_mean": np.mean(group1),
        "group1_sd": np.std(group1, ddof=1),
        "group2_mean": np.mean(group2),
        "group2_sd": np.std(group2, ddof=1),
    }
