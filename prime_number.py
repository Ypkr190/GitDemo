n = int(input("Enter a number"))
fact = 0

for i in range(2,n):
    if n%i == 0:
        fact = fact+1 

if fact == 0:
    print("Prime number")
else:
    print("Not a prime number")   