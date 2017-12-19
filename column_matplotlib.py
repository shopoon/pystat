# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

#日本語表示のためのフォント指定
mpl.rcParams["font.family"] = "AppleGothic"

class Column:
    def __init__(self, path):
        self.data = pd.read_csv(path, encoding="ShiftJIS")
    def make_column(self):
        data_statistics = self.data.describe()
        bar = plt.bar(range(3),
              data_statistics.loc["mean", ["HP", "こうげき", "ぼうぎょ"]],
              yerr=data_statistics.loc["std", ["HP", "こうげき", "ぼうぎょ"]],
              tick_label=["HP", u"こうげき", u"ぼうぎょ"]
              )
        return bar

if __name__ == "__main__":
    test = Column("pokemon_status.csv")
    graph = test.make_column()
    plt.show(graph)
