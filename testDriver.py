import calculatePower
import CondorcetDriver

numberOfMachines = 3
machineNumber = 3
firstTrial = 1
numberOfTrials = 1
baseNumPlayersPerGame = [3, 4, 5, 6]
discrepancyRangeList = [560, 1000, 5000]
baseNumPlayers = [60, 70, 80, 90, 100]
numGames = 100000
timeLimitMinutes = 5
targetVar = 0 ##0: player number, 1: player number per game, 2: disparity
directory = "NormalCondorcetData/"
CondorcetDriver.DriveSimulator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar)
CondorcetDriver.trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar, calculatePower.printPointsToDataFile)
##CondorcetDriver.trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar, calculatePower.calculateLeastSquares)


