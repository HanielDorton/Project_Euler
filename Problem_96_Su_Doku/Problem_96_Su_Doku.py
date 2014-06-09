global solved
AllPuzzles = []
with open ('sudoku.txt') as file:
    for line in file:
        if line[0] == "G":
            AllPuzzles.append([])
        else:
            AllPuzzles[-1].append(line.strip())

class Square():

    def __init__(self, number, row, column, box):
        self.number = number
        self.row = row
        self.column = column
        self.box = box
        self.possibles = []

    def __str__(self):
        return("Number: " + str(self.number) + " Row: " + str(self.row) + " Column: " + str(self.column) + " Box: " + str(self.box) + " Pos: " + str(self.possibles))

def interpretPuzzle(Puzzle):
    currentSquares = []
    for row in range(len(Puzzle)):
        currentBox = 1
        if row > 2:
            currentBox = 4
        if row > 5:
            currentBox = 7
        for column in range(len(Puzzle[row])):
            box = currentBox
            if column > 2:
                box += 1
            if column > 5:
                box += 1
            currentSquares.append(Square(int(Puzzle[row][column]), row + 1, column + 1, box))
    return currentSquares

def getRemainingNumbers(square):
    numbers =[i + 1 for i in range(9)]
    for i in currentSquares:
        if i.row == square.row:
            if i.number in numbers:
                numbers.remove(i.number)
        elif i.column == square.column:
            if i.number in numbers:
                numbers.remove(i.number)
        elif i.box == square.box:
            if i.number in numbers:
                numbers.remove(i.number)
    return numbers
        

def findCertains():
    #this one clears out all squares that only have one option
    #either because they only have on number to use
    #or they have a number that no other square in one of their sections has
    #I continue running this method until it goes through without finding any
    
    #first recalculate possibilities for each square
    for i in currentSquares:
        if i.number == 0:
            i.possibles = getRemainingNumbers(i)
            #check if square only has on possible number
            if len(i.possibles) == 1:
                i.number = i.possibles[0]
                i.possibles = []
                return True
    #then check if any squares have a unique possible number
    for square in currentSquares:
        if square.number == 0:
            tempPossibles = []
            for i in currentSquares:
                if i != square:
                    if i.row == square.row:
                        for p in i.possibles:
                            if p not in tempPossibles:
                                tempPossibles.append(p)
                    elif i.column == square.column:
                        for p in i.possibles:
                            if p not in tempPossibles:
                                tempPossibles.append(p)
                    elif i.box == square.box:
                        for p in i.possibles:
                            if p not in tempPossibles:
                                tempPossibles.append(p)
            possiblesLeft = []
            for p in square.possibles:
                if p not in tempPossibles:
                    possiblesLeft.append(p)
            if len(possiblesLeft) == 1:
                square.number = possiblesLeft[0]
                square.possibles = []
                return True
    return False
"""
so if clearing out the certain ones doesn't solve the puzzle
I run this recurssive algorithm which just brute-forces the solution
looping through each square that still has possibles
for each square try the first possible
then check if that breaks anything
if it does try the next possible
if there are no more possibles then change the number back to zero
and return so that you go back to the previous number
if it works then go onto the next number
do this until the puzzle is solved
"""

def bruteForce(current):
    global solved
    for possible in currentSquares[current].possibles:
        if solved == True:
            return
        currentSquares[current].number = 0
        attempt = True
        for i in currentSquares:
            if i != currentSquares[current]:
                if i.row == currentSquares[current].row:
                    if i.number == possible:
                        attempt = False
                elif i.column == currentSquares[current].column:
                    if i.number == possible:
                        attempt = False
                elif i.box == currentSquares[current].box:
                    if i.number == possible:
                        attempt = False
        if attempt:
            if current == len(currentSquares) - 1:
                solved = True
                currentSquares[current].number = possible
                return                
            currentSquares[current].number = possible
            for i in range(current + 1, len(currentSquares)):
                if len(currentSquares[i].possibles) > 0:
                    bruteForce(i)
                    break
                if i == len(currentSquares) - 1:
                    solved = True
                    currentSquares[current].number = possible
                    return                    
    if current == len(currentSquares) - 1:
        solved == True
    if not solved:
        currentSquares[current].number = 0
    return
    


answer = 0
for i in range(len(AllPuzzles)):
    if i == i:
        currentSquares = interpretPuzzle(AllPuzzles[i])
        while True:
            if not findCertains():
                break
        for s in currentSquares:
            if s.number == 0:
                s.possibles = getRemainingNumbers(s)
        solved = True
        for square in currentSquares:
            if square.number == 0:
                solved = False
        if not solved:
            for square in range(0, len(currentSquares)):
                if currentSquares[square].number == 0:
                    bruteForce(square)
                    break
        for square in currentSquares:
            if square.number == 0:
                print("Problem: ", i)
        print("solved: ", i)
        sum= ''
        for i in range(3):
            sum += str(currentSquares[i].number)
        answer += int(sum)
print(answer)
        
                    

        
            




