#Read a number n<50 indicating the number of pairs of parentheses to use. Write out all possible valid parenthesizations using these n pairs. A parenthesization is valid if no opening parenthesis remains unclosed and every closing parenthesis has a matching opening parenthesis, just like in an arithmetic expression.

#Output the parenthesizations in lexicographic order so that an opening parenthesis lexicographically precedes a closing parenthesis. Write each valid parenthesization on its own line.

#Input:

#2

#Output:
#(())
#()()

def zavorky(seznam, pos, n, open, close):     
    if(close == n): 
        for i in seznam: 
            print(i, end = "") 
        print() 
        return seznam
    else: 
        if(open < n): 
            seznam[pos] = '('; 
            zavorky(seznam, pos + 1, n, open + 1, close); 
        if(open > close): 
            seznam[pos] = ')'; 
            zavorky(seznam, pos + 1, n, open, close + 1); 
def moznosti(seznam, n): 
    if(n > 0): 
        zavorky(seznam, 0, n, 0, 0);
    return
n = int(input())
seznam = [None] * 2 * n
moznosti(seznam, n)