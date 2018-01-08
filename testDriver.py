import calculatePower
import CondorcetDriver

numberOfMachines = 1
machineNumber = 1
firstTrial = 1
numberOfTrials = 5
baseNumPlayersPerGame = [3, 4, 5]
discrepancyRangeList = [280, 560, 1120]
baseNumPlayers = [10, 20, 40, 70, 130, 250]
CondorcetDriver.DriveSimulator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers)
CondorcetDriver.trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, calculatePower.calculateLeastSquares)


