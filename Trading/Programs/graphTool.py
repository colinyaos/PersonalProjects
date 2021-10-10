import matplotlib.pyplot as plt
import pandas as pd

import numpy as np

x = np.linspace(0, 2, 100)

# plt.plot(x, x, label = "linear")


filename = "2760_1_0.1.csv"

df = pd.read_csv(filename)

k = df.Price.plot()

plt.plot(df.Price)
plt.plot(df.EMA)
plt.grid(True)

plt.show()