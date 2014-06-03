map = []
with open('matrix.txt') as file:
	for line in file:
		line = line.split(",")
		tempList = []
		for i in range(len(line)):
			tempList.append(line[i])
		map.append(tempList)

yLength = len(map)
xLength = len(map[0])

class node():

    def __init__(self, node, parent, gScore):
        self.node = node
        self.name = map[node[0]][node[1]]
        self.parent = parent
        self.gScore = gScore 

        
    def getFScore(self):
        y, x = self.node[0], self.node[1]
        score = self.gScore
        score += (yLength-y)*500
        score += (xLength-x)*500
        self.fScore = score

openList =[(0,0),]
closedList = []
openList[0] = node(openList[0], None, int(map[0][0]))
openList[0].getFScore()
    
def getLowest():
    lowest = 9999999999
    answer = ''
    for i in openList:
        if i.gScore < lowest:
            lowest = i.gScore
            answer = i
    return answer

def inClosedSet(n):
    for i in closedList:
        if i.node == n:
            return i

def inOpenSet(n):
    for i in openList:
        if i.node == n:
            return i

while len(openList) > 0:
    current = getLowest()
    closedList.append(current)
    openList.remove(current)
    if current.node == ((yLength-1, xLength-1)):
        print(current.gScore)
        break
    else:
        neighbors = []
        y = current.node[0]
        x = current.node[1]
        if y < yLength-1:
            neighbors.append((y+1, x))
        if x < xLength-1:
            neighbors.append((y, x+1))
        if y > 0:
            neighbors.append((y-1,x))
        if x > 0:
            neighbors.append((y, x-1))
        for neighbor in neighbors:
            tentativeGScore = current.gScore + int(map[neighbor[0]][neighbor[1]])
            if inClosedSet(neighbor):
                neighbor = inClosedSet(neighbor)
                if tentativeGScore < neighbor.gScore:
                    neighbor.parent = current
                    neighbor.gScore = tentativeGScore
                    openList.append(neighbor)
                    closedList.remove(neighbor)
            elif inOpenSet(neighbor):
                neighbor = inOpenSet(neighbor)
                if tentativeGScore < neighbor.gScore:
                    neighbor.parent = current
                    neighbor.gScore = tentativeGScore
            else:
                openList.append(neighbor)
                openList[-1] = node(openList[-1], current, tentativeGScore)
                openList[-1].getFScore()

input()

