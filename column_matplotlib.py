# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("./pokemon_status.csv", encoding="ShiftJIS")
data_statistics = data.describe()
bar = plt.bar(range(3),
              data_statistics.loc["mean", ["HP", "こうげき", "ぼうぎょ"]],
              yerr=data_statistics.loc["std", ["HP", "こうげき", "ぼうぎょ"]],
              tick_label=["HP", u"こうげき", u"ぼうぎょ"]
              )
plt.show(bar)
