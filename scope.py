#in python indentation is used to define scope.

# x = 10   #Global scope
# y = 20

# def sum(x,y):  #local scope
#     return x+y

x =10
def sum():
    global x
    x = 9
    y =33
    print(x)

print(x)

sum()

print(x)
    

