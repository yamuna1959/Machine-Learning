import matplotlib.pyplot as plt
from numpy import True_, true_divide
x=[1,2,3,4,5,6,7,8,9,10]
y=[1,4,9,16,25,36,49,64,81,100]
plt.hist(x,y,ec="red",density=True)
plt.show()