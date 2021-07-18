#From the file sach.txt read the description of a chessboard and write out the length of a knight's shortest path to a destination square. Write the output to standard output (i.e., the terminal). 
#The chessboard is described in the following way. The description starts with two lines containing positive integers x and y indicating the number of rows and columns of the given chessboard (respectively). 
#These numbers are followed by x lines, each consisting of y letters describing individual positions with the following meaning:

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


pohyby = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

sachovnice = open('sach.txt', 'r') 
sachovnice = sachovnice.read().splitlines()


x = -1
i = 0
while x == -1:
		radek = sachovnice[i]
		x = radek.find('S')
		i += 1

start_x = x
start_y = i-1


x = -1
i = 0
while x == -1:
		radek = sachovnice[i]
		x = radek.find('C')
		i += 1

end_x = x
end_y = i-1


for i in range(len(sachovnice)):
	temp = []
	for j in sachovnice[i]:
		temp.append(j)
	sachovnice[i] = temp


def NajdiMin(mat,x,y,end_x,end_y): 	

	q = []
	q.append([x, y]) 
	mat[x][y] = 0
	while(len(q) > 0): 
		x = q[0][0] 
		y = q[0][1] 
		q.pop(0) 
		appended = False
		for i in range(8): 
			a = x + pohyby[i][0] 
			b = y + pohyby[i][1]
			if(a < 0 or a >= 8 or
			b >= 8 or b < 0 or
			mat[a][b] == 'X'): 
				continue
			if(mat[a][b] == 'C'):
				mat[a][b] = mat[x][y] + 1
				return mat[a][b]
			if(mat[a][b] == '.'): 
				mat[a][b] = mat[x][y] + 1
				q.append([a, b]) 
				appended = True
	return 'NELZE'

print(NajdiMin(sachovnice,start_x,start_y,end_x,end_y)) 