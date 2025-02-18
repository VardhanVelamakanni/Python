#write a program to print the length of a list.(list is the parameter)

def len_list():
    n=int(input("enter the size of the list" ))
    a=[]
    for i in range(n):
        element=input("enter the number")
        i+=1
        a.append(element)
    print("length of your list is",len(a))
    return a
b=len_list()

#write a program to print elements of a list in a single line
def sing_line():
    n=int(input("enter the size of the list"))
    a=[]
    for i in range(n):
        ele=int(input("enter the elements"))
        i+=1
        a.append(ele)
    print(a,end="")
    return a
c=sing_line()

#write a program to find factorial of a number
def facto(n):
    n=int(input("enter the number"))
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(fact)
    
facto(4)

#write a program to convert USD to INR
def USd(n):
    n=int(input("enter the USD value"))
    m=n*80
    print("your Indian value is ",m)
USd(80)






