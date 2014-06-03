import itertools
'''
"""This makes a big list of prime numbers, don't need it anymoer."""
def isprime(number):
    for digit in range(2,number):
        if number % digit == 0:
            return False
    return True

allprimefactors = []

for number in range(2,10000):
    if isprime(number):
        allprimefactors.append(number)
'''

allprimefactors = [2,]
def getprimefactors(number):
    primefactors= []
    while number > 1:
        originalnumber=number
        for pf in allprimefactors:
            if number == pf or number % pf == 0:
                number = number/pf
                primefactors.append(pf)
        if number == originalnumber:
            allprimefactors.append(originalnumber)
            primefactors.append(number)
            return primefactors
    return primefactors

def getallfactors(number):
    primefactors = getprimefactors(number)
    allfactors = []
    for a in range(1, len(primefactors)):
        for b in itertools.combinations(primefactors, a):
            allfactors.append(b)
    allfactors = list(set(allfactors))
    for factor in range(len(allfactors)):
        multiplied = 1
        for number in allfactors[factor]:
            multiplied *= number
        allfactors[factor] = multiplied
    allfactors = list(set(allfactors))
    return allfactors
            
number = 0
for i in range(1,100000):
    number+=i
    answer = len(getallfactors(number))
    print(number, answer)
    if answer > 497:
        print(number)
        break

input()



