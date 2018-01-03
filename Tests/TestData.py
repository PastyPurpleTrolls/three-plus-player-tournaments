import Condorcet


#condorsetWinners
perfectPlayer = Condorcet.player(4000)
perfectPlayer.game = 1 ##just needs to not equal 0
perfectPlayer.id = 5 ##id must equal rank where higher is better
perfectPlayer.W = 4

greatPlayer = Condorcet.player(3000)
greatPlayer.game = 1
greatPlayer.id = 4
greatPlayer.W = 3

goodPlayer = Condorcet.player(2000)
goodPlayer.game = 1
goodPlayer.id = 3
goodPlayer.W = 2

badPlayer = Condorcet.player(1000)
badPlayer.game = 1
badPlayer.id = 2
badPlayer.W = 1

terriblePlayer = Condorcet.player(0)
terriblePlayer.game = 1
terriblePlayer.id = 1
terriblePlayer.W = 0

condorcetWinnerPlayersList = [perfectPlayer, greatPlayer, goodPlayer, badPlayer, terriblePlayer]


#noCondorsetWinners
bestPlayer = Condorcet.player(2500)
bestPlayer.game = 1 ##just needs to not equal 0
bestPlayer.id = 5 ##id must equal rank where higher is better
bestPlayer.W = 3

greatPlayer = Condorcet.player(2250)
greatPlayer.game = 1
greatPlayer.id = 4
greatPlayer.W = 2

goodPlayer = Condorcet.player(2000)
goodPlayer.game = 1
goodPlayer.id = 3
goodPlayer.W = 2

badPlayer = Condorcet.player(1750)
badPlayer.game = 1
badPlayer.id = 2
badPlayer.W = 2

terriblePlayer = Condorcet.player(1500)
terriblePlayer.game = 1
terriblePlayer.id = 1
terriblePlayer.W = 1

noCondorcetWinnerPlayersList = [bestPlayer, greatPlayer, goodPlayer, badPlayer, terriblePlayer]


def getCondorcetWinnersList():
    return condorcetWinnerPlayersList

def getNoCondorcetWinnersList():
    return noCondorcetWinnerPlayersList
