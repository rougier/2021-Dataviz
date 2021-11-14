import numpy as np
data = np.recfromcsv("mar2016.csv", delimiter=';',
                     filling_values=np.nan, case_sensitive=True,
                     deletechars='', encoding=None, replace_space=' ')
D = data["ANAIS1"] - data["ANAIS2"]

import matplotlib.pyplot as plt
plt.hist(D, bins=range(-30,30))

plt.ylim(-1000,30000)

plt.show()
