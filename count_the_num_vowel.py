#Membership operator(true/false)
# in
#notin
str1 = "Select a Language"
str_v = "aeiouAEIOU"

count_v = 0

for i in str1:
    if (i in str_v):
        count_v+= 1

print(count_v)