#function for List
# 1.

















# t1 = (10,20,40,30)

# print(t1[:3])

# L1 = ["Rungta",10,20,30,40]
# print(L1[:1])

# print("Tuple")
# for i in t1:
#     print(i)
# print()
# for i in range(len(t1)):
#     print(t1[i],end =" ")

# print("List")
# for i in L1:
#     print(i)

#for List
# l1 = [10,20,30,40,50,60,70]
# l1.append(80)
# print(l1)

# l1.insert(5,90)
# print(l1)

# l1.remove(10)
# print(l1)

# l1.pop(6)
# print(l1)

# l1.count(l1)
# print(l1)

# l1.index(50)
# print(l1)

# max(l1)
# print(l1)

# min(l1)
# print(l1)

# sum(l1)

# li3 = [i for i in range(1,1001)]
# print(li3)

# Create a list that contain only odd numbers between 1-100.
# li4 = [ i for i in range(1,101) if i % 2 !=0]
# print(li4)


l1 = [1,2,3,4]
l2 = [6,7,8,9]

# print(l1+l2) # Concatination
# # print(l1*l2) not possible 
# print(l1*4)

t1 = (10,20,30)

def f(t1):
    for i in range(len(t1)):
        print(f"{i}:{t1[i]}")

f(t1)