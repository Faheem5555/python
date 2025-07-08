light=""

if(light=="green"):
    print("go")
elif(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("wait")
else:
    print("light is broken")

##grading a class
maths=54  #99, 87, 74, 56
if(maths>=90):
    print("grade: A")
elif(maths>=80 and maths<90):
    print("grade: B")
elif(maths>=70 and maths<80):
    print("grade: C")
elif(maths<70):
    print("grade: D")

##
maths=54  #99, 87, 74, 56
if(maths>=90):
    grade="A"
elif(maths>=80 and maths<90):
    grade="B"
elif(maths>=70 and maths<80):
    grade="C"
else:
    grade="D"
print("grade od student in maths: ", grade)

##nesting
age=88  # 14, 25, 88

if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")