# using with statement to open and close a file
with open ("example.txt", "r") as file:
    contents = file.read()
    print(contents)
#no need to explicitly close the file