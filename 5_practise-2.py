#wap to check if user entered number is even or odd.
a= int(input("user input: "))
b=a%2
if(b==0):
    print("user input is even number")
else:
    print("user input is odd number")

#wap to find greatest of three numbers entered by the user.
d= input("enter first number: ")
e= input("enter second number: ")
f= input("enter third number: ")
if (d>e and d>f):
    print("greatest numner is: ", d)
elif (d>e and d<f):
    print("greatest number is: ", f)
else:
    print("greatest number is: ", e)

#wap to check if a number is multiple of 7 or not.
x=int(input("enter a number: "))
y=x%7
if (y==0):
    print("entered number is multiple of 7")
else:
    print("entered number is not multiple of 7")
