import Condorcet
import time
import inspect

def printLine():
    print('----------------')


def generateFileName(numPlayers, numPlayersPerGame, discrepancyRange, trial, directory):
    fileName = str(directory) + "_discrepancyRange" + str(discrepancyRange) + "_numPlayers" + str(numPlayers) + "_numPlayersPerGame" + str(numPlayersPerGame) + "_trial" + str(trial) + ".txt"
    return(fileName)



def trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar, function):
    i = machineNumber # should range between 1 and number of machines
    start = time.time()
    baseNumGames = numGames
    timeLimit = timeLimitMinutes*60
    for discrepancyIdx in range(0, len(discrepancyRangeList)):
        thisDiscrepancyRange = discrepancyRangeList[discrepancyIdx]
        for numPlayersPerGameIdx in range(0, len(baseNumPlayersPerGame)):
            thisNumPlayersPerGame = baseNumPlayersPerGame[numPlayersPerGameIdx]
            for numPlayerIdx in range (0, len(baseNumPlayers)):
                thisNumPlayers = baseNumPlayers[numPlayerIdx]
                thisDiscrepancy = thisDiscrepancyRange//thisNumPlayers ##
                for trial in range(firstTrial,firstTrial+numberOfTrials):
                    thisNumGames = baseNumGames                    
                    if (i%numberOfMachines == 0):
                        fileName = generateFileName(thisNumPlayers, thisNumPlayersPerGame, thisDiscrepancyRange, trial, directory)
                        argspecs = inspect.getargspec(function)
                        argCount = (len(argspecs.args))
                        if (argCount == 6):
                            function(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancy, fileName, timeLimit)
                        elif (argCount == 7):
                            function(thisNumPlayers, thisNumGames, thisNumPlayersPerGame, thisDiscrepancyRange, fileName, timeLimit, targetVar)                         
                    i+=1
    end = time.time()
    print(end-start)

def DriveSimulator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar):
    trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar, Condorcet.simulate)

##DriveSimulator(4, 4, 6, 1)




            
