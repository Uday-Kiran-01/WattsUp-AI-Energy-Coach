# src/utils/plot_utils.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_consumption(df, title="Daily kWh Consumption"):
    plt.figure(figsize=(12,5))
    sns.lineplot(x='datetime', y='kWh', data=df)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("kWh")
    plt.show()