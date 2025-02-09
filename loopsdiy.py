#print number from 1 to 100
i =1
while i<=100:
    print(i)
    i+=1
print("loop ends")
#print number from 100 to 1
x=100
while x>=1:
    print(x)
    x-=1
print("loop ends")
#print the multiplication table of a number n
num=int(input("enter the number for multiplication"))
limit=int(input("enter the end of the table limti"))
z=1
while z<=limit:
    print(num*z)
    z+=1
#print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]
nums=[1,4,9,16,25,36,49,64,81,100]
index=0
while index<len(nums):
    print(nums[index])
    index+=1
#this is called traversing in languages where we travel through each element of the list or tupple
#to find a number in the following list given
num1=[1,4,9,16,25,36,49,64,81,100]
element=int(input("enter a number to search in the followiung list"))
index=0
while index<len(num1):
    if (num1[index] == element):
         print("found")
    index +=1