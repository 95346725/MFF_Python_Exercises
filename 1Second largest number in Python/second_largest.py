#The input consists of a sequence of integers ending with a -1 (which is not considered to be an element of the sequence).
#Write a program that finds and prints out the value of the second largest element in the sequence. The sequence is guaranteed to be long enough to contain a second largest element (in all testing data).



#_Input:_
#  1
#  2
#  3
#  7
#  7
#  -1


#_Output:_
#  7

n = int()
prvniIterace = True
druhaIterace = True
stredni = -1
while n != -1:
    n = int(input())
    if(n != -1):
        if(prvniIterace):
                nejvetsi = n
                prvniIterace = False
        elif(druhaIterace):
                if(n > nejvetsi):
                    stredni = nejvetsi
                    nejvetsi = n
                    druhaIterace = False
                elif(n==nejvetsi):
                    nejvetsi = n
                    stredni = n
                    druhaIterace = False
                else:
                    stredni = n
                    druhaIterace = False
        elif(n > nejvetsi):
               stredni = nejvetsi
               nejvetsi = n
        elif (n > stredni):
                    stredni = n
        elif (n == stredni):
                    stredni = n
                    nejvetsi = n
print(stredni)
