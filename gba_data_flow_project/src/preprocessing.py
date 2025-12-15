import pandas as pd
from sklearn.preprocessing import StandardScaler


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    缺失值处理 + 标准化（无 dtype warning 版本）
    """
    df_clean = df.copy()

    # 明确数值列
    numeric_cols = df_clean.columns[2:]

    # 关键：先统一转为 float
    df_clean[numeric_cols] = (
        df_clean[numeric_cols]
        .apply(pd.to_numeric, errors="coerce")
        .astype(float)
    )

    # 缺失值填充
    df_clean[numeric_cols] = df_clean[numeric_cols].fillna(
        df_clean[numeric_cols].mean()
    )

    # 标准化
    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(df_clean[numeric_cols])

    # 用 DataFrame 接住，再整体替换（避免 dtype 冲突）
    df_clean[numeric_cols] = pd.DataFrame(
        scaled_values,
        columns=numeric_cols,
        index=df_clean.index
    )

    return df_clean
