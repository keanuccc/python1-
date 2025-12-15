import pandas as pd


def select_core_indicators(input_path: str, output_path: str) -> pd.DataFrame:
    """
    从原始指标数据中筛选用于前六章分析的核心指标
    """
    df = pd.read_csv(input_path)

    selected_columns = [
        "城市",
        "年份",
        "跨境数据传输总量_TB",
        "数据交易额_亿元",
        "GDP_亿元",
        "人均GDP_万元",
        "第三产业占比_%",
        "研发经费投入_亿元",
        "发明专利授权量",
        "高新技术企业数",
        "互联网国际出口带宽_Gbps",
        "算力规模_PFLOPS",
        "5G基站密度_个每平方公里"
    ]

    df_selected = df[selected_columns]
    df_selected.to_csv(output_path, index=False, encoding="utf-8-sig")

    return df_selected
