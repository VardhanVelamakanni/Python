#print the elements of the following list using a loop:
list=[1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)

#search for anumber x in this tuple using loop
tup=(1,4,9,16,25,36,49,64,81,100,25)
n=int(input("enter the number to be searched"))
idx=0
for el in tup:
    if (el==n):
        print("found",n,"at index",idx)
    print(el)
    idx+=1

#range diy
#print number from 1 to 100
for i in range(1,100):
    print(i)
#print number from 100 to 1
for i in range(100,0,-1):
    print(i)
#print the multiplication table of a number n
n=int(input("enter a number for multiplication table"))
limit=int(input("enter the limit og table"))
for i in range(1,limit+1):
    print(i*n)

#write a program to find the factorial of first n numbers:
num=int(input("enter the limit for factorial"))
fact=1
for i in range(1,num+1):
    fact *= i
    
print(fact)


