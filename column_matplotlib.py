# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from filedialog import *

#日本語表示のためのフォント指定
mpl.rcParams["font.family"] = "MS Gothic"

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
              tick_label=["HP", u"攻撃", u"防御"]
              )
        return bar

if __name__ == "__main__":
    selected = selectData()
    test = Column(selected)
    graph = test.make_column()
    plt.show(graph)
