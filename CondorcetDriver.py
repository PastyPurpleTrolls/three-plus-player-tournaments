import Condorcet
import time

def printLine():
    print('----------------')


def generateFileName(numPlayers, numPlayersPerGame, discrepancyRange, trial):
    fileName = "CondorcetData/_discrepancyRange" + str(discrepancyRange) + "_numPlayers" + str(numPlayers) + "_numPlayersPerGame" + str(numPlayersPerGame) + "_trial" + str(trial) + ".txt"
    return(fileName)


def DriveSimulator(trialNumber):  #trial number should be between 0 and 5
    start = time.time()
    baseNumPlayersPerGame = [3, 4, 5]
    baseNumGames = 50000
    discrepancyRangeList = [280, 560, 1120]
    baseNumPlayers = [10, 40, 70]
    for discrepancyIdx in range(0,3):
        thisDiscrepancyRange = discrepancyRangeList[discrepancyIdx]
        for numPlayersPerGameIdx in range(0,3):
            thisNumPlayersPerGame = baseNumPlayersPerGame[numPlayersPerGameIdx]
            for numPlayerIdx in range (0, 3):
                thisNumPlayers = baseNumPlayers[numPlayerIdx]
                thisDiscrepancy = thisDiscrepancyRange//thisNumPlayers
                print(thisDiscrepancy)
                for trial in range(trialNumber,trialNumber+1):
                    thisNumGames = baseNumGames                    
                    printLine()
                    print("number of players = ", thisNumPlayers, "number of games = ", thisNumGames, "discrepancy = ", thisDiscrepancyRange, "number of players per game = ", thisNumPlayersPerGame)
                    fileName = generateFileName(thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancyRange, trial)
                    Condorcet.simulate(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, 500)
    end = time.time()
    print(end-start)



DriveSimulator(2)


            
