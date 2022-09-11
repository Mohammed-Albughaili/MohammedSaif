import numpy as np
import pandas as pd




df = pd.DataFrame(np.random.randn(4,6), index=["nub1","nub2","nub3","nub4"], columns=["col1","col2","col3","col4","col5","col6"])

print(df)

df.to_excel("NewFile.xlsx")
df.to_csv("NewFile.csv")

#df = pd.read_excel("NewFile.xlsx")
#df = pd.csv("NewFile.csv")

df1 = pd.read_excel("NewFile.xlsx", sheet_name=None)
print(df1)
