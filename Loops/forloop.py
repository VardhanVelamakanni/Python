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
