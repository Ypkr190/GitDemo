string = input("Enter a string:")
reverse_string = ""

for char in string:
    reverse_string = char + reverse_string

print("Hi")

if string.lower() == reverse_string.lower():
    print("It's a Palindrome")
else:
    print("Not a palindrome")    