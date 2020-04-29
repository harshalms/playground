import numpy as np 
import matplotlib.pyplot as plt
class MP_neuron:

    def __init__(self):
        self.b = None

    def model(self, x):
        return int(sum(x)>=self.b)

    def predict(self, X):
        Y = []
        for x in X:
            Y.append(self.model(x))
        Y = np.expand_dims(np.array(Y), 1)
        return Y

    def fit(self, X, Y):
        accuracy = {}
        for b in range(X.shape[0]+1):
            self.b = b
            Y_pred = self.predict(X)
            accuracy[b] = self.accuracy_score(Y_pred, Y)
        print(accuracy)
        accuracy = {'a': 3, 'b': 4, 'c': 4}
        best_b = max(accuracy, key=accuracy.get)
        self.b = best_b
        print('Optimal value of b is:', best_b)
        print('Maximum accuracy is:', accuracy[best_b])
        

    def accuracy_score(self, Y_pred, Y):
        # import pdb;pdb.set_trace();
        correct_count = int(sum(Y_pred == Y))
        accuracy = correct_count*100/Y.shape[0]
        return accuracy



if __name__ == "__main__":
    X = np.random.randint(0,2,(10,3))
    # print(X)
    Y = np.random.randint(0,2,(10,1))
    neuron = MP_neuron()
    neuron.fit(X,Y)
    plt.plot(X,Y,'*')
    plt.show()