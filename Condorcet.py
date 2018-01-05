#Condorcet Voting Test
#Dallas Mullet
from random import *
from math import *
from time import *

#Players
#Player object with several values that are tracked through several stages of the game
class player:
    def __init__(self, rating): #Requires an ELO Rating parameter
        self.prob = (randrange(0, 101)) #Random Number they "guess" (traditional game only)
        #self.elo = (randrange(1000, 3001, 50)) #Uncomment and modify code for completely random games
        self.elo = rating  #Elo Score set to rating 
        self.rate = 10**(self.elo/400)      #Chance of them winning a game                     
        self.guess = -1                       #Initialization of a variable we need further on
        self.rand = -1                      #Helps the game maker choose randomly
        self.game = 0                        #Helps the game maker keep track of how many games each player has been in
        self.id = -1                          #Helps game keeper track positions in the matrix
        self.wins = 0                         #Keeps track of this player's wins. 
        self.losses = 0                      #Keeps track of this player's losses
        self.W = 0                      #Condorcet Wins
        self.L=0                       #Condorcet Losses
        self.T=0                      #Condorcet Ties


#Create Players Systematically
def createXPlayers(x, lst, disparity):
    i = 0
    lastRating = 1000
    while i < x:
        lst.append(player(lastRating))
        lastRating += disparity
        lst[i].id = i
        i+=1


#Create Matrix Systematically
def createMatrix(numPlayers, mtrx):
    r = 0
    while r < numPlayers:
        mtrx.append([])
        c = 0
        while c < numPlayers:
            mtrx[r].append(0)
            c+=1
        mtrx[r][r] = -1
        r+=1

#Make this look nice here...
def printMatrix(playMat, condorSet): #Requires List of Players and Matrix to be printed
    size = len(condorSet)
    p = 0
    print("ID|GUESS|1   2   3   4   5   6   7   8   9   10   11   12   13   14   15...")
    while p < size:
        print(playMat[p].id+1,")",playMat[p].prob, condorSet[p], "Wins:", playMat[p].wins, "Losses:", playMat[p].losses, "Total Games:", playMat[p].game)
        p+=1

#Modified function above to apply to ELO rating
def printEloMatrix(playMat, condorSet): #Requires List of Players and Matrix to be printed
    size = len(condorSet)
    p = 0
    print("ID|RATING|1   2   3   4   5   6   7   8   9   10   11   12   13   14   15...")
    while p < size:
        print(playMat[p].id+1,")",playMat[p].elo, condorSet[p], "Wins:", playMat[p].wins, "Losses:", playMat[p].losses, "Total Games:", playMat[p].game)
        p+=1

#XP Game Logic
def gameXP(players, condor):  #Requires list of players in game and Matrix to send score to
    win = (randrange(0, 101)) #randomly picked number
    #win = 32
    stats=[]
    numPlayers = len(players)
    p = 0
    while p < numPlayers:
        players[p].guess=(abs(win-players[p].prob))
        stats.append(players[p].guess)
        p+=1
    stats.sort()
##    winner = stats[0]  ##Uncomment to see Winning (shortest) Distance and/or the Winning Number to be guessed
##    print("Winning Number:", win)
    awardPlayer(stats[0], players, condor)
    

##Award Player makes changes to condor to reflect outcomes
def awardPlayer(win, Pset, Cmat): #Requires winning value, list of players in game, and Matrix to set scores in
    s = len(Pset)
    p = 0
    while p < s:
        if Pset[p].guess == win:
            ##Verbosity
            #print("Player", Pset[p].id +1, "wins!")
            #print("Win=", win)
            #Pset[p].wins+=1
            idx=0
            while idx < s:
                if idx != p:
                    Cmat[Pset[p].id][Pset[idx].id]+=1
                    Pset[p].wins+=1
                    Pset[idx].losses+=1
                idx+=1
        p+=1

##Create Combinations of players for the actual matches
def chooseXPlayersFrom(x,lst,gameIdx, numGames): #Num of Players to choose, List to choose from, What game we're on, and Total Number of Games (Yes, this matters.)
    choice=set() #No duplicates
    stats=[]
    lngth = len(lst)
    if x >= lngth: #Shortcut (if you want all the players there's no need for this)
        choice = lst
    else:
        for each in lst:
            stats.append([each.game, each.id])
            stats.sort(reverse=True)
        while len(choice) < x:
            for each in lst:
                each.rand = randrange(0,lngth) #Random Choice
            for each in lst:
                if each.game == stats[-1][1]: #Prioritize ones with least games played
                    choice.add(each)
                if each.rand == 1 and each.game <= gameIdx:  
                   choice.add(each)   

    while len(choice) > x: #No extras.  Prioritize removal of those with most games played
        for each in list(choice): 
            if (each.game > (numGames//x) and each.game > gameIdx and each.game > calculateMeanGames(lst)) or each.id == stats[0][1]:
                choice.remove(each)
        if len(choice) > x: #If everyone's not played too many games, just pop off a random one
            choice.pop()
            
    for each in choice:
        each.game+=1 #Increment game count to help future choices
##        print(each.id+1) #Uncomment to see choices for each game
    return list(choice)
        
##Calculate win/loss differences to determine winners
def getWinners(playMat, playersPerGame):  #Requires the List of players and players per game
    stats = []
    for each in playMat:
        stats.append([each.wins - each.losses, each.id+1])
    stats.sort(reverse=True)
##    print("----WIN-LOSS BY RANK----")
##    print(stats)
##    print("----TOP PLAYERS----")  ##Choose Either this or the next print loop to be commented out
    for each in stats:
        if each[0] > calculateAverage(playMat):
            pass
##            print("Player", each[1], "Win Percentage:", calculateWinPercent(playMat[each[1]-1], playersPerGame))
##    print("----GUESSES AND WIN PERCENTAGES----")
##    print("Player 2 Win Percentage:", calculateWinPercent(playMat[1], playersPerGame))
    for each in stats:
        pass
##        print("Player", each[1], "Guess:", playMat[each[1]-1].prob, "Win Percentage:", calculateWinPercent(playMat[each[1]-1], playersPerGame))
##    print("----WINNERS----- And their Guess")
##    print("1st Place: Player", stats[0][1], "(", playMat[stats[0][1]-1].prob,")")
##    print("2nd Place: Player", stats[1][1], "(", playMat[stats[1][1]-1].prob,")")
##    print("3rd Place: Player", stats[2][1], "(", playMat[stats[2][1]-1].prob,")")

#Calc the number of games played on Avrg:
def calculateMeanGames(playMat):  #Only requires the list of players
    mean = 0
    for each in playMat:
        mean += each.game
    mean = mean//len(playMat)
    return mean

#Calc the average performance of players
def calculateAverage(playMat):  #Only requires the list of players
    mean = 0
    for each in playMat:
        mean += (each.wins - each.losses)
    mean = mean//len(playMat)
    return mean

#Calc the chance of a player winning
def calculateWinPercent(player, playersPerGame): #Requires the player and the number of players per game
    percy = (((player.wins/player.game)*100)//1)
    if percy > 100:
        return 100.0
    else:
        return percy

##MainFunction
def smallTournament(numPlayers, numGames, numPlayersPerGame):  #Self-explanatory
    playMat=[] #EmptyIt
    condorSet=[] #EmptyIt
    createXPlayers(numPlayers, playMat, 25) #FillIt

##COMMENT THIS OUT IF YOU WANT A TRULY FAIR/RANDOM GAME
##    playMat[0].cheater = True #Player 1 becomes a "genius" who never loses (all losses are ties)
##    playMat[0].prob = 42
##    playMat[1].prob = 52
##    playMat[2].prob = 29
##    playMat[3].prob = 69
##    playMat[4].prob = 92
##    playMat[5].prob = 7
##    playMat[6].prob = 22
##    playMat[7].prob = 54
##    playMat[8].prob = 72
##    playMat[9].prob = 0
##    playMat[10].prob = 89
##    playMat[-1].prob = 190 #The last player always guesses 1000, which isn't even on the list! (always loses)
##    playMat[1].cheater = "true" #Player 2 has approximate knowledge of many things (percentage is whatever I want)

    createMatrix(numPlayers, condorSet) #FillIt
    i = 0
    while i < numGames:
        gameXP(chooseXPlayersFrom(numPlayersPerGame,playMat, i, numGames), condorSet)
        #printMatrix()
        #print("-------------")
        i+=1
    printMatrix(playMat, condorSet)
    getWinners(playMat, numPlayersPerGame)
    stats = []
    for each in playMat:
        stats.append([each.game, each.id])
    stats.sort(reverse=True)
    mean = calculateMeanGames(playMat)
##    print("----------------")
##    print("Mean Games Played:", mean)
##    print("Most Games Played:", stats[0][0], "(+", stats[0][0]-mean,")")
##    print("LEst Games Played:", stats[-1][0], "(-", mean-stats[-1][0],")")
##    print("----------------")

##############################################################################

##RATINGS SIMULATION
#Calculate Odds of Winning based purely on Ratings
def calculateElos(players):
    p = 0
    probs = []
    for each in players:
        probs.append([0, each.id, each.rate]) #Rate is an afterthought of refactoring so I put it as the last item
    while p < len(players):
        idx = 0
        while idx < len(players):
            probs[p][0]+=(players[idx].rate)
            idx+=1
        p+=1
    for each in probs:
        each[0] = each[2]/(each[0])
    return probs

def gameSim(playerElos, players, condorSet):
    win = (randrange(0, 100)/100) #randomly picked number
##    print("Win:", win)
    stats=[]
    mark = 0
    for each in playerElos:
        mark+=each[0]
        stats.append(mark)
##    print(stats)
    numPlayers = len(players)
    p = 0
    while p < numPlayers and win > stats[p]:
        p+=1
    winner = playerElos[p][1]
##    print("Winner:",winner)
    simAward(winner, playerElos, players, condorSet)

def simAward(winIdx, elosIds, players, matrix): #Takes the Player Index of the winner, the list made by CalcElos, complete list of all players, and matrix
##    for each in elosIds:
##        if winIdx == each[1]:
##            players[each[1]].wins += 1
##        else:
##            players[each[1]].losses += 1
    s = len(elosIds)
    p = 0
    while p < s:
        if elosIds[p][1] == winIdx:
            players[winIdx].wins+=1
            idx=0
            while idx < s:
                if idx != p:
                    matrix[players[winIdx].id][players[elosIds[idx][1]].id]+=1
                    players[elosIds[idx][1]].losses+=1
                idx+=1
        p+=1

def getEloWinners(playMat, playersPerGame):  #Requires the List of players and players per game
    stats = []
    for each in playMat:
        stats.append([each.W, each.id+1])
    stats.sort(reverse=True)
##    print("----[WINS, PLAYER] BY RANK----")
##    print(stats)
##    print("----PLAYERS AND WIN PERCENTAGE----")  ##Choose Either this or the next print loop to be commented out
##    for each in stats:
##        if each[0] > calculateAverage(playMat):
##            print("Player", each[1], "Win Percentage:", calculateWinPercent(playMat[each[1]-1], playersPerGame))
##    print("----ELOS AND CONDORCET WINS----")
    for each in stats:
        pass
##        print("Player", each[1], "Rating:", playMat[each[1]-1].elo, "Defeated Players:", playMat[each[1]-1].W)

def simulate(numPlayers, numGames, numPlayersPerGame, disparity, fileName="", timeLimit=1000): #Same as Main Function
    start = time()
    timeTaken = 0
    playMat = [] #Empty it
    condorSet = [] #Empty it
    createXPlayers(numPlayers, playMat, disparity) #Fill it
    createMatrix(numPlayers, condorSet) #Fill it
    i = 0
    
    ##WRITES OUTPUT OF RMSE TO FILES FOR GRAPHING PURPOSES
    print(fileName)
    w = open(fileName, mode = 'w')
    while i < numGames and timeTaken < timeLimit:
        gameSim(calculateElos(chooseXPlayersFrom(numPlayersPerGame,playMat, i, numGames)), playMat, condorSet) #Magic!
        i+=1
        reportFrequency = generateReportFrequency(i)
        if i%reportFrequency == 0: #Every %# games, stop and write the RMSE and number of games to a file called "condormse" Comment out if not graphing
            condorGetWinners(condorSet, playMat)
            w.write(str(i))
            w.write(", ")
            w.write(str(RMSE(playMat, i)))
            w.write("\n")
            timeTaken = time() - start
    w.close()
##    printEloMatrix(playMat, condorSet)
    condorGetWinners(condorSet, playMat)
    getEloWinners(playMat, numPlayersPerGame)
    stats = []
    for each in playMat:
        stats.append([each.game, each.id])
    stats.sort(reverse=True)
    mean = calculateMeanGames(playMat)
##    print("----------------")
##    print("Mean Games Played:", mean)
##    print("Most Games Played:", stats[0][0], "(+", stats[0][0]-mean,")")
##    print("Least Games Played:", stats[-1][0], "(-", mean-stats[-1][0],")")
##    print("----------------")

def generateReportFrequency(i):
    if i <= 10:
        return 1
    elif i <= 100:
        return 5
    elif i <= 1000:
        return 50
    elif i <= 10000:
        return 250
    else:
        return 1000

##CONDORCET WINNER SYSTEM##
def condorGetWinners(matrix, players):
    clearCondor(players)
    i = 0
##    print("CONDORCET STATS")
    while i < len(matrix):
        j = 0
        while j < len(matrix):
            if i != j:
                if matrix[i][j] - matrix[j][i] > 0:
                    players[i].W+=1
                elif matrix[i][j] - matrix[j][i] < 0:
                    players[i].L+=1
                else:
                    players[i].T+=1
            j+=1
        i+=1
##        print("-----------")
##        print("Player", i)
##        print("Defeated", players[i-1].W, "other players.")
##        print("Lost to", players[i-1].L, "other players.")
##        print("Tied with", players[i-1].T, "other players.")
            
def clearCondor(players): #Clears wins, losses, and ties so that the above function doesn't stack
    for each in players:
        each.W = 0
        each.L = 0
        each.T = 0

####ROOTMEANSQUAREERRORTESTING#####
def RMSE(players, numGames):
    #Get Actual Ratings
    ACT = []
    for each in players:
        ACT.append([each.elo, each.id])
    ACT.sort(reverse=True)
    #ACTual Ratings are now Stored in ACT based on their index

    #Rank based on calculated CONDORCET WINS
    COMP = []
    for each in players:
        if each.game != 0:
            COMP.append([each.W, each.id])
        else:
            COMP.append([0, each.id])
    COMP.sort(reverse=True)
    #COMPuted Wins are stored in COMP, ranked by their index

    rmse = 0
    a = 0
    while a < len(ACT):
        c = 0
        while c < len(COMP):
            if ACT[a][1] == COMP[c][1]:
                rmse+=((a-c)**2) #Sums the square of each ranking difference 
            c+=1
        a+=1

    rmse = sqrt(rmse/len(players))#Divide by numPlayers and Square Root it

    #Fancy printing for feedback (comment out for faster execution)
##    print("-------ACTUAL-COMPUTED-------")
##    idx = 0
##    while idx < len(players):
##        print("Rank", idx+1, ":", ACT[idx][1]+1,"-", COMP[idx][1]+1)
##        idx+=1
##    print("TOTAL GAMES:", numGames)
##    print("RMSE:", rmse)
    return rmse
    

##DEBUGGING    
##a = player()
##b = player()
##c = player()
##d = player()
##a.id = "a"
##b.id = "b"
##c.id = "c"
##a.elo = 2100
##b.elo = 1200
##c.elo = 1300
##d.elo = 1000
##players = [a,b,c,d]
##gameSim(calculateElos(players))

##simulate(100, 100000, 5, 20, "test.txt", 1000)
#smallTournament(10, 2000, 4)

