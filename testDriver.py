import calculatePower
import CondorcetDriver

numberOfMachines = 1
machineNumber = 1
firstTrial = 1
numberOfTrials = 1
baseNumPlayersPerGame = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 30]
discrepancyRangeList = [1000]
baseNumPlayers = [60]
numGames = 100000
timeLimitMinutes = 5
CondorcetDriver.DriveSimulator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes)
CondorcetDriver.trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, calculatePower.calculateLeastSquares)


