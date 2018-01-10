import calculatePower
import CondorcetDriver

numberOfMachines = 1
machineNumber = 1
firstTrial = 1
numberOfTrials = 1
baseNumPlayersPerGame = [4]
discrepancyRangeList = [560]
baseNumPlayers = [4, 8, 10, 20, 30, 40]
numGames = 100000
timeLimitMinutes = 5
targetVar = 0 ##0: player number, 1: player number per game, 2: disparity
directory = "CondorcetData/"
CondorcetDriver.DriveSimulator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar)
CondorcetDriver.trialGenerator(numberOfMachines, machineNumber, firstTrial, numberOfTrials, baseNumPlayersPerGame, discrepancyRangeList, baseNumPlayers, numGames, timeLimitMinutes, directory, targetVar, calculatePower.printPointsToDataFile)

