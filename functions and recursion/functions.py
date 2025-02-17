#function is a block of statements that perform a specific task
#example
"""def func_name(value1,value2..):
##some work
return value
func_name(arg1,arg2..)#func call"""
#clculating sum of two numbers using functions
def sum(a,b):#parameters a,b
    sum=a+b
    return sum
a=(int(input("enter first number")))
b=int(input("enter the second number"))
print(sum(a,b))#attributes a,b
"""if we see the sum values in the definition of the fucntion and the calling of the function are same ...but they are different ,
the values the defined the function definition are parameters and the values that are called to print the function are know as arguments"""
#this way the need to sum numbers an be called any number of tiumes by just calling the function rather than writing code every time 
#example 2
def calc_sum(a,b):
    return a+b
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
print(calc_sum(num1,num2))
#print average of 3 numbers
def avrg(a,b,c):
    sum=a+b+c
    avrg=sum/3
    print(avrg)
    return avrg
num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
avrg(num1,num2,num3)#this way we dont need to print the value instead just call the function
#default parameters
#when there is no values given in as attributes in the function call then there must be default values given in the function definition
def calc_prod(a=1,b=3):#default values 1,3 given
    prod=a*b
    print(prod)
    return prod
calc_prod()#no vlaues given means it need to take default parametrs of the function definition 1,
#if only one default value must be given then it must always follow a non default argument
#example
"""def cal_prod(b,a=2)===correct
def calc_prod(a=2,b)===wrong"""
