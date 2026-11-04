#create a list that contains the cubes of the numbers from another pre-existing and check if the geven number are even.
a = [77,88,64,10,54,3,2]
l1 = [ i**3 for i in a if i%2 == 0]
print(l1)

