#Write a program that merges two increasing sorted sequences into a single sorted sequence.

#The first line of standard input contains a positive integer N ≤ 10,000. The second line contains a sorted sequence of N integers. The third line contains a positive integer M ≤ 10,000. The fourth line contains a sorted sequence of M integers. All numbers in the sequences are separated by a single space.

#The program should write the merged sequence to standard output on a single line, with numbers separated by a space.

#All sequence elements will fit into a variable of type integer.
#Mergesort do puvodniho seznamu#

def mergesort(s,zac,kon,kopie):
    stred = (zac+kon)//2
    if zac < stred:
        mergesort(s,zac,stred,kopie)
    if stred+1<kon:
        mergesort(s,stred+1,kon,kopie)

    for r in range(zac,kon+1):
        kopie[r] = s[r]
    i = zac
    j = stred+1
    k = zac
    print("pocita se",zac,kon)
    print()
    while i <=stred and j <= kon:
        if kopie[i]<=kopie[j]:
            s[k] = kopie[i]
            i+=1
        else:
            s[k] = kopie[j]
            j+=1
        k+=1
    while i<=stred:
        s[k] = kopie[i]
        i +=1
        k +=1
    while j<=kon:
        s[k] = kopie[j]
        j +=1
        k +=1

a = [100,5,0,-20,4]
kopie = [None]*len(a)
mergesort(a,0,4,kopie)