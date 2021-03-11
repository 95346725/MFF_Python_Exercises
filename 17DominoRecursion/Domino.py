#Write a program that finds a longest row that can be built from a given domino-stones and prints its length. Dominoes contain always two numbers. 
#Mind the fact that we do not prescribe which number is the left one and which the right one.

#Dominoes are labeled by (pair of) numbers 1..38, maximum number of dominoes is 16.

#On the input, there are several numbers of this form: First number k tells us number of dominoes. It is followed by 2k where each consecutive pair describes numbers on particular domino-stone.

#For a sample input:

#5  1 2  1 2  2 3  2 17  2 17
#the appropriate output is:

#5
#I.e. longest row we can build using the described stones, is (e.g.) 2-1 1-2 2-17 17-2 2-3 and it has length 5.

import sys

def najdi(seznamKostek, tempList):
    maximum = len(tempList)

    for pozice, domino in enumerate(seznamKostek):
        if maximum == len(seznamKostek) + len(tempList): #mame nejdelsi
            break 

        zbyvajici = seznamKostek[:pozice] + seznamKostek[pozice+1:] #vyjmuti stavajiciho kousku

        if tempList:
            obraceneDomino = domino[::-1] 
            head, tail = tempList[0], tempList[-1]
            ##pripojime k zacatku
            if domino[1] == head[0]:
                maximum = max(najdi(zbyvajici, [domino] + tempList), maximum) #update maxima, pokud je maximum z rekurze vetsi
            elif obraceneDomino[1] == head[0]:
                maximum = max(najdi(zbyvajici, [obraceneDomino] + tempList), maximum)
            #pripojime ke konci
            elif domino[0] == tail[1]:
                maximum = max(najdi(zbyvajici, tempList + [domino]), maximum)
            elif obraceneDomino[0] == tail[1]:
                maximum = max(najdi(zbyvajici, tempList + [obraceneDomino]), maximum)
        else:
            maximum = max(najdi(zbyvajici, [domino]), maximum) #nezaradili jsme domino, zkusime ho pouzit jak novy zacatek

    return maximum


def cteckaKostka():
    global counter
    novyZnak = " "
    #prvni cislo
    while novyZnak == " " or novyZnak == "\n":
        novyZnak = sys.stdin.read(1)
    dalsiZnak = sys.stdin.read(1)
    if dalsiZnak != " " and dalsiZnak != "\n":
        a = int(novyZnak)*10+int(dalsiZnak)
    else:
        a = int(novyZnak)

    #druhe cislo
    novyZnak = " "
    while novyZnak == " " or novyZnak == "\n":
        novyZnak = sys.stdin.read(1)
    dalsiZnak = sys.stdin.read(1)
    if dalsiZnak != " " and dalsiZnak != "\n":
        b = int(novyZnak)*10+int(dalsiZnak)
    else:
        b = int(novyZnak)
    return (a,b)



prvni = " "
while prvni == " " or prvni == "\n":
    prvni = sys.stdin.read(1)
druhy = sys.stdin.read(1)
if druhy != " " and druhy != "\n":
    n = int(prvni)*10+int(druhy)
else:
    n = int(prvni)
seznamKostek = []
counter = 0
if n == 0:
    print(0)
else:
    while counter<n:
        seznamKostek.append(cteckaKostka())
        counter+=1
    print(najdi(seznamKostek, []))