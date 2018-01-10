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
    return [c, b]
    
def printEquationToDataFile(lsResults, fileName):
    c = lsResults[0]
    b = lsResults[1]
    printableResults = ("Equation: y =" +  str(c) + "* x^" + str(b))
    dataFile = open("EquationsFile.txt", mode = 'a')
    dataFile.write(fileName)
    dataFile.write(": ")
    dataFile.write(printableResults)
    dataFile.write("\n")
    dataFile.close()

def printCPointsToDataFile(lsResults, x):
    c = lsResults[0]
    dataFile = open("graphPointsC.txt", mode = 'a') 
    dataFile.write(str(c) + "," + str(x))
    dataFile.write("\n")
    dataFile.close()

def printBPointsToDataFile(lsResults, x):
    b = lsResults[1]
    dataFile = open("graphPointsB.txt", mode = 'a') 
    dataFile.write(str(b) + "," + str(x))
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

def calculateLeastSquares(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit):
    pointsListx, pointsListy = readFile(fileName)
    result = leastSquares(pointsListx, pointsListy)
    printEquationToDataFile(result, fileName)

def printPointsToDataFile(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit, targetVar):
    pointsListx, pointsListy = readFile(fileName)
    result = leastSquares(pointsListx, pointsListy)
    if (targetVar == 0):
        X = thisNumPlayers
    elif (targetVar == 1):
        X = thisNumPlayersPerGame
    elif (targetVar == 2):
        X = thisDiscrepancy
    printCPointsToDataFile(result, X)
    printBPointsToDataFile(result, X)

def graphData(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit):
    pointsListx, pointsListy = readFile(fileName)
    result = leastSquares(pointsListx, pointsListy)
    print (result, thisNumPlayers)
##    plt.figure(figsize=(8,6), dpi=80)
##    plt.plot(, , color="blue", linewidth=1.0, linestyle="-")
##    plt.xlim(4.0,250.0)
##    plt.xticks(np.linspace(-4,4,9,endpoint=True))
##    plt.ylim(0.0,9.0)
##    plt.yticks(np.linspace(-1,1,5,endpoint=True))
##    plt.savefig("exercice_2.png",dpi=72)
##    plt.show()

printPointsToDataFile(4, 2, 3, 5, "dataFormat.txt", 5, 2)    
graphData(4, 2, 3, 4, "dataFormat.txt", 5)
