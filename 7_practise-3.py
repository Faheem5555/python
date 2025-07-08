#wap to ask the user to enter the name of their 3 favorite movies and store them in a list.
movies=[]
movies.append(input("enter first favorite movie: "))
movies.append(input("enter first favorite movie: "))
movies.append(input("enter first favorite movie: "))
print(movies)

#wap to check if a list contains palindrome of elements(hint: use copy() method.)
mylist1=[1,2,3,4,3,2,1]
mylist1_copy=mylist1.copy()
mylist1_copy.reverse()
print(mylist1_copy)
if(mylist1==mylist1_copy):
    print("yes, its palindrome")
else:
    print("its not palindrome")

mylist2=[1,2,3,4,3,2]
mylist2_copy=mylist2.copy()
mylist2_copy.reverse()
print(mylist2_copy)
if(mylist2==mylist2_copy):
    print("its palindrome")
else:
    print("NOT palindrome")

##wap to count number of students with A grade in the following tuple.
tup1=("C","D","A","A","B","B","A")
print(tup1.count("A"))

#wap to store the above tuple values in a list and sort them from A to D.
tup1=["C","D","A","A","B","B","A"]
tup1.sort()
print(tup1)