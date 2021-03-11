#From the file sachovnice.txt read the description of a chessboard and write out the length of a king's shortest path to a destination square. Write the output to standard output (i.e., the terminal).
# The chessboard is described in the following way. The description starts with two lines containing positive integers x and y indicating the number of rows and columns of the given chessboard (respectively). 
# These numbers are followed by x lines, each consisting of y letters describing individual positions with the following meaning:

#dot: we can access this position,
#X (uppercase letter), this position is forbidden,
#S (also uppercase), the king starts here,
#C (also uppercase), the destination position.
#If there exists no path between the given pair of positions, write -1.

#Example:
#Input:
#4
#4
#X.XS
#.X.X
#.XXX
#..C.
#Output:
#6


sachovnice = open('sachovnice.txt', 'r') 
radky = sachovnice.read().splitlines()

vyska = int(radky[0])
sirka = int(radky[1])
sachovnice = radky[2:]
x = -1
for i in sachovnice:
    start_y = i.find('S')
    x += 1
    break
start_x = x

x2 = -1

for i in sachovnice:
    end_y = i.find('C')
    x2 += 1
    break
end_x = x2


for i in range(len(sachovnice)):
	temp = []
	for j in sachovnice[i]:
		temp.append(j)
	sachovnice[i] = temp
		



#smery
dx = [ 0, -1, -1, -1, 0, 1, 1, 1 ] 
dy = [ 1, 1, 0, -1, -1, -1, 0, 1 ] 


def NajdiMin(mat,x,y,r,c,end_x,end_y): 	

	q = []
	q.append([x, y]) 
	mat[x][y] = 0
	while(len(q) > 0): 
		x = q[0][0] 
		y = q[0][1] 
		q.pop(0) 
		appended = False
		for i in range(8): 
			a = x + dx[i] 
			b = y + dy[i] 
			if(a < 0 or a >= r or
			b >= c or b < 0 or
			mat[a][b] == 'X'): 
				continue
			if(mat[a][b] == 'C'):
				mat[a][b] = mat[x][y] + 1
				return mat[a][b]
			if(mat[a][b] == '.'): 
				mat[a][b] = mat[x][y] + 1
				q.append([a, b]) 
				appended = True
	return -1

print(NajdiMin(sachovnice,start_x,start_y,vyska,sirka,end_x,end_y)) 