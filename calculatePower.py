from math import *
from statistics import *
from scipy.stats import *
import numpy
import CondorcetDriver
import matplotlib.pyplot as plt
import inspect
import os


def power(xList, yList):
    if (emptyFile(xList, yList) == True):
        return -1
    else:
        xList = logList(xList)
        yList = logList(yList)
        r = linregress(xList, yList)
        b = r.slope
        c = exp(r.intercept)
    return [c, b]

def linearRegression(xList, yList):
    if (emptyFile(xList, yList) == True):
        return -1
    else:
        r = linregress(xList, yList)
        b = r.slope
        c = r.intercept
    return [c, b]

def logarithmic(xList, yList):
    if (emptyFile(xList, yList) == True):
        return -1
    else:
        xList = logList(xList)
        r = linregress(xList, yList)
        b = r.slope
        c = r.intercept
    return [c, b]

def exponential(xList, yList):
    if (emptyFile(xList, yList) == True):
        return -1
    else:
        yList = logList(yList)
        r = linregress(xList, yList)
        b = r.slope
        c = exp(r.intercept)
    return [c, b]

def logList(lst):
    loggedList = []
    for each in lst:
        if each == 0:
            each = 0
        else:
            each = numpy.log(each)
        loggedList.append(each)
    return loggedList

def emptyFile(xList, yList):
    if (len(xList) == 0 or len(yList) == 0):
        print("warning: empty file")
        return True
    return False
    
def printEquationToDataFile(lsResults, importFileName, equationType):
    c = lsResults[0]
    b = lsResults[1]
    if (equationType == 0):
        printableResults = ("Equation: y = " +  str(c) + " * x^" + str(b))
        fileName = "PowerEquationsFile.txt"
    if (equationType == 1):
        printableResults = ("Equation: y = " +  str(b) + " * x + " + str(c))
        fileName = "LinearRegressionEquationsFile.txt"
    if (equationType == 2):
        printableResults = ("Equation: y = (" +  str(c) + " * ln(x) + " + str(b))
        fileName = "LogarithmicEquationsFile.txt"
    if (equationType == 3):
        printableResults = ("Equation: y = " +  str(c) + " * e^(" + str(b) + " * x)")
        fileName = "ExponentialEquationsFile.txt"
    dataFile = open(fileName, mode = 'a')
    dataFile.write(importFileName)
    dataFile.write(": ")
    dataFile.write(printableResults)
    dataFile.write("\n")
    dataFile.close()

def writePointsToDataFile(lsResults, x, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy, directory):
    if (directory == "bPoints"):
        results = lsResults[1]
    elif (directory == "cPoints"):
        results = lsResults[0]
    if (targetVar == 0):
        fileName = "graphPointsNumPlayers/" + directory + "/_Discrepancy" + str(thisDiscrepancy) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".txt"
    elif (targetVar == 1):
        fileName = "graphPointsNumPlayersPerGame/" + directory + "/_Discrepancy" + str(thisDiscrepancy) + "_NumPlayers" + str(thisNumPlayers) + ".txt"
    elif (targetVar == 2):
        fileName = "graphPointsDiscrepancy/" + directory + "/_NumPlayers" + str(thisNumPlayers) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".txt"
    dataFile = open(fileName, mode = 'a') 
    dataFile.write(str(x) + "," + str(results))
    dataFile.write("\n")
    dataFile.close()
    return fileName

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
            if (line != "\n"):
                if (line[-1:] == "\n"):
                    line = line[0:-1]
                splitLine = line.split(",")
                xPoints.append(float(splitLine[0]))
                yPoints.append(float(splitLine[1]))
        r.close()
        return xPoints, yPoints

def calculatePower(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit):
    pointsListx, pointsListy = readFile(fileName)
    result = power(pointsListx, pointsListy)
    equationType = 0
    printEquationToDataFile(result, fileName, equationType)

def calculateLinearRegression(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit):
    pointsListx, pointsListy = readFile(fileName)
    result = linearRegression(pointsListx, pointsListy)
    equationType = 1
    printEquationToDataFile(result, fileName, equationType)

def calculateLogarithmic(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit):
    pointsListx, pointsListy = readFile(fileName)
    result = logarithmic(pointsListx, pointsListy)
    equationType = 2
    printEquationToDataFile(result, fileName, equationType)

def calculateExponential(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit):
    pointsListx, pointsListy = readFile(fileName)
    result = exponential(pointsListx, pointsListy)
    equationType = 3
    printEquationToDataFile(result, fileName, equationType)

def printPointsToDataFile(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, importFileName, timeLimit, targetVar):
    pointsListx, pointsListy = readFile(importFileName)
    result = power(pointsListx, pointsListy)
    if (targetVar == 0):
        X = thisNumPlayers
        xStr = "Number of Players"
    elif (targetVar == 1):
        X = thisNumPlayersPerGame
        xStr = "Number of Players Per Game"
    elif (targetVar == 2):
        X = thisDiscrepancy
        xStr = "Discrepancy"
    bFileName = writePointsToDataFile(result, X, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy, "bPoints")
    cFileName = writePointsToDataFile(result, X, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy, "cPoints")
    graphData(bFileName, xStr, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy, "b")
    graphData(cFileName, xStr, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy, "c")

def graphData(importFileName, xStr, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy, graphType):
    pointsListX, pointsListY = readFile(importFileName)
    plt.scatter(pointsListX, pointsListY)
    plt.xlabel(xStr)
    plt.ylabel(graphType + " Value")
    directory = ""
    positiveListY = []
    if (graphType == "b"):
        directory = "bPoints"
        for each in pointsListY:
            if each >= 0:
                each = 0
            else:
                each = each * -1
            positiveListY.append(each)
        powerTrendlineC, powerTrendlineB = power(pointsListX, positiveListY)
        exponentialTrendlineC, exponentialTrendlineB = exponential(pointsListX, positiveListY)
    elif (graphType == "c"):
        directory = "cPoints"
        powerTrendlineC, powerTrendlineB = power(pointsListX, pointsListY)
        exponentialTrendlineC, exponentialTrendlineB = exponential(pointsListX, pointsListY)
    linearTrendlineC, linearTrendlineB = linearRegression(pointsListX, pointsListY)
    logarithmicTrendlineC, logarithmicTrendlineB = logarithmic(pointsListX, pointsListY)
    print(logarithmicTrendlineC, logarithmicTrendlineB)
    maxX = max(pointsListX)
    powerLineX = numpy.linspace(1, maxX, 100)
    powerLineY= []
    for each in powerLineX:
        powerLineY.append(powerTrendlineC * numpy.power(each,powerTrendlineB))
    
    linearLineX = numpy.linspace(1, maxX, 100)
    linearLineY= []
    for each in linearLineX:
        linearLineY.append(linearTrendlineB * each + linearTrendlineC)
   
    logarithmicLineX = numpy.linspace(1, maxX, 100)
    logarithmicLineY= []
    for each in logarithmicLineX:
        logarithmicLineY.append(logarithmicTrendlineB * numpy.log(each) + logarithmicTrendlineC)
    
    exponentialLineX = numpy.linspace(1, maxX, 100)
    exponentialLineY= []
    for each in exponentialLineX:
        exponentialLineY.append(exponentialTrendlineC * exp(each * exponentialTrendlineB))
    
    plt.plot(powerLineX,powerLineY, color="green") ##works
    plt.plot(linearLineX,linearLineY, color="red")
    plt.plot(logarithmicLineX,logarithmicLineY, color="blue")
    plt.plot(exponentialLineX,exponentialLineY, color="black") ##works
    if (targetVar == 0):
        fileName = "graphPointsNumPlayers/" + directory + "/Graph_Discrepancy" + str(thisDiscrepancy) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".png"
    elif (targetVar == 1):
        fileName = "graphPointsNumPlayersPerGame/" + directory + "/Graph_Discrepancy" + str(thisDiscrepancy) + "_NumPlayers" + str(thisNumPlayers) + ".png"
    elif (targetVar == 2):
        fileName = "graphPointsDiscrepancy/" + directory + "/Graph_NumPlayers" + str(thisNumPlayers) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".png"
    if (os.path.exists(fileName)):
        os.remove(fileName)
    plt.savefig(fileName, dpi=72)
    plt.gcf().clear()

####printPointsToDataFile(50, 100, 4, 560, "dataFormat.txt", 100, 0)
    
    
