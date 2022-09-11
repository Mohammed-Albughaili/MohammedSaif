import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.randn(4,6), index = ["size1", "size2", "size3", "size4"], columns = ["p1", "p2", "p3", "p4", "p5", "p6"])
print(df)
print(df.sort_values(by="p1"))
print(df.sort_values(by="p2"))
print(df.sort_values(by="p3"))
print(df.sort_values(by="p4"))
print(df.sort_values(by="p5"))
print(df.sort_values(by="p6"))

x = list(range(4))
y = df.loc[:, "p1"]
plt.title("scatter_example")
plt.scatter(x, y)
plt.show()
plt.savefig("scatter_example")
