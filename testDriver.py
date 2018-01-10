import calculatePower
import CondorcetDriver

numberOfMachines = 1
machineNumber = 1
firstTrial = 1
numberOfTrials = 1
baseNumPlayersPerGame = [8, 24]
discrepancyRangeList = [560, 5000, 10000, 100000]
baseNumPlayers = [4, 8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
numGames = 100000
timeLimitMinutes = 5
CondorcetDriver.DriveSimulator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes)
CondorcetDriver.trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, calculatePower.calculateLeastSquares)


