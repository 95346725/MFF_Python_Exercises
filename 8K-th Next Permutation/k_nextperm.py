#The first input line contains integers N and K. The second input line contains a permutation of numbers 1 .. N. The output shall consist of a permutation (of numbers 1 .. N) which is k positions behind the input one (w. r. t. lexicographical ordering). You may expect that 1<= N <=13 and that the value K can be represented as a longint (but it may be also negative). Also you may expect that all the inputs (and even outputs) are correct (i.e., well defined). Example 1:
#Input:
#5 1
#1 2 3 5 4

#Output:
#1 2 4 3 5

#Example 2:
#Input:
#12 -200000000
#12 11 10 9 8 7 6 5 3 4 1 2

#Output:
#7 12 10 9 6 4 2 3 5 8 1 11


prvni = str.split(input())
n = int(prvni[0])
k = int(prvni[1])
vstup = str.split(input())

cisloZadane= []
for i in range(0, n): 
    ele = int(vstup[i])  
    cisloZadane.append(ele)

def NextPerm(cislo,n):
	for i in range(n-1,0,-1): #pozadu
		if cislo[i] > cislo [i-1]: #vymenenim vetsich dopredu udelame vetsi cislo
			break
	x = cislo[i-1]
	toBeNejmensi = i
	#najdi nejmensi ze zbytku a dej ho na i-1
	for j in range (i+1,n): #6 pozice #mezi cislama za zmenou vcetne najdi nejmensi
		if cislo[j] > x and cislo[j] < cislo[toBeNejmensi]:
			toBeNejmensi = j
	cislo[toBeNejmensi],cislo[i-1] = cislo[i-1], cislo[toBeNejmensi] #najdu cislo, ktere je dalsi v poradi zleva (nejmensi)-> 1 3 6 2 4 5, 258761

	cislo[i:] = sorted(cislo[i:])
	return cislo

#13524 -> 13452 -> 13425
def PrevPerm(cislo, n): 
	for i in range(n-1,0,-1): #pozadu
		if cislo[i] < cislo [i-1]: #vymenenim vetsich dopredu udelame vetsi cislo
			break
	#i = 4
	x = cislo[i-1] #velke cislo
	toBeNejvetsi = i
	#najdi nejvetsi ze zbytku a dej ho na i-1
	for j in range (i+1,n):
		if cislo[j] < x and cislo[j] > cislo[toBeNejvetsi]:
			toBeNejvetsi = j 
	cislo[toBeNejvetsi],cislo[i-1] = cislo[i-1], cislo[toBeNejvetsi] #4,5 -> 5,4
	cislo[i:] = sorted(cislo[i:],reverse = True)
	return cislo

def kNextPerm(cislo, n, k):
	global cisloZadane
	if(k>0):
		for l in range(k):
			NextPerm(cisloZadane,n)
			#cisloZadane = srovnane
	elif(k<0):
		for l in range(-k):
			PrevPerm(cisloZadane,n)
			#cisloZadane = srovnane
	else:
		return cisloZadane

kNextPerm(cisloZadane,n ,k)
print(*cisloZadane)