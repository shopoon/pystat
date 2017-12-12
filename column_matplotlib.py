#coding: utf-8
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv("/Users/miyaketakahito/python/pystat/pokemon_status.csv", encoding = "ShiftJIS")
data_statistics = data.describe()
bar = plt.bar(range(3),data_statistics.loc["mean",["HP","こうげき","ぼうぎょ"]], yerr = data_statistics.loc["std",["HP","こうげき","ぼうぎょ"]], tick_label = ["HP",u"こうげき",u"ぼうぎょ"])
plt.show(bar)
