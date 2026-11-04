S = "Recursion is very useful"

# print(S[0])
# print(S[-1])

# print(S[2:5])
# print(S[ : :-1])

# temp_s=""
# for i in S:
#     if i== "e":
#         temp_s+=i.upper
#         temp_s+=i
# print(temp_s)

password

def validate_password(password):
    if len(password)<8:
        return "password should be at least 8 characters"
    if len(password)>16:
        return "password is too long"
    if not any(char.isdigit() for char in password):
        return "password should contain at least one digit"
    if not any(char.isupper() for char in password):
        return "password should contain at least on upper"
    if not any(char.islower() for char in password):
        return "pasword should contain at least one lower"

