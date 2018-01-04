import Condorcet
import time
import math

def printLine():
    print('----------------')



def DriveSimulator():
    start = time.time()
    baseNumPlayersPerGame = 3
    baseNumGames = 1000
    baseDiscrepancy = 5
    discrepancyMultiplier = 5
    baseNumPlayers = 10
    for numPlayersPerGame in range(0,4):
        thisNumPlayersPerGame = baseNumPlayersPerGame + numPlayersPerGame
        for discrepancy in range(0,4):
            thisDiscrepancy = baseDiscrepancy + discrepancyMultiplier * discrepancy
            for numPlayers in range (1, 5):
                thisNumPlayers = baseNumPlayers * numPlayers
                thisNumGames = baseNumGames
                printLine()
                print("number of players = ", thisNumPlayers, "number of games = ", thisNumGames, "discrepancy = ", thisDiscrepancy, "number of players per game = ", thisNumPlayersPerGame)
                Condorcet.simulate(thisNumPlayers, thisNumGames, thisDiscrepancy, thisNumPlayersPerGame)
    end = time.time()
    print(end-start)



DriveSimulator()


            
