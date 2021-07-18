#A number is perfect if it is the sum of its proper positive divisors (i.e. including 1, excluding itself).
# For example, 6 is perfect, as 6 = 1 + 2 + 3, while 36 is not perfect, as the sum of its divisors is 1 + 2 + 3 + 4 + 6 + 9 + 12 + 18 = 55. 
# A number is a square if it is the second power (square) of some integer. We call a number a cube if it can be expressed as a third power, and so on. 
# Write a program that decides whether a given number is perfect, a square and/or a cube. Denote these properties by writing out the letters 'P', 'C' and/or 'K' (in this order),
#  respectively. ('C' and 'K' stand for the Czech words 'čtverec' and 'krychle'.)
#Example: Input: 64 Output: CK

vstup = int(input())
SumaDelitelu = 0
cislo = abs(vstup) 
if(vstup != 0 and cislo != 1):
    for i in range(1,cislo):
        if(cislo % i == 0):
            SumaDelitelu = SumaDelitelu + i
    if (SumaDelitelu == cislo or cislo == abs(1)):
        print("P")

    for i in range(1,cislo):
        if (vstup == i * i):
            print("C")
            break
     

    for i in range(1,cislo):
        if (cislo == i * i * i):
            print("K")
            break
elif(vstup == 0):
    print("C")
    print("K")
elif(vstup == -1):
    print("P")
    print("K")
elif(vstup == 1):
    print("P")
    print("C")
    print("K")