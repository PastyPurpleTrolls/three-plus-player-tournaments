import numpy as np
from scipy.optimize import leastsq


def getData():
    return [[-0.042780748663101636, -0.0040771571786609945, -0.00506567946276074],
        [0.042780748663101636, -0.0044771571786609945, -0.10506567946276074],
        [0.542780748663101636, -0.005771571786609945, 0.30506567946276074],
        [-0.342780748663101636, -0.0304077157178660995, 0.90506567946276074]]



data = np.array(getData())
coefficient = data[:,0:2]
dependent = data[:,-1]

def model(p, x):
    a,b,c = p
    u = x[:,0]
    v = x[:,1]
    return(a*u**2 + b*v + c)

def residuals(p, y, x):
    a,b,c = p
    err = y - model(p,x)
    return err

p0 = np.array([2, 3, 4])  #arbitary guess

p = leastsq(residuals, p0, args = (dependent, coefficient))[0]

def f(p,x):
    return p[0]*x[0] + p[1]*x[1] + p[2]

def getPredictionPoints():
    predictionPoints = []
    for x in coefficient:
        predicionPoint = (f(p,x))
        predictionPoints.append(predicionPoint)
    return predictionPoints

def getActualPoints():
    return dependent

def getResiduals():
    predictionPoints = getPredictionPoints()
    actualPoints = getActualPoints()
    residualPoints = []
    for i in range(len(predictionPoints)):
        print(predictionPoints[i])
        residualPoints.append(predictionPoints[i] - actualPoints[i])
    return residualPoints

       


    
