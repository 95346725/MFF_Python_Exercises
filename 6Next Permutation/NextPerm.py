#A permutation on N element set (of natural numbers {1, 2, ..., N} is any ordering of elements of this set. The underlying set has N! (mutually different) permutations. All permutations can be lexicographically ordered, i.e., in such the same way as the words in a dictionary are. Ordering of two particular permutations is given by the first element (from the beginning) where these permutations differ. Lexicographically first permutation is (1, 2, ..., N), the last one is (N, N-1, ..., 2, 1).

#The first input line contains one positive integer N which is at most 100. The second line contains particular permutation on a set {1, 2, ..., N} while individual numbers are separated by spaces.

#For a given permutation the program outputs directly the next permutation. If such a permutation does not exist, it outputs the word NEEXISTUJE

#Example input:
#6
#1 3 6 2 5 4

#Appropriate output:
#1 3 6 4 2 5


n = int(input())
vstup = str.split(input())

cislo= []
for i in range(0, n): 
    ele = int(vstup[i]) 
  
    cislo.append(ele)

for i in range(n-1,0,-1): #pozadu
    if cislo[i] > cislo [i-1]: #vymenenim vetsich dopredu udelame vetsi cislo
        break
if i == 1 and cislo[i] <= cislo[i-1]: #do konce = druhe cislo
	print ("NEEXISTUJE") #543210
else:
	#i = 4
	x = cislo[i-1] #2, 1
	toBeNejmensi = i
	#najdi nejmensi ze zbytku a dej ho na i-1
	for j in range (i+1,n): #6 pozice #mezi cislama za zmenou vcetne najdi nejmensi
		if cislo[j] > x and cislo[j] < cislo[toBeNejmensi]: #4>2 and 4<5
			toBeNejmensi = j #5
	cislo[toBeNejmensi],cislo[i-1] = cislo[i-1], cislo[toBeNejmensi] #najdu cislo, ktere je dalsi v poradi zleva (nejmensi)-> 1 3 6 2 4 5, 258761           4,2 = 2,4

	srovnane=cislo[:i]
	konec = []
	konec = sorted(cislo[i:])

	for i in range(len(konec)):
		srovnane.append(konec[i])

	print(*srovnane)