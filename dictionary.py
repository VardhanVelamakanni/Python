#has key:value pair
#these are mutable and can have any value as a key and value 
Dictionary={
    "key":"value",
    "name":"vardhan",
    "age":19,
    "is_adult":True,
    "marks":80.3,
    "subjects":["python","c","java"],
    "topics":("dictionary","tuples"),
    12.9:9

}
Dictionary["name"]="Hemavardhan"
Dictionary["surname"]="Velamakanni"


#this can also start with a null dictionary
null_dictionary={}
null_dictionary["name"]="vardhan"
#print(null_dictionary)
#so this way we can start with a null dictionary and keep on adding stuiuf to it


#Nested Dictionary
Student={
    "name":"vardhan",
    "score":{
        "coding":"a",
        "aptitude":"b",
        "Maths":"c"
    },
    "Cgpa":7
}
#print(Student)

#print(Student["score"]["coding"])

#dicitonary Methods

print(list(Student.keys()))#prints all the keys present in the dictionary
print(list(Student.values()))#prins all the valkues prestnt in the dicitonary as a list
print(Student.items())#prints all the key value pairs as a tuple
pairs=list(Student.items())
print(pairs[0])#prints the provided pair 
print(Student.get("name"))#prints the vlaue of the key
#to update the dictionary with a new key and value pair
Student.update({"City":"Vijayawada"})
print(Student)