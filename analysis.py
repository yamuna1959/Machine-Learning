from operator import index
from tkinter import Y
import numpy as np
import pandas as pd
data=pd.read_excel('price.xlsx',index_col=None,na_values=['NA'],usecols="B,E")
df=pd.DataFrame(data)
print(df)
x=np.array(df['OPEN']).reshape(-1,1)
y=np.array(df['CLOSE']).reshape(-1,1)
df.dropna(inplace=True)
print(x)
print(y)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()