import calculatePower
import CondorcetDriver

numberOfMachines = 1
machineNumber = 1
firstTrial = 1
numberOfTrials = 1
baseNumPlayersPerGame = [4]
discrepancyRangeList = [560]
baseNumPlayers = [1000]
numGames = 1000000
timeLimitMinutes = 1120
targetVariable = 0
directory = "CondorcetData/"
##CondorcetDriver.DriveSimulator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes)
CondorcetDriver.trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVariable, calculatePower.calculateLeastSquares)


