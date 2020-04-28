import  numpy as np 
import matplotlib.pyplot as plt 
# Data generation
x = np.arange(0, 10, 0.1)
y = np.sin(x) + np.random.normal(-1,0.1,100)
print(y.shape)
m = len(y)
print(m)
# Plotiing the data
plt.scatter(x, y)
# plt.show()
# weight initialization 
w0 = 0
w1 = 0
alpha = 0.001
# cost = np.sum(w0 + w1*np.sin(x) - y, axis=0)/(2*m)

for epochs in range(10000):
    cost = np.sum(w0 + w1*x - y, axis=0)/(2*m)
    # print('cost: ', cost)
    w0 = w0 - np.sum(w0 + w1*x - y, axis=0)*(alpha/m)
    w1 = w1 - np.sum((w0 + w1*x-y)*x, axis=0)*(alpha/m)

y_hat = w0 + w1*x
plt.plot(x, y_hat)
plt.show()
print(w0, w1)

# gradient in vectorization form
x0 = np.ones((m,1))
x = np.expand_dims(x, axis=1)
y = np.expand_dims(y, axis=1)
x_new = np.hstack((x0, x))
w = np.array([[0], [0]])
print(x0.shape, x.shape, x_new.shape, y.shape)
for epochs in range(10000):
    # w = np.random.rand(2,1)
    cost_gradient = np.dot((np.dot(x_new, w)-y).T, x_new)
    w = w - cost_gradient.T*alpha/(m)
print(w)