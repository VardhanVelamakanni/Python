age=int(input("enter your age"))
if(age<18):
    print("you ar a minor with a age of",age)
else:
    print("you are good to go")
#example for if elif ans else statements
name=input("enter your name")
mark1=int(input("enter your marks of subject 1"))
mark2=int(input("enter your marks of subject 2"))
mark3=int(input("enter your marks of subject 3"))
mark4=int(input("enter your marks of subject 4"))
mark5=int(input("enter your marks of subject 5"))
avrg=((mark1+mark2+mark3+mark4+mark5)/5)
if(avrg>=90):
    print("your grade is A")
elif(avrg>=70):
    print("your grade is B")
elif(avrg>=60):
    print("your garde is C")
elif(avrg>=40):
    print("your garde is D")
else:
    print("you are fail")
#nested if statements
age1=int(input("enter your age"))
if(age1>=18):
    if(age1>80):
        print("not apllicable")
    
    print("your are a major")
    
else:
    print("you are a minor")