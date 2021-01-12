import pandas as pd
df = pd.read_csv("symbollink.csv")
matrix2 = df[df.columns[0]].to_numpy()
list1 = matrix2.tolist()
print(list1)
