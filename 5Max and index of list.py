#The program is given a sequence of N positive integers, where N <= 1000. Find the largest number contained in the sequence and write out the position of each of its occurrences.

#Input: The first input line contains N, the number of elements in the sequence (1 <= N <= 1000). The second line contains N integers separated by spaces.

#Output: On the first output line, write the largest number contained in the sequence. On the second output line, write the position of each of its occurrences, separated by spaces.

#Example:

#input:

#7
#568 1 546 84 568 215 546
#output:

#568
#1 5

delka = input()
vstup = input()
indexMax = []
vstup_sep = vstup.split()
for i in range(0,len(vstup_sep)):
    vstup_sep[i] = int(vstup_sep[i])
maxVstup = max(vstup_sep)
print(maxVstup)
for j in range(0,len(vstup_sep)):
    if(maxVstup == vstup_sep[j]):
        indexMax.append(j+1)
print(*indexMax)
