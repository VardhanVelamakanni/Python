#sets are collection of unordered items
#each item must be unique and immutable
#no keys present...only values
set={1,2,2,2,3,4,"Hello","Hello"}
print(set)
#ignores the values that are repeated more than once
#methods in set
set.add("world")
print(set)#adds rthe specified element
set.remove("Hello")
print(set)#removes the specified element
set.pop()
print(set)#removes a element randomly
set.clear()
print(set)#empties the set

#Mathematical point of view for set methods
Set1={1,2,3,4}
Set2={3,4,5,6}
print(Set1.union(Set2))#prints all the elemnts present in both the set and ignores all other duplicate items
print(Set1.intersection(Set2))#prints only the elements that are common in both the sets
