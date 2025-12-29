import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def pandas_group_analysis(group1, group2):
    df = pd.DataFrame(
        {
            "Group": ["A"] * len(group1) + ["B"] * len(group2),
            "Score": list(group1) + list(group2),
        }
    )

    summary = df.groupby("Group")["Score"].describe()

    plt.figure(figsize=(12, 4))
    sns.violinplot(data=df, x="Group", y="Score")
    plt.savefig("figures/day2_seaborn_plots.png", dpi=300)

    return summary
