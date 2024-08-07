# slicing a list
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#slicing from index 2 to 5
print(numbers[2:6]) #output [2, 3, 4, 5]

# slicing with step
print(numbers[1:8:2]) #output: [1, 3, 5, 7]

#slicing from start to position
print(numbers[:4]) #output: [0, 1, 2, 3]

#slicing from a position to the end
print(numbers[6:1]) #output: [6, 7, 8, 9]
