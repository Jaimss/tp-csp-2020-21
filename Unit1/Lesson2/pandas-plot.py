import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv")
pd.set_option("display.max.columns", None)

plt.plot(data["Rank"], data[["P25th", "Median", "P75th"]])
plt.show()
