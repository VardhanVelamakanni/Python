#lists
#lists are mutable that is the value its single index can be changed
list1=[99,00,22,33,44]
print(list1)
list2=["hello",44,"world",45,66]
list2[0]="hi!"#gere the index 0 has been changed
print(list2[0])
#slicing in list
#same as lsicing in string
list3=[99,87,64,48,34]
print(list3[1:4])
print(list3[:4])
print(list3[1:])
print(list3[-4:-1])

#list methods(functions)
list4=[1,3,5,4,2,6]
list4.append(7)
print(list4)
list4.sort()
print(list4)
list4.sort(reverse=True)
print(list4)
list3.reverse()
print(list3)
list4.insert(4,8)
print(list4)

list4.remove(4)#removes the elemnet 4
print(list4)
list3.pop(2)#removes the lement at index 2
print(list3)