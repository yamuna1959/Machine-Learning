from turtle import pd
import numpy as np
import pandas as pd
df=pd.read_csv('irisflower.csv',header=0)
print(df.head())
print(df.shape)
print(df[10:21])
print(df[["variety","sepal.length"]])
p=df.loc[df["variety"]=="Setosa"]
print(p)