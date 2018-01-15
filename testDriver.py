import calculatePower
import CondorcetDriver

numberOfMachines = 1
machineNumber = 1
firstTrial = 1
numberOfTrials = 1
baseNumPlayersPerGame = [3, 4, 5 ,6]
discrepancyRangeList = [100, 560, 1000, 2500, 5000]
baseNumPlayers = [4, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
numGames = 100000
timeLimitMinutes = 5
targetVar = 0 ##0: player number, 1: player number per game, 2: disparity
directory = "CondorcetData/"
CondorcetDriver.DriveSimulator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar)
CondorcetDriver.trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar, calculatePower.printPointsToDataFile)
##CondorcetDriver.trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar, calculatePower.calculateLeastSquares)


