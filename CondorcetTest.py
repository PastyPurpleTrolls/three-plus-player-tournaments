import Condorcet
import TestData

globalCorrectTests = 0
globalIncorrectTests = 0

def PrintResult(string, expectedResult, actualResult):
    print("Test", string, " ->expected:", expectedResult, " ->actual:", actualResult)
    if (expectedResult == actualResult):
        print('TEST PASSED')
        global globalCorrectTests
        globalCorrectTests += 1
        return 1
    else:
        print('TEST FAILED')
        global globalIncorrectTests
        globalIncorrectTests += 1
        return -1

def printLine():
    print("----------------")

def InterpretTestTotals():
    printLine()
    print ("Tests passed = ", globalCorrectTests, "/",globalIncorrectTests+globalCorrectTests)
    if (globalIncorrectTests == 0):
        print ("ALL TESTS PASSED!! :)")
    else:
        print ("FAILING TESTS")

CondorcetWinner = Condorcet.RMSE(TestData.getCondorcetWinnersList(), 5)
NoCondorcetWinner = Condorcet.RMSE(TestData.getNoCondorcetWinnersList(), 5)

##TestSuite
PrintResult("CondorcetWinner", 0.0, CondorcetWinner)
PrintResult("NoCondorcetWinner", 0.0, NoCondorcetWinner)
InterpretTestTotals()

    
    
