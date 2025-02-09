#store folllowoing word meaning in a python dictionary:
Dictionary={
    "table":{
        "a piece of furniture", "list of facts and figures"
    },
    "cat":"a small animal"
}
print(Dictionary)

#You are given a list subjects.Assume one classroom is required for 1 subjects.How many Classrooms are needed by all students.
#"python","java","C++","python","javascript","java","python","java","C++","C"
Student_subjects={
    "python","java","C++","python","javascript","java","python","java","C++","C"
}
print(Student_subjects)

#write a program to enter the marks of 3 subjects from the user and store them in a dictionary.Start with an empty dictionary and ass one by one.Use Subject name as key and marks as values.
marks={}
x=int(input("enter the marks of physics"))
marks.update({"physics":x})
y=int(input("enter the marks of maths"))
marks.update({"Maths":y})
z=int(input("enter the marks of chemistry"))
marks.update({"Chemistry":z})
print(marks)