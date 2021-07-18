#This program implements functions, which transform mathematical expressions to 3 different types of notation (postfix, infix, suffix), creates binary trees from these expressions, and evaluates the expressions

class Et:
	def __init__(self , value):
		self.value = value
		self.left = None
		self.right = None

def isOperator(c):
	if (c == '+' or c == '-' or c == '*'
		or c == '/' or c == '^'):
		return True
	else:
		return False


def isParenthesis(c):
	if (c == '(' or c == ')'):
		return True
	else:
		return False

#reads an expression in infix notation and transforms it to postfix
def in2post(infix):
	in_list = list(infix)
	final_list = []
	stack = []
	while len(in_list)>0:
		i = in_list.pop(0)
		if (i == '('):
			stack.append(i)
		elif (i == ')'):
			l = stack.pop()
			while l != '(':
				final_list.append(l)
				l = stack.pop() #posledni leva zavorka uz se tam neda
		elif(i == '-' or i == '+'):
			l = None
			addPar = False
			while (l != '(' and len(stack)>0):
				l = stack.pop() #posledni leva zavorka uz se tam neda
				if l == '(': 
					stack.append('(') #jeste jsme neuzavreli
					break
				else:
					final_list.append(l)
			stack.append(i)

		elif(i == '*' or i == '/'): # deleno nebo krat
			for k in range(len(stack)-1,0,-1): #odzadu
				if stack[k] == '(':
					break
				elif (stack[k] == '*' or stack[k] == '/'):
					final_list.append(stack[k])
					stack.pop(k)
			stack.append(i)
		else: #cislo
			final_list.append(i)
	while len(stack)>0:
		last = stack.pop()
		final_list.append(last)
	return ''.join(final_list)


# auxiliary function for infix to prefix transformation
def reverseInfix(expr):
    rev=""
    for i in expr:
        if i is '(':
            i=')'
        elif i is ')':
            i='('
        rev=i+rev
    return rev


#reads an expression in infix notation and transforms it to prefix
def in2pre(infix):
	rev = reverseInfix(infix)
	in_list = list(rev)
	final_list = []
	stack = []
	while len(in_list)>0:
		i = in_list.pop(0)
		if (i == '('):
			stack.append(i)
		elif (i == ')'):
			l = stack.pop()
			while l != '(':
				final_list.append(l)
				l = stack.pop() #posledni leva zavorka uz se tam neda
		elif(i == '-' or i == '+'):
			l = None
			addPar = False
			while (l != '(' and len(stack)>0):
				l = stack.pop() #posledni leva zavorka uz se tam neda
				if l == '(': 
					stack.append('(') #jeste jsme neuzavreli
					break
				else:
					final_list.append(l)
			stack.append(i)

		elif(i == '*' or i == '/'): # deleno nebo krat
			for k in range(len(stack)-1,0,-1): #odzadu
				if stack[k] == '(':
					break
				elif (stack[k] == '*' or stack[k] == '/'):
					final_list.append(stack[k])
					stack.pop(k)
			stack.append(i)
		else: #cislo
			final_list.append(i)
	while len(stack)>0:
		last = stack.pop()
		final_list.append(last)
	return ''.join(reversed(final_list))


#evaluates the expression given in prefix notation
def solvePre(soustava):
    if not soustava:
        return None
    naseCisla = []  
    for c in reversed(soustava): 
  
        # push operand to stack 
        if not isOperator(c): 
            naseCisla.append(int(c))
  
        else:  
            cislo1 = naseCisla.pop() 
            cislo2 = naseCisla.pop() 
  
            if c == '+': 
                naseCisla.append(cislo1 + cislo2) 
  
            elif c == '-': 
                naseCisla.append(cislo1 - cislo2) 
  
            elif c == '*': 
                naseCisla.append(cislo1 * cislo2) 
  
            elif c == '/': 
                naseCisla.append(cislo1 / cislo2) 
  
    return naseCisla.pop()

#puts postfix expression into binary tree data structure
def construct_post(postfix):
	stack = []

	# Traverse through every character of input expression
	for char in postfix :
		if not isOperator(char):
			t = Et(char)
			stack.append(t)
		else:
			# Pop two top nodes
			t = Et(char)
			t1 = stack.pop()
			t2 = stack.pop()			
			# make them children
			t.right = t1
			t.left = t2			
			# Add this subexpression to stack
			stack.append(t)

	# Only element will be the root of expression tree
	t = stack.pop()
	
	return t

#prints the expression given in prefix notation
def preorder(t):
	global pre_list
	if t is not None:
		pre_list.append(t.value)
		preorder(t.left)
		preorder(t.right)

#prints the expression given in infix notation, including parenthesis
def inorder(t):
	if t.left == None:
		print(t.value,end='')
	else:
		print('(',end='')
		inorder(t.left)
		print(t.value,end='')
		inorder(t.right)
		print(')',end='')
  



#INFIX="1+((C+A)*(B-F))"
#infix = "((1-2)-3)*((4+5)/(6-7))" #==9

#testing different things
pre_vysledek = in2pre(infix)
solution = solvePre(pre_vysledek)
print(solution)

post_vysledek = in2post(infix)
print(post_vysledek)
r = construct_post(post_vysledek)

pre_list = []
preorder(r)
print(*pre_list)





post = "12-3-45+*67-/"
post_done = construct_post(post)


pre_list = []
pre_list=preorder(post_done)
print(*pre_list)

inorder(post_done)
