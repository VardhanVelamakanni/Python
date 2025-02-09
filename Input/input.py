name= input("enter your name:")
print("hi ", name)

#to get the data type of the inputed variable
#value =input("enter any value:")
#print(type(value),value)
#this always gives the value to be as str..no mater what
value=int(input("enter your age"))
if(value<18):
    print("the age",value,"is considerd to be minor")
else:
    print("you are good to go")
#this way to take a integer value as input "int(input(""))" should be used
#same apllies for other data types
#DIY
#Write a program to input two numbers and print their sum
value1=int(input("enter the first number"))
value2=int(input("enter the second nummber"))
sum=(value1+value2)
print(sum)