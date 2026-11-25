student={"name":"Alice","age":21,"grade":"A"}
print(student)
print(student["name"])
print(student.get("age"))
student["age"]=22
student["city"]="New York"
print(student)

for key,value in student.items():
    print(key,":",value)