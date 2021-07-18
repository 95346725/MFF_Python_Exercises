#Young tabuleaux come in the following way: Considering a number n, we are forming the following weird tables consisting of n cells so that each table consists of some number of rows and columns. For each consecutive pair of rows i and i+1, it holds that the former row is at least as long as the next one (i.e., it has at least as many cells as the latter one). For the columns, the same assumption applies. Now, we want to know for a given number n, how many Young tableaux can we build with n cells.

#Write (and debug) a program that reads from the standard input a number n and outputs (to the standard output) the number of Young tableaux with n cells.

#Example:
#Input:
#5

#Output:
#7

k=0
def deleni(i, n): 
	global k
	if (n == 0): 
		k+=1
		return 
	for j in range(i, n+1): 
		deleni(j, n-j) 


n = int(input())
deleni(1, n) 

print(k)