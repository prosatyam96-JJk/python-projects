# Dictionary is colllection of (key value) pairs.

dict1 = {"stu1_name":"Satyam", "Age": 19, "Percentage": 55.0}
print(dict1)

for key in dict1:
    print(key)

for key in dict1.items():
    print(key)

print(dict1.get("stu1_name"))
print(dict1["stu1_name"])