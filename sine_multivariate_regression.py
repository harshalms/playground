import  numpy as np 
import matplotlib.pyplot as plt 
# Data generation
x = np.arange(0, 10, 0.1)
y = np.sin(x) + np.random.normal(-1,0.1,100)
m = len(y)
print(m)
# Plotiing the data
plt.scatter(x, y)
# plt.show()
# weight initialization 
w0 = 0
w1 = 0
w2 = 0
alpha = 0.001
# cost = np.sum(w0 + w1*np.sin(x) - y, axis=0)/(2*m)

for epochs in range(10000):
    cost = np.sum(w0 + w1*x + w2*x*x - y, axis=0)/(2*m)
    print('cost: ', cost)
    w0 = w0 - np.sum(w0 + w1*x + w2*x*x - y, axis=0)*(alpha/m)
    w1 = w1 - np.sum((w0 + w1*x + w2*x*x - y)*x, axis=0)*(alpha/m)
    w2 = w2 - np.sum((w0 + w1*x + w2*x*x - y)*x*x, axis=0)*(alpha/m)

y_hat = w0 + w1*x + w2*x*x
plt.plot(x, y_hat)
plt.show()
print(w0, w1, w2)