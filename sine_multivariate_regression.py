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
w0, w1, w2 = np.random.rand(3) 
# w0 = 0
# w1 = 0
# w2 = 0
alpha = 0.001
# cost = np.sum(w0 + w1*np.sin(x) - y, axis=0)/(2*m)

for epochs in range(50000):
    cost = np.sum(w0 + w1*x + w2*x*x - y, axis=0)/(2*m)
    # print('cost: ', cost)
    w0 = w0 - np.sum(w0 + w1*x + w2*x*x - y, axis=0)*(alpha/m)
    w1 = w1 - np.sum((w0 + w1*x + w2*x*x - y)*x, axis=0)*(alpha/m)
    w2 = w2 - np.sum((w0 + w1*x + w2*x*x - y)*x*x, axis=0)*(alpha/m)

y_hat = w0 + w1*x + w2*x*x
plt.plot(x, y_hat)


# gradient in vectorization form
x0 = np.ones((m,1))
x = np.expand_dims(x, axis=1)
y = np.expand_dims(y, axis=1)
x_new = np.hstack((x0, x, x*x))
w = np.array([[0], [0], [0]])
print(x0.shape, x.shape, x_new.shape, y.shape)
for epochs in range(50000):
    # w = np.random.rand(2,1)
    cost_gradient = np.dot((np.dot(x_new, w)-y).T, x_new)
    w = w - cost_gradient.T*alpha/(m)
y_new_hat = np.dot(x_new, w)
plt.plot(x, y_new_hat)
plt.show()
print(w0, w1, w2)
print(w)