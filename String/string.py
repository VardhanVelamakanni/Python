
# type: ignore

string1="this is a string"#example of a string declaration
#for the line to be printed in new line
string2="this string is in first line\nthis string is in new line"
print(string2)
#for a tab space btween
string3="before gap\tafter gap"
print(string3)
#conacatenation of strings
str1="vardhan"
str2="velamakanni"
final_str=str1+str2
print(final_str)
#length of the string
str3="vardhanvelamakanni"
print(len(str3))
#empty spaces also count while using inbuilt fucntion "len()"
name1="vardhan"
name2="velamakanni"
final_name=name1+ " " +name2
print(len(final_name))#space also counts as a character

#**Indexing**#
#when ever a string is created internally a indexing is created for a string like a number wise indexing starting from 0
a="vardhan"
print(a[2])#"r" is printed
#"v,a,r,d,h,a,n"
#"0,1,2,3,4,5,6"

#**slicing**
#slicing used to acces parts of a string
#str[starting_indx:ending_indx]
str = "vardhan"
print(str[ 1 : 4 ]) #is "ard" ("ending_indx is not included in slicing")
print(str[ : 4 ]) #is same as str[ O : 4]
print(str[ 1 : ]) #is same as str[ 1 : len(str) ]
#negative slicing
#"v,a,r,d,h,a,n"
#"-7,-6,-5,-4,-3,-2,-1"
print(str[-6:-4])