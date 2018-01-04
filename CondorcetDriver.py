import Condorcet
import time

def printLine():
    print('----------------')


def generateFileName(numPlayers, numPlayersPerGame, discrepancy, trial):
    fileName = "CondorcetData/_discrepancy" + str(discrepancy) + "_numPlayers" + str(numPlayers) + "_numPlayersPerGame" + str(numPlayersPerGame) + "_trial" + str(trial)
    return(fileName)


def DriveSimulator():
    start = time.time()
    baseNumPlayersPerGame = 3
    baseNumGames = 100000
    discrepancyList = [5, 25, 100]
    baseNumPlayers = 10
    for discrepancy in range(0,3):
        thisDiscrepancy = discrepancyList[discrepancy]
        for numPlayersPerGame in range(0,3):
            thisNumPlayersPerGame = baseNumPlayersPerGame + numPlayersPerGame
            for numPlayers in range (1, 8, 3):
                thisNumPlayers = baseNumPlayers * numPlayers
                for trial in range(0,5):
                    thisNumGames = baseNumGames                    
                    printLine()
                    print("number of players = ", thisNumPlayers, "number of games = ", thisNumGames, "discrepancy = ", thisDiscrepancy, "number of players per game = ", thisNumPlayersPerGame)
                    fileName = generateFileName(thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancy, trial)
                    Condorcet.simulate(thisNumPlayers, thisNumGames, thisDiscrepancy, thisNumPlayersPerGame, fileName, 20)
    end = time.time()
    print(end-start)



DriveSimulator()


            
