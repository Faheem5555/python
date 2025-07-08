##store following word meaning in python dictionary
#table: "a piece of furniture" , cat:"pet animal"

dict={
    "table":"a piece of furniture",
    "cat": "pet animal"
}
print(dict)
print(type(dict))

#you are given a list of subjects for students. assume one classroom is required for i subject so how many classroom is required for all subjects.
# "python", "java", "c++", "java", "python","javascript","power BI","SQL", "Power BI"

set={"python", "java", "c++", "java", "python","javascript","power BI","SQL", "Power BI"}
print(set)
print(len(set))

#WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

set1={}
set1.update({"phy": input("phy marks: ")})
set1.update({"chem": input("chem marks: ")})
set1.update({"math": input("math marks: ")})
print(set1)

#firgure out a way to store 9 and 9.0 in a set. you can take help of built in datatypes.
set2={9,"9.0"}
print(set2)