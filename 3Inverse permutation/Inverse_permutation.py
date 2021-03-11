#A permutation of the integers from 1 to N describes a way to shuffle those numbers.

#Here is a permutation of the integers {1, 2, 3, 4, 5, 6}:

#1 -> 1
#2 -> 3
#3 -> 6
#4 -> 2
#5 -> 5
#6 -> 4
#The inverse of a permutation is a shuffling that returns each integer to its original position.

#Here is the inverse of the above permutation:

#1 -> 1
#2 -> 4
#3 -> 2
#4 -> 6
#5 -> 5
#6 -> 3
#Your program should read a series of numbers from standard input. The first number is a positive integer N <= 100. The following numbers represent a permutation of the set of natural numbers {1, 2, ..., N} and are separated by spaces. All input numbers appear on a single line.

#Determine the inverse permutation and write it to a single line of standard output, with numbers separated by spaces.

#Example

#input:

#6 1 3 6 2 5 4
#output:

#1 4 2 6 5 3


vstup = input()
vstup_spl = vstup.split()

for i in range(len(vstup_spl)):
    vstup_spl[i] = int(vstup_spl[i])


N = vstup_spl[0]
permutace = vstup_spl[1:]
poradi = []

for j in range(0,N):
    for k in range(0,N):
        if(permutace[k] == j+1):
            poradi.append(k+1)
            break
print(*poradi)