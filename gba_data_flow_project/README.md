# 粤港澳大湾区数据要素流动多元统计分析（前六章）

## 一、项目简介

本项目基于粤港澳大湾区城市层面数据，运用多元统计分析方法，
对区域数据要素流动的特征及其影响因素进行实证研究。

根据课程任务要求，本项目：
- 完成完整的数据处理与分析流程
- 综合报告部分仅完成前六章内容
- 所有实证分析均使用 Python 实现

---

## 二、研究内容对应关系

| 内容 | 对应章节 |
|---|---|
| 数据读取与指标筛选 | 第四章 |
| 数据预处理 | 第四章 |
| 描述性统计与相关性分析 | 第五章 |
| 主成分分析与因子分析 | 第六章 |

---

## 三、项目结构

gba_data_flow_project/
├── data/
│ ├── raw/ # 原始数据
│ └── processed/ # 筛选后的数据
├── src/ # 核心分析代码
├── notebooks/ # 分析流程 Notebook
├── outputs/
│ ├── figures/ # 论文用图
│ └── tables/ # 结果表
└── README.md
---

## 四、运行环境

- Python 3.9+
- pandas
- numpy
- scikit-learn
- factor-analyzer
- matplotlib
- seaborn

安装依赖：

```bash
pip install -r requirements.txt