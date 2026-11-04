# km = float(input("Enter distance:"))
# miles = km * 0.621371
# print(f"{miles:.2f}")

n = int(input("Enter a number: "))

if n<2:
    print("Not Prime")
else:
    for i in range(2, n):
        if n%i ==0:
            print("Not Prime")
            break
    else:
        print("Prime")
