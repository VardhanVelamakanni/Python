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




