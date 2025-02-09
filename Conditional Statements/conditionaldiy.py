#write a program to check if a number entered by the user is odd or even
numb1=int(input("enter a number"))
if(numb1%2==0):
    print("it is a even number")
else:
    print("it is a odd number")

#write to find the greatest of 3 numbers entered by the user
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))
if(n1>n2>n3):
    print("first numb i sgreater than other")
elif(n2>n3):
    print("second is greater")
else:
    print("third i greater")

#write a program to check if a number is a multiple of 7 or not
n=int(input("enter a number"))
if(n%7==0):
    print("it is a multiple of 7")
else:
    print("no)")

