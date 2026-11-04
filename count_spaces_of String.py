str1=input("Enter a string: ")
count = 0

for i in str1:
    if(i==" "):
        count+=1
print("Number of spaces in the string:", count)