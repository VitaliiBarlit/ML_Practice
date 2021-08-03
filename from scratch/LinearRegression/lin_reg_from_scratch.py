import matplotlib.pyplot as plt
from random import gauss, seed


seed(100)
length = 50
x = [i + gauss(0,1) for i in range(length)]
y = [j + gauss(1,7) for j in range(length)]

class LinearRegression:
    
    def __init__(self,x,y):
        try:
            plt
        except NameError:
           print('Add \'import matplotlib.pyplot as plt\' to code first or check spelling of this row')

        self.x = x
        self.y = y
    
    def __doc__(self):
        return 'Linear regression from Scratch'
    
    def mean(self, arr:list):
        return sum(arr) / len(arr)
    
    def cov(self):
        return sum([self.x[i] * self.y[i] for i in range(len(self.x))]) / len(self.x)
    
    def square(self):
        return sum([i ** 2 for i in self.x]) / len(self.x)
    
    def slope(self):
        return (self.cov() - self.mean(self.x)*self.mean(self.y))/(self.square() - self.mean(self.x) ** 2)
    
    def intercept(self):
        C = self.slope()
        return self.mean(self.y) - self.mean(self.x) * C
    
    def coefs(self):
        return [self.slope(),self.intercept()]
    
    def __str__(self):
        print('Coefficients: \nSlope: {} \nIntercep: {}'.format(self.coefs()[0], self.coefs()[1]))
    
    def predict(self):
        c = self.coefs()
        return [(c[0] * i) + c[1] for i in self.x]
    
    def graph(self):
        try:
            plt.scatter(self.x, self.y, color='blue')
            plt.plot(self.x, self.predict(), color='red', linewidth=3)
        except NameError:
            print('')
            
    def shape(self, array):
        rows = len(array)
        columns = 1
        
        for i in range(len(array)):
            try:
                len(array[i]) 
            except TypeError:
                return [rows, columns]
            else:
                cols = [len(array[i]) for i in range(len(array))]
                min_c = max(cols)
                max_c = min(cols)
                if min_c != max_c:
                    raise TypeError('Incorrect shape')
                else:
                    columns += len(array[i])
                    
                
        return [rows,int(columns)]
    
    def sq_error(self,arr:list,pred:list):
        return sum([(pred[i]-arr[i]) ** 2 for i in range(len(arr))])

    def coefficient_of_determination(self):
        y_mean_line = [self.mean(self.y) for i in self.y]
        squared_error_regr = self.sq_error(self.y,self.predict())
        squared_error_y_mean = self.sq_error(self.y, y_mean_line)
        return 1 - (squared_error_regr/squared_error_y_mean)
    
reg = LinearRegression(x, y)
reg.graph()
