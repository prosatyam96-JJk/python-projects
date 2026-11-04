# 1.Write a to print all prime numbers 1 and n.
#input: 10
#output: 2,3,5,7
# n=int(input("Enter n:"))
# for i in range(2,n+1):
#     count = 0

#     for j in range(1, i+1):
#         if i % j ==0:
#             count = count + 1
        

#     if count == 2:
#         print(i, end=" ")

#2. Write a program to find the sum of prime numbers between 1 and n.
#Input:10
#Output: 17

# n = int(input("Enter n: "))
# total = 0

# for i in range(2,n+1):
#     count = 0

#     for j in range(1,i+1):
#         if i % j == 0:
#             count = count + 1

#     if count == 2:
#         total = total + i

# print(total)

# 3.Write a Program to print all factors of a given number.
# input: 12
#output: 1 2 3 4 6 12

# n = int(input("Enter n: "))

# for i  in range(1,n+1):
#     if n % i == 0:
#         print(i, end=" ")

# 4.Write a program to check whe
# ther a given number is a perfect number.
# input: 6
#output: Perfect number

# n = int(input("Enter a Number: "))
# total = 0

# for i in range(1,n):
#     if n % i == 0:
#         total+= i

# if total == n:
#     print("Perfect number")
# else:
#     print("Not a Perfect number")

#5.Write a program to find the second largest number among n input numbers without sorting.
#input: 5 numbers: 12 45 7 31 28
#Output: 31
# n = int(input("Enter number of values: "))

# largest = 0
# sec_largest = 0

# for i in range(n):
#     num = int(input("Enter number: "))

#     if num > largest:
#         sec_largest = largest
#         largest = num

#     elif num > sec_largest:
#         sec_largest = num

# print("Second Largest =",sec_largest, end =" ")


# 6.Write a program to repeatedly calculate the sum of digits until a single digit number is obtained.
# Input: 9875
# output: 2

# n = int(input("Enter a Number: "))
# total = 0

# while n>0:
#     digit = n % 10 
#     total+= digit
#     n = n // 10

# n = total

# print(n)

# 7. Write a program to perform circular shift of a number by one digit.
# input: 12345
#Output:51234

# n = input("Enter a number: ")

# last = n[-1]
# first = n[:-1]

# print(last + first)

# 8.Write a program to check whether a number is an armstrong number.
# input: 153
# Armstrong number

# n = int(input("Enter a number: "))
# original = n
# total = 0

# while n > 0:
#     digit = n % 10
#     total += digit ** 3
#     n = n // 10
    


# if total == original:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# 9. Write a program to find the frequency of each digit in a given number.
# input: 1223342
#Output: 1:1, 2:3, 3:2, 4:1

# n = input("Enter a number:")

# for i in range(10):
#     count = 0

#     for j in n:
#         if j == str(i):
#             count+=1

#     if count > 0:
#          print(i,":",count, end=",")

# 10. Write a program to find the second largest digit of a number without sorting.
# input: 58321
#output: 5

# n = int(input("Enter a number: "))
# largest = -1
# sec_largest = -1

# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         sec_largest = largest
#         largest = digit
#     elif digit > sec_largest:
#         sec_largest = digit
#     n = n // 10

# print("Second Largest Digit =", sec_largest)

# 11, Write a program to find the sum of digits at even positions and odd positions separatly.
# input: 12345
#Output: Sum of digits at even positions: 6, Sum of digits at odd positions: 9

# n = input("Enter a number:")
# even_sum = 0
# odd_sum = 0

# for i in range(len(n)):
#     digit = int(n[i])
#     if i % 2 == 0:
#         odd_sum+= digit
#     else:
#         even_sum += digit

# print("Sum of digits at even positions:", even_sum)
# print("Sum of digits at odd positions:", odd_sum)

# 12. Write a program to check whether all digits of a number are even.
# input: 2486
#Output: All digits are even

# n = input("Enter a number:")

# for i in n:
#     if int(i) % 2 != 0:
#         print("Not all digits are even")
#         break
# else:
#     print("All digits are even")

# 13. Write a program to check whether the digits of a number are in increasing order.
# input: 12349
#Output: Digits are in increasing order

# n = input("Enter a number:")
# is_increasing = True

# for i in range(len(n) - 1):
#     if int(n[i]) >= int(n[i + 1]):
#         is_increasing = False
#         break

# if is_increasing:
#     print("Digits are in increasing order")
# else:
#     print("Digits are not in increasing order")

# 14.Write a program to find the difference between the largest and the smallest digit of a number.
# input: 58321
# Output: 7

# n = int(input("Enter a number: "))
# largest = -1
# smallest = 10

# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         largest = digit
#     if digit < smallest:
#         smallest = digit
#     n = n // 10

# print("Difference between largest and smallest digit:", largest - smallest)

# 15. Write a program to find the largest and second largest digit in a single traversal of the number.
#input: 58321
#Output: Largest Digit: 8, Second Largest Digit: 5

# n = int(input("Enter a number:"))
# largest = -1
# sec_largest = -1

# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         sec_largest = largest
#         largest = digit
#     elif digit > sec_largest:
#         sec_largest = digit
#     n = n // 10

# print("Largest Digit:", largest)
# print("Second Largest Digit:", sec_largest) 
