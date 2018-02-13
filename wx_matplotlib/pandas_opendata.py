import pandas as pd

class Opendata:
    def __init__(self, path):
        self.table = pd.read_csv(path, encoding="ShiftJIS", header=None)


if __name__ == "__main__":
    test = Opendata("test.csv")
    for r in range (3):
        for c in range(4):
            print(test.table.iloc[r, c])