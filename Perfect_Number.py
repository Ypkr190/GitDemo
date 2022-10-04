n=int(input("Enter a number:"))
Sum=0
for i in range(1,n):
    if n%i==0:
        Sum+=i

if Sum==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")