t = (10,20,30,40,50) #define a function to swap first and last elements without converting to a list.

# def swap(t):
    # t = list(t)
    # t[0],t[4] = t[-1],t[-5]
    # return t

# def swap(t):
#     if len(t) == 1:
#         return t
#     return (t[-1],) + t[1:-1] + (t[0],)

# print(swap(t))

# def reverse(t):
#     return t[::-1]


# print(reverse(t))

#write a function to rotate a given tuple by k positions

# def rotate(t,k):
#     k = k%len(t) 
#     return t[-k:] + t[:-k]

# def rotate(t, a):
#     result = (t[-1],) + t[:len(t)-1]
#     print(result)
#     if a < 0:
#         return 0
#     return rotate(result, a-1)

# # print(t)
# rotate(t, len(t))

# word = input("input Word:")

# def word_freq(word):
#     freq = {}

#     for i in word:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
#     return freq

# print(word_freq(word))

# dict = {"a":-10,"b":-1,"c":-11}
# def max_f(dict):
#     max_value = (-1)*(2)**32

#     for i in dict:
#         if dict[i] > max_value:
#             max_value = dict[i]
#             max_key = i
#     return max_key        

# print(max_f(dict))

# write a function to merge-add(d1,d2).Merge two dictionaries when a key appears in both add the value.

# d1={"a":1,"b":2}
# d2={"b":3,"c":4}

# def merge_add(d1,d2):
#     for i in d1:
#         for j in d2:
#             if i == j:
#                 d1[i] == d1[i] + d[j]
#             else:


#Q. 

# a ={1,2,3,4}
# b = {2,3,5}
# c ={3,2,9}

# intersection = a & b & c

# print(intersection)


# e = "Satyam is a good boy"
# s = "The cat and the hat"
# def unique_word(s):
#     l = s.lower()
#     u = l.split()
#     s1 =set(u)
#     print(s1)
#     print(len(s1)) 

# unique_word(e)
a = [1,2,3]
b = [2,3,4]

def only_in_one(a,b):
    s1 = set(a)
    s2 = set(b)

    s3 = (s1|s2) - (s1&s2)
    lis1 = list(s3)
    return lis1

print(only_in_one(a,b))
# print(s3)
# print(s1)
# print(s2)

