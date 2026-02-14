import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("heights.csv")

height = np.array(data["height(cm)"])
print(height)

# print("Mean of heights =", height.mean())
# print("Standard Deviation of heights =", height.std())
# print("Minimum height =", height.min())
# print("Maximum height =", height.max())

# print("25th percentile =", np.percentile(height, 25))
# print("Median (50th percentile) =", np.percentile(height, 50))
# print("75th percentile =", np.percentile(height, 75))

sns.set_style("whitegrid")
plt.hist(height)
plt.title("Hiehgt Distribution of Presidents of USA")
plt.xlabel("Height (cm)")
plt.ylabel("Number")
plt.show()