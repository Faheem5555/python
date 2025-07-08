marks= ["Faheem", 98, "Mohammed", 90, "Akthar", 89]
print(marks)
print(marks[:2])
print(marks[-2:])
marks[1]=100
print(marks)

# list methods
a=[2, 1, 3]
print(a.append(4))
a.append(4)
print(a)

print(a.sort()) 
a.sort()
print(a)

print(a.sort(reverse=True))
a.sort(reverse=True)
print(a)

print(a.reverse())
a.reverse()
print(a)

list=["a", "b", "e", "d", "f"]
print("list: ", list)

list.reverse()
print("reverse list: ",list)

list.append("g")
print("add g: ",list)
list.append("h")
print("add h:",list)
list.append("i")
print("add i: ",list)
list.append("j")
print("add j: ",list)
list.append("k")
print("add k:", list)

list.sort()
print("sort the list: ",list)

list.sort(reverse=True)
print("reverse sort the list: ",list)

list.reverse()
print("revere the list: ",list)

print("final list: ", list)

list.insert(0,"z")
print("inserted z in list: ", list)

list.append("z")
print("add z: ", list)

list.remove("z")
print("removed z: ", list)

list.pop(0)
print("pop a from the list: ", list)

#tuple
tup =(1,2,3,4,3,4) 
print(type(tup))
print(tup)
print(tup.index(2))
print(tup.count(3))
print(tup.index(4))
