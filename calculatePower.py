from math import *
from statistics import *
from scipy.stats import *
import matplotlib.pyplot as plt
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

def printCPointsToDataFile(lsResults, x, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy):
    c = lsResults[0]
    if (targetVar == 0):
        fileName = "graphPointsNumPlayers/cPoints/_Discrepancy" + str(thisDiscrepancy) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".txt"
    elif (targetVar == 1):
        fileName = "graphPointsNumPlayersPerGame/cPoints/_Discrepancy" + str(thisDiscrepancy) + "_NumPlayers" + str(thisNumPlayers) + ".txt"
    elif (targetVar == 2):
        fileName = "graphPointsDiscrepancy/cPoints/_NumPlayers" + str(thisNumPlayers) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".txt"
    dataFile = open(fileName, mode = 'a') 
    dataFile.write(str(x) + "," + str(c))
    dataFile.write("\n")
    dataFile.close()
    return fileName

def printBPointsToDataFile(lsResults, x, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy):
    b = lsResults[1]
    if (targetVar == 0):
        fileName = "graphPointsNumPlayers/bPoints/_Discrepancy" + str(thisDiscrepancy) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".txt"
    elif (targetVar == 1):
        fileName = "graphPointsNumPlayersPerGame/bPoints/_Discrepancy" + str(thisDiscrepancy) + "_NumPlayers" + str(thisNumPlayers) + ".txt"
    elif (targetVar == 2):
        fileName = "graphPointsDiscrepancy/bPoints/_NumPlayers" + str(thisNumPlayers) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".txt"
    dataFile = open(fileName, mode = 'a') 
    dataFile.write(str(x) + "," + str(b))
    dataFile.write("\n")
    dataFile.close()
    return fileName

def readFileLog(fileName):
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
        r.close()
        return xPoints, yPoints

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
            xPoints.append(float(splitLine[0]))
            if (float(splitLine[1]) == 0.0):
                yPoints.append(0)
            else:
                yPoints.append(float(splitLine[1]))
        r.close()
        return xPoints, yPoints

def calculateLeastSquares(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit):
    pointsListx, pointsListy = readFileLog(fileName)
    result = leastSquares(pointsListx, pointsListy)
    printEquationToDataFile(result, fileName)

def printPointsToDataFile(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit, targetVar):
    print(thisDiscrepancy)
    pointsListx, pointsListy = readFileLog(fileName)
    result = leastSquares(pointsListx, pointsListy)
    if (targetVar == 0):
        X = thisNumPlayers
        xStr = "Number of Players"
    elif (targetVar == 1):
        X = thisNumPlayersPerGame
        xStr = "Number of Players Per Game"
    elif (targetVar == 2):
        X = thisDiscrepancy
        xStr = "Discrepancy"
    cFileName = printCPointsToDataFile(result, X, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy)
    bFileName = printBPointsToDataFile(result, X, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy)
    graphDataB(bFileName, xStr, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy)
    graphDataC(cFileName, xStr, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy)
    print(bFileName)

def graphDataB(bFileName, xStr, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy):
    pointsListXB, pointsListYB = readFile(bFileName)
    plt.figure(figsize=(8,6), dpi=80)
    plt.scatter(pointsListXB, pointsListYB)
    plt.xlabel(xStr)
    plt.ylabel("B Value")
    if (targetVar == 0):
        fileName = "graphPointsNumPlayers/bPoints/Graph_Discrepancy" + str(thisDiscrepancy) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".png"
    elif (targetVar == 1):
        fileName = "graphPointsNumPlayersPerGame/bPoints/Graph_Discrepancy" + str(thisDiscrepancy) + "_NumPlayers" + str(thisNumPlayers) + ".png"
    elif (targetVar == 2):
        fileName = "graphPointsDiscrepancy/bPoints/Graph_NumPlayers" + str(thisNumPlayers) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".png"
    plt.savefig(fileName, dpi=72)
    
def graphDataC(cFileName, xStr, targetVar, thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy):
    pointsListXC, pointsListYC = readFile(cFileName)
    plt.figure(figsize=(8,6), dpi=80)
    plt.scatter(pointsListXC, pointsListYC)
    plt.xlabel(xStr)
    plt.ylabel("C Value")
    if (targetVar == 0):
        fileName = "graphPointsNumPlayers/cPoints/Graph_Discrepancy" + str(thisDiscrepancy) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".png"
    elif (targetVar == 1):
        fileName = "graphPointsNumPlayersPerGame/cPoints/Graph_Discrepancy" + str(thisDiscrepancy) + "_NumPlayers" + str(thisNumPlayers) + ".png"
    elif (targetVar == 2):
        fileName = "graphPointsDiscrepancy/cPoints/Graph_NumPlayers" + str(thisNumPlayers) + "_NumPlayersPerGame" + str(thisNumPlayersPerGame) + ".png"
    plt.savefig(fileName, dpi=72)

##printPointsToDataFile(4, 2, 3, 5, "dataFormat.txt", 5, 0)    
