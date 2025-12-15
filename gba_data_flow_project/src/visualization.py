import numpy as np
import matplotlib

# 关键：绕开所有 Jupyter / backend 问题
matplotlib.use("Agg")

import matplotlib.pyplot as plt


def correlation_heatmap(df, save_path: str):
    corr = df.iloc[:, 2:].corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    cax = ax.imshow(corr.values)

    ax.set_xticks(np.arange(len(corr.columns)))
    ax.set_yticks(np.arange(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90)
    ax.set_yticklabels(corr.columns)

    for i in range(len(corr.columns)):
        for j in range(len(corr.columns)):
            ax.text(j, i, f"{corr.values[i, j]:.2f}",
                    ha="center", va="center", fontsize=7)

    ax.set_title("指标相关系数矩阵")
    fig.colorbar(cax)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()
