import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


rng = np.random.RandomState(1)


#X = 10 * rng.rand(10)
#Y = 2 * X - 5 + rng.rand(10)

#X = np.ones(10)
#Y = [0,2,4,8,8,8,8,4,2,0]
#Y = np.ones(10)
#y = np.array([1,2,3,4,0,0,0,0,1,2,3,4,0,0,0,0,1,2,3,4,0,0,0,0,1,2,3,4,0,0,0,0,])
#Y = Y * rng.rand(len(Y))
#x = np.linspace(0,2*np.pi,10)
#y = np.sin(x)
#plt.scatter(X,Y)
#y = [0,0,0,0,8,8,8,8,0,0,0,0,-8,-8,-8,-8,0,0,0,0,
#     12,12,12,12,0,0,0,0,-12,-12,-12,-12,0,0,0,0,]
y = [0,0,0,0,8,8,8,8,0,0,0,0,12,12,12,12,0,0,0,0,
     16,16,16,16,0,0,0,0,20,20,20,20,0,0,0,0,]
x = np.array([0,1,2,3,3,4,5,6,6,7,8,9,9,10,11,12,12,13,14,15,
              15,16,17,18,18,19,20,21,21,22,23,24,24,25,26,27])
#y = [0,2,4,8,8,8,8,4,2,0,0,0,0,-2,-4,-8,-8,-8,-8,-4,-2,0]
#x = np.array([i for i in range(len(y))])


from sklearn.linear_model import LinearRegression

'''
              Линейная регрессия
'''
"""
from sklearn.linear_model import LinearRegression

model1 = LinearRegression(fit_intercept=True)

model1.fit(X[:, np.newaxis],Y)

xfit = np.linspace(0,10,10)
yfit = model1.predict(xfit[:, np.newaxis])

plt.scatter(X,Y)
plt.plot(xfit,yfit)

print('Угловой коэффициент: ', model1.coef_[0])
print('Точка пересечения с осью координат Y: ', model1.intercept_)
"""


'''
        Полиномиальные базисные функции
'''
from sklearn.preprocessing import PolynomialFeatures
#poly = PolynomialFeatures(3, include_bias=False)
#poly.fit_transform(X[:,None])

from sklearn.pipeline import make_pipeline
#poly_model1 = make_pipeline(PolynomialFeatures(7),LinearRegression)
#
#poly_model1.fit(X[:, np.newaxis], Y)
#
#xfit = np.linspace(0,10,1000)
#yfit = poly_model1.predict(xfit[:, np.newaxis])
#
#plt.scatter(X,Y)
#plt.plot(xfit,yfit)

#
#poly = PolynomialFeatures(5, include_bias=False)
#poly.fit_transform(x[:, None])
#
#poly_model = make_pipeline(PolynomialFeatures(3), LinearRegression())
#xfit = np.linspace(0,len(y)-2,100)
#
#rng = np.random.RandomState(1)
##x = 10 * rng.rand(50)
##y = np.sin(x) + 0.1 * rng.randn(50)
#poly_model.fit(x[:, np.newaxis], y)
#yfit = poly_model.predict(xfit[:, np.newaxis])
#plt.scatter(x, y)
#plt.plot(xfit, yfit);


from sklearn.base import BaseEstimator, TransformerMixin

class GaussianFeatures(BaseEstimator, TransformerMixin):
    
    def __init__(self, N, width_factor=2.0):
        self.N = N
        self.width_factor = width_factor
        
    @staticmethod
    def _gauss_basis(x, y, width, axis=None):
        arg = (x - y) / width
        return np.exp(-0.5 * np.sum(arg ** 2, axis))

    def fit(self, X, y=None):
        self.centers_ = np.linspace(X.min(), X.max(), self.N)
        self.width_ = self.width_factor * (self.centers_[1] - self.centers_[0])
        return self
    
    def transform(self, X):
        return self._gauss_basis(X[:, :, np.newaxis], 
                                 self.centers_, self.width_, axis=1)
        
gauss_model = make_pipeline(GaussianFeatures(40), LinearRegression())
xfit = x
gauss_model.fit(x[:, np.newaxis], y)
yfit = gauss_model.predict(xfit[:, np.newaxis])


#plt.scatter(x, y)
#plt.plot(xfit, yfit)
#plt.xlim(0, 10);


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# график коэффициентов Гауссовых базисных функций в соответствии с координатой x 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def basis_plot(model, title=None):
    fig, ax = plt.subplots(2, sharex=True)
    model.fit(x[:, np.newaxis], y)
    ax[0].scatter(x, y)
    ax[0].plot(xfit, model.predict(xfit[:, np.newaxis]))
    ax[0].set(xlabel='x', ylabel='y',)
    if title:
        ax[0].set_title(title)

    ax[1].plot(model.steps[0][1].centers_,
               model.steps[1][1].coef_);
    ax[1].set(xlabel='basis location', # Базовое местоположение
              ylabel='coefficient',    # Коэффициент
              xlim=(0, 20));
    
#model = make_pipeline(GaussianFeatures(30), LinearRegression())
#basis_plot(model)

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge


model_lasso = make_pipeline(GaussianFeatures(30), Lasso(alpha=0.001))
model_ridge = make_pipeline(GaussianFeatures(30), Ridge(alpha=0.01))

plt.figure(1)
basis_plot(model_lasso)

plt.figure(2)
basis_plot(model_ridge)








































