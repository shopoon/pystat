# 環境構築

必要なライブラリはrequirements.yamlに保存する
https://qiita.com/yubessy/items/2dd43551aa8308dc7eca

## 環境設定の書き出し方法
~~~bash
$ conda env export > requirements.yaml
~~~

## Requirements.yamlを用いた環境設定方法
~~~bash
$ conda env create --file requirements.yaml
~~~

# 現状
## 今できること
wx_main.pyをrun --> メニューバーの「開く」をクリック --> csvファイルをファイルダイアログから選択 --> そのファイルの中身を表とグラフとして別々に表示

## 課題
1. 表とグラフのウィンドウを紐付けする（片方閉じたらもう片方も閉じる、みたいな）
2. 表で値を変更したら、グラフにもそれが反映するようにする
3. 保存できるようにする
4. 他の形式（カラム、2群グラフなど）
