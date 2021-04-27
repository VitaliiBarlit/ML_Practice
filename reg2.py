import numpy as np
import pandas as pd
import statsmodels.api as sm
import patsy as pt
import sklearn.linear_model as lm
import matplotlib.pyplot as plt


X = np.array([i for i in range(0,96,2)])
Y = np.array([0,0,0,0,
              1,1,1,1,
              0,0,0,0,
              -1,-1,-1,-1,
              0,0,0,0,
              1,1,1,1,
              0,0,0,0,
              -1,-1,-1,-1,
              0,0,0,0,
              1,1,1,1,
              0,0,0,0,
              -1,-1,-1,-1,
              ])


from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline


poly = PolynomialFeatures(5, include_bias=False)
poly.fit_transform(X[:, None])

poly_model = make_pipeline(PolynomialFeatures(10), LinearRegression())
xfit = np.linspace(-4,96,1000)

rng = np.random.RandomState(1)
poly_model.fit(X[:, np.newaxis], Y)
yfit = poly_model.predict(xfit[:, np.newaxis])

plt.figure(1)
plt.scatter(X, Y)
plt.plot(xfit, yfit);


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
xfit = X
gauss_model.fit(X[:, np.newaxis], Y)
yfit = gauss_model.predict(xfit[:, np.newaxis])

def basis_plot(model, title=None):
    fig, ax = plt.subplots(2, sharex=True)
    model.fit(X[:, np.newaxis], Y)
    ax[0].scatter(X, Y);
    ax[0].plot(xfit, model.predict(xfit[:, np.newaxis]));
    ax[0].set(xlabel='x', ylabel='y',)
    if title:
        ax[0].set_title(title)

    ax[1].plot(model.steps[0][1].centers_,
               model.steps[1][1].coef_);
    ax[1].set(xlabel='basis location', # Базовое местоположение
              ylabel='coefficient',    # Коэффициент
              xlim=(0, 100));
    
#model = make_pipeline(GaussianFeatures(30), LinearRegression())
#basis_plot(model)

from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge


model_lasso = make_pipeline(GaussianFeatures(85), Lasso(alpha=0.001))
model_ridge = make_pipeline(GaussianFeatures(65), Ridge(alpha=0.01))

plt.figure(2)
basis_plot(model_lasso)

plt.figure(3)
basis_plot(model_ridge)



#plt.plot(X,Y)


