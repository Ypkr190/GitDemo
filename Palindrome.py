string = input("Enter a string:")
reverse_string = ""

for char in string:
    reverse_string = char + reverse_string


if string.lower() == reverse_string.lower():
    print("Palindrome")
else:
    print("Not a palindrome")    