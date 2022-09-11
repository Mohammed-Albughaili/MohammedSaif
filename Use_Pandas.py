import numpy as np
import pandas as pd




df = pd.DataFrame(np.random.randn(4,6), index=["nub1","nub2","nub3","nub4"], columns=["col1","col2","col3","col4","col5","col6"])

print(df)

df2 = df.sort_values(by = "col5")
df3 = df.sort_values(by = "col3")
df4 = df.sort_values(by = "col2")
df5 = df.sort_values(by = "col6")
df6 = df.sort_values(by = "col1")
df7 = df.sort_values(by = "col4")

print(df7.describe())
print(df2.describe())
