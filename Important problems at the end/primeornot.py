def prime(num):
    if num>1:
        for i in range(2,int(num/2)+1):
            if(num%i==0):
                print("it is not a prime number")
            else:
                print ("it is a prime number")
    else:
        print("it i snot a prime number")
num=int(input("enter a number"))
prime(num)