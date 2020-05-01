import numpy as np 
import matplotlib.pyplot as plt 

def f(w, b, x):
    return 1/(1+np.exp(-(w*x+b)))

def w_grad(w, b, x, Y):
    fx = f(w, b, x)
    dw = np.sum((fx-Y)*fx*(1-fx)*x)/5
    # print('w',dw)
    return dw

def b_grad(w, b, x, Y):
    fx = f(w, b, x)
    db = np.sum((fx-Y)*fx*(1-fx))/5
    # print('b',db)
    return db

def error(w,b):
    n = Y.shape[0]
    loss = np.sum((f(w,b,X)-Y)**2)/(2*n)
    return loss

def update(eta, epochs, X, Y):
    # initialization of w and b
    w = 0
    b = 0
    for epoch in range(epochs):
        w = w - eta*w_grad(w,b,X,Y)
        b = b - eta*b_grad(w,b,X,Y)
        print('Current Loss is:', error(w,b))
    print('Converged w and b:', w, b)
    return w,b

if __name__ == "__main__":
    X = np.array([[2], [3], [4], [5], [8]])
    Y = np.array([[0.047], [0.268], [0.73], [0.952], [0.999]])
    print(Y.shape)
    w, b = update(1, 10000, X, Y)
    # w, b = 2, -7
    plt.plot(X,Y,'*')
    x_new = np.linspace(-5, 10, 100)
    z = f(w,b,x_new)
    plt.plot(x_new,z)
    plt.show()

    