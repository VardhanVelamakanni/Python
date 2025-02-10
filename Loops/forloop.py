#for loops are used for sequential traversal ,for Traversing list,string,tuples etc,
list=[1,2,3]
for el in list:#here there can be anything instead of el ..like value,char etc
    if(el%2==0):
        print(el)
    else:
        print("not found")
#the main difference between while loop and for loop is that while loop is used where there is stopping condition or it is a code that is neede top work in iterater
#whereas for loop is used traverse through data types sequentially
#break condition
str="vardhan"
for char in str:
    if (char=="r"):
        print("r found")
        break
    print(char)

#range()
#range functions return a sequence of numbers,starting from 0 by default, and increments by 1(by default),and stops before specified number
#range(start,stop,step)
#start:the element from which the range must start
#stop:the element at which the range must stop incrementing
#step:the size between each increment
for i in range(10):
    print(i)
print("end")
for x in range(2,10):
    print(x)
print("end")
for z in range(2,10,2):
    print(z)
print("end")

#pass
#pass is anull statement that does nothing.it is used as a placeholder for future code
for i in range(1,10):
    pass #here it ia null statement
print("further code")

