#Break:is used to terminate the loop when encountered
#continue:terminates execution in the curren iteration and continues execution of the loop with the next iteration
#example
num=1
while num<5:
    print(num)
    if num==3:
        break
    num+=1
print("end of the loop")
#prints only untill the specified if confition 

#previous example
#refer to Loops/loopsdiy.py
num1=[1,4,9,16,25,36,49,64,81,100]
element=int(input("enter a number to search in the followiung list"))
index=0
while index<len(num1):
    if (num1[index] == element):
         print("found at index",index)
         break
    else:
        print("finding...")
    index +=1
#if we add break statement here it checks for the specified elements and breaks the loop and wont check further

#Continue
num=1
while num<=5:
    if num ==3:
        num +=1
        continue
    print(num)
    num+=1