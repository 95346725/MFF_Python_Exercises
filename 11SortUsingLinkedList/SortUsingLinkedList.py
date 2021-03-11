#The input consists of (uncertain) number of integers. Individual numbers may be separated either with space-characters or with the ends of lines. Read the individual numbers and output them ordered ascendently. The end of input can be recognized using our well-known EOF function (or by an empty line).

#Example:
#Input:
#5 1 3 5 4 6 2

#Output:
#1 2 3 4 5 5 6

#Please, do not use dynamic data structures already implemented in Python (like list or dictionaries). Implement a linked list yourself.


import sys
class Node:
    def __init__(self, hodnota=None, next = None):
        self.hodnota = hodnota
        self.next = next
    def pridejZa(self, radek):
        if self.hodnota == None:
            self.hodnota = radek
            self.next = None
            return
        while self.next is not None:
            self = self. next
        pridat = Node(radek, None)
        self.next = pridat
        return

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
        if stavajici.hodnota > data: # v pripade ze pridavame nejmensi cislo
            n = Node()
            n.hodnota = data
            n.next = stavajici
            self.head = n
            return
        while stavajici.next is not None:
            if stavajici.next.hodnota > data: #ted je next vetsi nez hodnota, chceme dat data pred next
                break
            stavajici = stavajici.next
        n = Node()
        n.hodnota = data
        n.next = stavajici.next #stavajici.next ma uz vetsi hodnotu
        stavajici.next = n # přepsat dalši prvek stavajiciho i s nove pridanym
        return

    def printList(self):
        temp = self.head 
        while(temp): 
            print (temp.hodnota, end = " ")
            temp = temp.next
        print()


class SpojovaCtecka:
    Konec = False
    NovaCislice = ""
    def PrectiCislo(self):
        self.NovaCislice = sys.stdin.read(1)
        if self.NovaCislice == "\n":
           self.Konec = True
        while self.NovaCislice == " ":
            self.NovaCislice = sys.stdin.read(1)
            if self.NovaCislice == "\n":
                return 'prazdny'
        start = True
        zapor = False
        temp = None
        while temp == None and self.NovaCislice == " ":
            self.NovaCislice = sys.stdin.read(1)
        while self.NovaCislice != " " and self.NovaCislice != "\n":
            if self.NovaCislice == "-":
                zapor = True
                self.NovaCislice = sys.stdin.read(1)
            if start:               
                temp = int(self.NovaCislice)
                start = False
                self.NovaCislice = sys.stdin.read(1)
                continue
            temp = 10*temp + int(self.NovaCislice)
            self.NovaCislice = sys.stdin.read(1)
        if temp != None:
            if zapor:
                return -temp
            else:
                return temp


    def PrectiRadku(self):
        tempSpojovy = SpojovySeznam()
        while self.NovaCislice != "\n":
            samostatneCislo = self.PrectiCislo()
            if samostatneCislo == "prazdny":
                samostatneCislo = self.PrectiCislo()
            tempSpojovy.pridejNode(samostatneCislo)
        return tempSpojovy


    def SpojVsechno(self):
        tempFinal = Node()
        while self.Konec == False:
            samostatnaRadka = self.PrectiRadku()
            if self.Konec == True:
                return tempFinal
            tempFinal.pridejZa(samostatnaRadka)
            self.NovaCislice = None
        return tempFinal



akce = SpojovaCtecka()

finalSeznam = akce.SpojVsechno()


if finalSeznam.hodnota == None:
    exit
else:
    while finalSeznam != None:
        currentNode = finalSeznam.hodnota
        currentNode.printList()
        finalSeznam = finalSeznam.next