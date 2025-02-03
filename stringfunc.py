#inbuilt function in strings
string1="vardhan"
print(string1.endswith("an"))#for the give input in the fucntion it telss us if it ends with it or not
print(string1.endswith("na"))#flase as it does not end with na
#capitalize
print(string1.capitalize())#prints the sring with first letter capitalized
#replace
print(string1.replace("d","t"))#replaces d with t in the given string
#find
print(string1.find("d"))#gives the index value of the letter given in the word
string2="hi iam a python developer"
print(string2.find("iam"))#as the word that has been given to find starts from index value 3..it gives output as 3
#count
string3="iam iam iam iam not not iam"
print(string3.count("am"))
