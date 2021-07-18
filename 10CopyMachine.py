#Read a (possibly unbounded) number of integers (32bit integer). Each number is on a separate line. Output the whole input (at a standard output) twice - one sequence after another. For example the input
#100000
#2
#3
#4
#5
#produces an output:
#100000
#2
#3
#4
#5
#100000
#2
#3
#4
#5

import sys
Konec = False

class Node:
    def __init__(self, hodnota=None, next = None):
        self.hodnota = hodnota
        self.next = next


class SpojovySeznam:
    def __init__(self): 
        self.head = None 
 
    def pridejNode(self, data):
        stavajici = self.head
        if stavajici is None:
            n = Node() #nova node
            n.hodnota = data
            n.next = stavajici #None
            self.head = n
            return
        while stavajici.next is not None:
            stavajici = stavajici.next
        n = Node()
        n.hodnota = data
        n.next = stavajici.next #stavajici.next ma uz vetsi hodnotu
        stavajici.next = n # přepsat dalši prvek stavajiciho i s nove pridanym
        return

    def printList(self):
        temp = self.head 
        secondRound = False
        while(temp): 
            print (temp.hodnota, end = "\n")
            temp = temp.next
        if (temp is None):
            temp = self.head
            secondRound = True
        while(temp and secondRound):
            print (temp.hodnota, end = "\n")
            temp = temp.next

class Ctecka:
    def PrectiCislo(self):
        global Konec
        NovaCislice = sys.stdin.read(1)
        if NovaCislice == "\n":
            Konec = True
        start = True
        temp = None
        while NovaCislice != "\n":
            if start:        
                temp = int(NovaCislice)
                start = False
                NovaCislice = sys.stdin.read(1)
                continue
            temp = 10*temp + int(NovaCislice)
            NovaCislice = sys.stdin.read(1)
        return temp

#SpojovyList = SpojovySeznam()
#cteckaObjekt = Ctecka()

#while Konec == False:
#    cislo = cteckaObjekt.PrectiCislo()
#    if Konec == True:
#        break
#    SpojovyList.pridejNode(cislo)

SpojovyList = SpojovySeznam()

while True:
    try:
        cislo = input()
        if cislo == "":
            break
        SpojovyList.pridejNode(cislo)
    except EOFError:
        break

SpojovyList.printList()
