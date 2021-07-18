#Write a program implementing a simple "phonebook". Instead of names and numbers we are storing only (positive) integers. Program is operated by the instructions given on a standard input. 
#One input line always consist of one or two numbers. The first number is the code of the operation, the second (when applicable) is an argument. Operations are the following:
#1 - insert the number into the phonebook,
#2 - erase the number from the list,
#4 - sort the list (in an descendent way),
#5 - output (print the numbers in the list),
#6 - exit (finish the program).
#Operations 1 and 2 are followed by the parameter (a number that shall be inserted or erased).

#For example, a line "1 5" means "insert value 5 into the list". Line "2 4" means "remove value 4 from the list". For the output, put each number on a separate line. 
#When you are asked to erase a value which is not a member of the list, ignore the operation (and avoid the crash of the program). When removing from an ordered list, keep the list ordered.

#Example:
#Input:
#1 1
#2 2
#1 2
#1 3
#2 3
#4
#5
#6
#Output:
#2
#1

#Remarks: Any list is sorted somewhere after the last insert preceding output (thus you may add at the beginning, at the end or wherever you want; you must not change the order of the elements remaining after erasing). 
#When erasing an element that occurs multiply, all the testing data contain sufficiently many deletes so you may erase either only one or all of them, it does not matter.


def ctecka():
    vstup = str.split(input())
    cisloZadane= []
    for i in range(len(vstup)): 
        ele = int(vstup[i])  
        cisloZadane.append(ele)
    return cisloZadane

kontakty = []
operace = None
while operace != 6:
    prikaz = ctecka()
    operace = prikaz[0]
    if len(prikaz)>1:
        hodnota = prikaz[1]
    if operace  == 1:
        kontakty.append(hodnota)
    elif operace  == 2:
        if hodnota not in kontakty:
            pass
        else:
            kontakty.remove(hodnota)
    elif operace == 4:
        kontakty.sort(reverse = True)
    elif operace == 5:
        for i in kontakty:
            print(i)
