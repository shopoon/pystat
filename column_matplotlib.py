# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

#日本語表示のためのフォント指定
mpl.rcParams["font.family"] = "AppleGothic"

class Column:
    def show(self, path):
        data = pd.read_csv(path, encoding="ShiftJIS")
        data_statistics = data.describe()
        bar = plt.bar(range(3),
              data_statistics.loc["mean", ["HP", "こうげき", "ぼうぎょ"]],
              yerr=data_statistics.loc["std", ["HP", "こうげき", "ぼうぎょ"]],
              tick_label=["HP", u"こうげき", u"ぼうぎょ"]
              )
        plt.show(bar)

if __name__ == "__main__":
    test = Column()
    test.show("pokemon_status.csv")
