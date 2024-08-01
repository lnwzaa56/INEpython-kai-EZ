counter = 0

def increment():
    global counter
    counter += 1

#calling the function
increment()
increment()

# Accessing the modifiled global variable
print(counter) # Output 2
