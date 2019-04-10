import pandas as pd
import matplotlib.pyplot as plt
#chunksize = 10 ** 6
ms = pd.read_csv('../train_1m.csv', low_memory=False)#, chunksize = chunksize)
import seaborn as sns
aux = sns.heatmap(ms.isnull(), cbar=False)
plt.show()