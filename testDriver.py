import calculatePower
import CondorcetDriver

numberOfMachines = 6
machineNumber = 1
firstTrial = 1
numberOfTrials = 5
baseNumPlayersPerGame = [4]
discrepancyRangeList = [560]
baseNumPlayers = [4, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 250, 500, 1000]
CondorcetDriver.DriveSimulator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers)
CondorcetDriver.trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, calculatePower.calculateLeastSquares)


