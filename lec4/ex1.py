input_string = input("Enter a string:")
modifiled_string = ""
vowels = "aeiouAEIOU"
for char in input_string:
    upper_char = char.upper()
    if upper_char in vowels:
       modifiled_string +="*"
    else:
       modifiled_string += upper_char
print("modifiled string:", modifiled_string)
