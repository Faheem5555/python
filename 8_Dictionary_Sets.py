info={
    "name": "Faheem",
    "Age": 25,
    "Adult": True,
    "Percentage":98.9,
    "Subjects": ["python","SQL","Power BI"],
    "Topics": ("Dictionary","sets","List","Tuple"),
    "marks": {
        "phy": 98,
        "chem": 96,
        "math":99
    }

}
print(info)
print(type(info))
print(info["marks"])
print(info["marks"]["phy"])

print(info.keys())

print(info.values())
print(list(info.values()))

print(info.items())

pairs=list(info.items())
print(pairs[0])

print(info.get("name"))
print(info.get("marks"))
print(info.get("Subjects"))
print(tuple(info.get("Subjects")))
print(dict(info.get("marks")))

print(info.keys())
print(info.values())
print(type(info.items()))

info.update({"city": "hyderabad"})
print(info)

# sets
set1=set()
print(type(set1))
set1.add(1)
print(set1)
set1.add(2)
print(set1)
set1.add(("a","b","c"))
print(set1)
set1.add(4)
set1.add(5)
set1.add(6)
print(set1)
set1.remove(1)
print(set1)
print(set1.pop())

print(set1)
set1.clear()
print(set1)
print(len(set1))

set2={1,2,3,4,5}
set3={3,4,5,6,7}
print(set2.union(set3))
print(set2.intersection(set3))

set4={"kalki","fan","salaar","rajasaab","darling","mr.perfect"}
print(set4.pop())