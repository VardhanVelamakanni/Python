#operators
#Arithmetic Operators ( +,-,*,/,%, ** )
#Relational / Comparison Operators ( == , != , > , <, >=, <= )
#Assignment Operators ( = , +=, -= , *= , /=, %=, **= )
#Logical Operators ( not, and , or )

#Arithmetic oprators
a=10
b=20
sum=(a+b)
sub=(a-b)
mul=(a*b)
float=(a/b)
modulo=(a%b)
power=(a**b)

print(sum)
print(sub)
print(mul)
print(float)
print(modulo)
print(power)
 
#assignment operator
x=(10)
x+=10
print("num", x)
#similar for every other assignment operator

#Relational operators is for relating
s=10
d=4
if (s==d):        #if else statements(learned them)
    print("equal")
else:
    print("no")

#logical operators
#AND,OR,NOT

f=50
g=30
print(not(f>g))#output will be flase as the given condtion is true and not of true is flase
val1=True
val2=False
print("And operator",val1 and val2)#only gives true if any of the values of the variable is true..or it will only result in false
print("Or operator" ,val1 or val2)#results in true of any of the value of the varaiable is true

