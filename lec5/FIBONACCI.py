def fibonacci(n):
    if n ==0 :
       return 0 #base case
    elif n == 1:
        return 1 #base case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) #Recursive case
 #Example usage   
print(fibonacci(6)) # Output: 8
    