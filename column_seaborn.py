# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

#日本語表示のためのフォント指定
sns.set_style("white", {'font.family':[u'AppleGothic']})

#グラフの右と上の枠を削除
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().yaxis.set_ticks_position('left')
plt.gca().xaxis.set_ticks_position('bottom')

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
