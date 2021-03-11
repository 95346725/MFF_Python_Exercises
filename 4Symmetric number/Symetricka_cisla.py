#Design (and implement) a function testing whether an integer given in a decimal notation is symmetric (i.e., whether it is a palindrom or, equivalently, whether we obtain the same number when reading it from the end to the beginning).

#The input of a program is formed by a sequence of natural numbers ended by 0 (zero is already not a member of the sequence). Each number is on a separate line. Output is formed by numbers whose notation is symmetric. Numbers forming the output are separated by a (single) space (i.e., all of them are on the same line).

#A number symmetric up to zeroes at the end (e.g., 100) is not symmetric! All the numbers fit into 32bit integer.

#Example:

#Input

#15651
#8521
#3647
#123321
#51215
#3000
#0

#Output

#15651 123321 51215


import sys
prvniIterace = True
listVytiskni = []
while True:
    n = input()
    if n == '0':
        break
    n_int = int(n)
    n_str = str(n)
    n_str_len = len(n_str)
    if(n_str_len%2 == 0):
        for i in range(len(n)):
            porovnani = int(n_str[i])
            posledni = n_int%10
            if (porovnani != posledni):
                break
            else:
                  n_int = n_int//10
            if(i == n_str_len/2-1):
                listVytiskni.append(n)
                break
    elif(n_str_len == 1):
        listVytiskni.append(n)
    else:

        for i in range(len(n)):
            porovnani = int(n_str[i])
            posledni = n_int%10
            if (porovnani != posledni):
                break
            else:
                  n_int = n_int//10
            if(i == (int(n_str_len)+1)/2-2):
                listVytiskni.append(n)
                break
print(*listVytiskni)    