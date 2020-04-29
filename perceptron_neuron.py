import numpy as np 

x = np.random.rand(100, 2)
# print(x.shape)
y = np.random.randint(0, 2, (100, 1))
# print(y.shape)
m = len(y)
x_new = np.hstack((np.ones((m,1)), x))
# print(x_new.shape)
w = np.random.rand(3, 1)
# print(w.shape)

for epoch in range(100):
    k = np.random.randint(0, m)
    if y[k][0] == 1 and np.dot(x_new[k,:], w) < 0:
        w = w + x_new[k,:]
        
    
    if y[k][0] == 0 and np.dot(x_new[k,:], w) > 0:
        w = w - x_new[k,:]
    print(w)
    print('################')   

