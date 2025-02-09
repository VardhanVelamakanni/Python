#write a program to ask the user to enter names of their 3 favorite movies and store them in a list
mov=[]
mov.append(input("enter your first movie"))
mov.append(input("enter your second movie"))
mov.append(input("enter your third movie"))

print(mov)

#write a program to check if a list contains a palindrome of elements
list1=[1,2,1]
list2=[2,3,4]
copy_list=list1.copy()
if(list1==copy_list):
    print("its is a plaindrome")
else:
    print("no")

#write a program to count the number of student swith the "A" grade in the following tupple.
#["C","D","A","A","B","B","A"]
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))
#similar above values most be stored in a list and be sorted
List=["C","D","A","A","B","B","A"]
List.sort()
print(List)
