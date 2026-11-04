#What is recurssion?
#A function calling itself until a condition is satisfied.

# syntax of recurssion

#def fun():
#base condition

# n = int(input("Enter Number: "))

#Recursive function - factorial
# n x (n - 1)!

# def f(n):
    #Base condition
    # if n == 0 or n == 1:
        # return 1
    # return n*f(n-1)

# print(f(n))

# n = int(input())

# def f(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2

#     return f(n-1)+f(n-2)

# print(f(n))

#sum
# n = int(input())

# def f(n):
#     if n == 0:
#         return 0
#     return n + f(n-1)

# print(f(n))

a = int(input())
b = int(input())

def po(a,b):
    if b == 0:
        return 1
    return a*(a,b-1)

print(po(a,b))
    




    