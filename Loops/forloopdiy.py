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


