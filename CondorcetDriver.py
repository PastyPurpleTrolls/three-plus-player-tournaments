import Condorcet
import time

def printLine():
    print('----------------')


def generateFileName(numPlayers, numPlayersPerGame, discrepancyRange, trial):
    fileName = "CondorcetData/_discrepancyRange" + str(discrepancyRange) + "_numPlayers" + str(numPlayers) + "_numPlayersPerGame" + str(numPlayersPerGame) + "_trial" + str(trial) + ".txt"
    return(fileName)



def trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, function): #@Kyle pass a function with 6 parameters to do that thing to the variables that trial generator generates
    i = machineNumber # should range between 1 and number of machines
    start = time.time()
    baseNumPlayersPerGame = [4]
    baseNumGames = 100000
    timeLimitMinutes = 20
    timeLimit = timeLimitMinutes*60
    discrepancyRangeList = [500]
    baseNumPlayers = [500]
    for discrepancyIdx in range(0, len(discrepancyRangeList)):
        thisDiscrepancyRange = discrepancyRangeList[discrepancyIdx]
        for numPlayersPerGameIdx in range(0, len(baseNumPlayersPerGame)):
            thisNumPlayersPerGame = baseNumPlayersPerGame[numPlayersPerGameIdx]
            for numPlayerIdx in range (0, len(baseNumPlayers)):
                thisNumPlayers = baseNumPlayers[numPlayerIdx]
                thisDiscrepancy = thisDiscrepancyRange//thisNumPlayers
                print(thisDiscrepancy)
                for trial in range(firstTrial,firstTrial+numberOfTrials):
                    thisNumGames = baseNumGames                    
                    printLine()
                    if (i%numberOfMachines == 0):
                        print("number of players = ", thisNumPlayers, "number of games = ", thisNumGames, "discrepancy = ", thisDiscrepancyRange, "number of players per game = ", thisNumPlayersPerGame)
                        fileName = generateFileName(thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancyRange, trial)
                        function(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit)
                    i+=1
    end = time.time()
    print(end-start)

def DriveSimulator(numberOfMachines, machineNumber, firstTrial, numberOfTrials):
    trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, Condorcet.simulate)

DriveSimulator(1, 1, 10, 1)




            
