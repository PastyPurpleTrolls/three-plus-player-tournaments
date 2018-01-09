from math import *
from statistics import *
from scipy.stats import *
import numpy
import CondorcetDriver


def leastSquares(xList, yList):
    if (len(xList) == 0 or len(yList) == 0):
        print("warning: empty file", fileName)
        return
    r = linregress(xList, yList)
    b = r.slope
    c = exp(r.intercept)
    ##print(r)
    return [c, b]
    ##print(result)
    
def printToDataFile(lsResults, fileName):
    c = lsResults[0]
    b = lsResults[1]
    printableResults = ("Equation: y =" +  str(c) + "* x^" + str(b))
    dataFile = open("EquationsFile.txt", mode = 'a')
    dataFile.write(fileName)
    dataFile.write(": ")
    dataFile.write(printableResults)
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
    result = leastSquares(pointsListx, pointsListy)
    printToDataFile(result, fileName)

    


##CondorcetDriver.trialGenerator(1, 1, 6, 1, calculateLeastSquares)

