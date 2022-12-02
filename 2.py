# day 2
# puzzle one

# open data file
input = open("2-data.txt", "r")
data = input.readlines()

# create empty lists for the opponent's moves and your moves, as well as your scores
oppMoves, yourMoves, scores = [], [], []

# split the data into two lists for the opponent's moves and your moves
for i in range(len(data)):
    oppMoves.append(data[i][0])
    yourMoves.append(data[i][2])

# function to check if you win
# returns 0 for lose, 3 for draw, 6 for win (as per the challenge)
def checkWin(oppMove, yourMove):
    # shifts yourMove to the left 23, bringing XYZ to ABC, making it easier to check if it's the same as oppMove
    if oppMove == chr(ord(yourMove) - 23):
        return 3
    elif oppMove == 'A' and yourMove == 'Z':
        return 0
    elif oppMove == 'C' and yourMove == 'Y':
        return 0
    elif oppMove == 'B' and yourMove == 'X':
        return 0
    else:
        return 6

# calculate score for each round
for i, x in enumerate(yourMoves):
    n = checkWin(oppMoves[i], yourMoves[i])
    if x == 'X':
        n += 1
    elif x == 'Y':
        n += 2
    elif x == 'Z':
        n += 3
    scores.append(n)

# calculate total score
print(sum(scores))

# puzzle two

# given the opponent's move and how the game needs to end, decide your move
def chooseMove(oppMove, yourMove):
    if oppMove == 'A':
        if yourMove == 'X':
            return 'Z'
        elif yourMove == 'Y':
            return 'X'
        elif yourMove == 'Z':
            return 'Y'
    elif oppMove == 'B':
        if yourMove == 'X':
            return 'X'
        elif yourMove == 'Y':
            return 'Y'
        elif yourMove == 'Z':
            return 'Z'
    elif oppMove == 'C':
        if yourMove == 'X':
            return 'Y'
        elif yourMove == 'Y':
            return 'Z'
        elif yourMove == 'Z':
            return 'X'

# replace yourMove with the results of chooseMove
for i, x in enumerate(yourMoves):
    yourMoves[i] = chooseMove(oppMoves[i], yourMoves[i])

# calculate score for each round
for i, x in enumerate(yourMoves):
    n = checkWin(oppMoves[i], yourMoves[i])
    if x == 'X':
        n += 1
    elif x == 'Y':
        n += 2
    elif x == 'Z':
        n += 3
    scores[i] = n

# calculate total score
print(sum(scores))