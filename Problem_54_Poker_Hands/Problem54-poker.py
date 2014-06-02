values = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
player1 = 0
player2 = 0
allHands=[]
with open("poker.txt") as f:
    for line in f:
        line = line.split()
        newhands = [[],[]]
        for i in range(len(line)):
            if i<5:
                newhands[0].append(line[i])
            else:
                newhands[1].append(line[i])
        allHands.append(newhands)

def handValues(hands):
    hand1=[]
    hand2=[]
    for card in hands[0]:
        hand1.append(values[card[0]])
    hand1.sort()
    for card in hands[1]:
        hand2.append(values[card[0]])
    hand2.sort()
    currentHandValues =[hand1, hand2]
    return currentHandValues

def highestValue(handvalues):
    for i in range(len(handvalues[1])-1,-1,-1):
        if handvalues[0][i] > handvalues[1][i]:
            return 1
        if handvalues[1][i] > handvalues[0][i]:
            return 2
    print('Problem')

def straightFlush (hands, handvalues):
    f = flush(hands)
    s = straight(handvalues)
    if f == None or s == None:
        return None
    if f == 'both' and s == 'both':
        return highestValue(handvalues)
    if f == 'both':
        if s == 1:
            return 1
        if s == 2:
            return 2
    if s == 'both':
        if f == 1:
            return 1
        if f == 2:
            return 2
    if f == 1:
        if s == 1:
            return 1
    if f == 2:
        if s == 2:
            return 2
    return None
       
def fourOfaKind (hands):
    hand1, hand2 = False, False
    for i in set(hands[0]):
        if hands[0].count(i) == 4:
            hand1 = True
            hand1card = i
    for i in set(hands[1]):
        if hands[1].count(i) == 4:
            hand2 = True
            hand2card = i
    if hand1 == True and hand2 == True:
        if hand1card == hand2card:
            if sum(set(hands[0])) > sum(set(hands[1])):
                   return 1
            else:
                   return 2
        if hand1card > hand2card:
            return 1
        else:
            return 2
    if hand1 == True:
        return 1
    if hand2 == True:
        return 2
    return None

def fullHouse (hands):
    hand1, hand2 = False, False
    if len(set(hands[0])) == 2:
        for i in set(hands[0]):
            if hands[0].count(i) == 3:
                hand1 = True
                hand1card = i
    if len(set(hands[1])) == 2:
        for i in set(hands[1]):
            if hands[1].count(i) == 3:
                hand2 = True
                hand2card = i
    if hand1 == True and hand2 == True:
        if hand1card == hand2card:
            if sum(set(hands[0])) > sum(set(hands[1])):
                   return 1
            else:
                   return 2
        if hand1card > hand2card:
            return 1
        else:
            return 2
    if hand1 == True:
        return 1
    if hand2 == True:
        return 2
    return None

def flush(hands):
    suits1=[]
    suits2=[]
    for i in hands[0]:
        suits1.append(i[1])
    for i in hands[1]:
        suits2.append(i[1])
    suits1 = set(suits1)
    suits2 = set(suits2)
    if len(suits1) == 1 and len(suits2) == 1:
        return 'both'
    if len(suits1) == 1:
        return 1
    if len(suits2) == 1:
        return 2
    return None

def straight (handvalues):
    hand1, hand2 = False, False
    if handvalues[0][4] == handvalues[0][0]+4:
        hand1=True
    if handvalues[1][4] == handvalues[1][0]+4:
        hand2=True
    if len(set(handvalues[0])) <5:
        hand1=False
    if len(set(handvalues[1])) <5:
        hand2=False
    if hand1 and hand2:
        return 'both'
    if hand1:
        return 1
    if hand2:
        return 2
    return None

def threeOfaKind (hands):
    hand1, hand2 = False, False
    for i in set(hands[0]):
        if hands[0].count(i) == 3:
            hand1 = True
            hand1card = i
    for i in set(hands[1]):
        if hands[1].count(i) == 3:
            hand2 = True
            hand2card = i
    if hand1 == True and hand2 == True:
        if hand1card == hand2card:
            return highestValue(hands)
        if hand1card > hand2card:
            return 1
        else:
            return 2
    if hand1 == True:
        return 1
    if hand2 == True:
        return 2
    return None

def twoPairs (hands):
    hand1, hand2 = False, False
    hand1twos = []
    hand2twos = []
    hand1extra, hand2extra = 0,0
    if len(set(hands[0])) == 3:
        hand1 = True
        for i in set(hands[0]):
            if hands[0].count(i) == 2:
                hand1twos.append(i)
            else:
                hand1extra = i
    if len(set(hands[1])) == 3:
        hand2 = True
        for i in set(hands[1]):
            if hands[1].count(i) == 2:
                hand2twos.append(i)
            else:
                hand2extra = i
    hand1twos.sort()
    hand2twos.sort()
    if hand1 == True and hand2 == True:
        if hand1twos[1]  == hand2twos[1]:
            if hand1twos[0] == hand2twos[0]:
                if hand1extra > hand2extra:
                    return 1
                else:
                    return 2
            if hand1twos[0] > hand2twos[0]:
                return 1
            else:
                return 2
        if hand1twos[1] > hand2twos[1]:
            return 1
        else:
            return 2
    if hand1 == True:
        return 1
    if hand2 == True:
        return 2
    return None
    

def onePair (hands):
    hand1, hand2 = False, False
    handvalues=[[],[]]
    for i in hands[0]:
        if hands[0].count(i) == 2:
            hand1 = True
            hand1pair = i
        else:
            handvalues[0].append(i)
    for i in hands[1]:
        if hands[1].count(i) == 2:
            hand2 = True
            hand2pair = i
        else:
            handvalues[1].append(i)
    if hand1 == True and hand2 == True:
        if hand1pair == hand2pair:
            return highestValue(handvalues)
        else:
            if hand1pair > hand2pair:
                return 1
            else:
                return 2
    if hand1 == True:
        return 1
    if hand2 == True:
        return 2
    return None

def getwinner(hand):
    handvalues = handValues(hand)
    if straightFlush(hand, handvalues):
        return straightFlush(hand, handvalues)
    if fourOfaKind(handvalues):
        return fours(handvalues)
    if fullHouse(handvalues):
        return fullHouse(handvalues)
    if flush(hand):
        if flush(hand) == 'both':
            return highestValue(handvalues)
        else:
            return flush(hand)
    if straight(handvalues):
        if straight(handvalues) == 'both':
            return highestValue(handvalues)
        else:
            return straight(handvalues)
    if threeOfaKind(handvalues):
        return threeOfaKind(handvalues)
    if twoPairs(handvalues):
        return twoPairs(handvalues)
    if onePair(handvalues):
        return onePair(handvalues)
    return highestValue(handvalues)
        


for hand in allHands:
    print(hand)
    if getwinner(hand) == 1:
        print(1)
        player1 +=1
    elif getwinner(hand) == 2:
        print(2)
        player2 += 1
    else:
        print('problematend')
print(player1, player2)
input()

      


