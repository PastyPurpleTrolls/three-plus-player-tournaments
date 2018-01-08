from math import *
from statistics import *
from scipy.stats import *
import numpy
import CondorcetDriver


def leastSquares(xList, yList, fileName):
    if (len(xList) == 0 or len(yList) == 0):
        print("warning: empty file", fileName)
        return
    r = linregress(xList, yList)
    b = r.slope
    c = exp(r.intercept)
    ##print(r)
    result = ("Equation: y =" +  str(c) + "* x^" + str(b))
    ##print(result)
    dataFile = open("EquationsFile.txt", mode = 'a')
    dataFile.write(fileName)
    dataFile.write(": ")
    dataFile.write(result)
    dataFile.write("\n")
    dataFile.close()


   

def readFile(fileName):
    try:
        r = open(fileName, mode = 'r')
    except FileNotFoundError:
        print("warning: file not found", fileName)
        return [], []
    else:
        data = r.readlines()
        xPoints = []
        yPoints = []
        for line in data:
            if (line[0:-1] == "\n"):
                line = line[0:-1]
            splitLine = line.split(",")
            xPoints.append(numpy.log(int(splitLine[0])))
            if (float(splitLine[1]) == 0.0):
                yPoints.append(0)
            else:
                yPoints.append(numpy.log(float(splitLine[1])))
        ##print (xPoints,yPoints)
        r.close()
        return xPoints, yPoints

def calculateLeastSquares(a, b, c, d, fileName, f):
    pointsListx, pointsListy = readFile(fileName)
    leastSquares(pointsListx, pointsListy, fileName)
    


##CondorcetDriver.trialGenerator(1, 1, 6, 1, calculateLeastSquares)

