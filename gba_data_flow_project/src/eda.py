import pandas as pd


def descriptive_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    描述性统计（不涉及任何绘图）
    """
    return df.describe().T
