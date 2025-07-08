#print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1

#print numbers from 100 to 1
j=100
while j>=1:
    print(j)
    j-=1

#print multiplication table of a number n
n=int(input("enter a number: "))
l=1
while l<=10:
    print(n*l)
    l+=1
#print the elements of the following list using a loop:
#[1,4,9,16,25,36,49,64,81,100]

list=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(list):
    print(list[idx])
    idx+=1
    

#search for a number x in a tuple using loop
#[1,4,9,16,25,36,49,64,81,100]
tup=(1,4,9,16,25,36,49,64,81,100)
x= int(input("enter a number: "))
i=0
while i<len(tup):
    if (x==tup[i]):
        print("we found x at index: ",i)
        break
    else:
        print("x not found at index: ", i)
    i+=1

#continue

i=1
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

#break
i=1
while i<=5:
    if(i==3):
        break
    print(i)
    i+=1

# FOR LOOPS
nums=[1,2,3,4,5,6,7,8]
for val in nums:
    print(val)

college="osmania college"
for char in college:
    if(char=='n'):
        break
    print(char)

# range
print(range(5))


for i in range(10):
    print(i)

for i in range(2,10):
    print(i)

for i in range(2, 10, 2):
    print(i)

#print numbers from 1 to 100 using for loop:
for i in range(1,101):
    print(i)

#print numbers from 100 to 1 using for loop:
for i in range(100,0,-1):
    print(i)

#print multiplication table of number n.
n=int(input("enter a number: "))
for i in range(1,11):
    print(n*i)

#wap to find the sum of first n numbers. use while loop.

n=int(input("enter a number: "))
sum=0
while i <=n:
    sum+=i
    i+=1
print(sum)

#wap to find the sum of first n numbers. use for loop.

n=int(input("enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#wap to find the factorial of first n numbers. use for loop.
n=int(input("enter a number: "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)

## #wap to find the factorial of first n numbers. use while loop.
n=int(input("enter a number: "))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print(fact)