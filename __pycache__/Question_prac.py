#Check whether given string is a palindrome or not.

# str1 = input("Enter String:").strip()

# reversed_str = str1[::-1]

# if str1 == reversed_str:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

s = input()
clean_s = s.strip()

# rev = clean_s[::-1]
# if (rev == clean_s):
#     print("is a palindrome")
# else:
#     print("not a palindrome")

#function
# def check_str_palindrome(s):
#     cleaned = "".join(i for i in clean_s if i.isalnum())
#     return clean_s == cleaned[::-1]

# print(check_str_palindrome(clean_s))

#Write a function to count thr no. of vowels ,consonants,numbers and special characters in a given string.

#And return there count in a form of dictionary.

# def f(s):
#     temp = ""
#     for i in s:
#         if i not in temp:
#             temp += i
#     return temp

# print(f(clean_s))

#Write a function to count amd print the longest word in a given string.

s = "First programe language "
max = 0

def longest_word(s):
    max_len = 0
    for i in range(len(s)):
        if len(s[i]):