fruits_with_duplicates = ["apple", "banana", "apple", "cherry", "apple", "kiwi", "apple", "strawberry"]


apple_position =[]
index = 0
for fruit in fruits_with_duplicates:
    if fruit == 'apple':
       apple_position.append(index)
    index = index+1

fruits_with_duplicates.pop(apple_position[-1])
fruits_with_duplicates.pop(apple_position[0])
print(f"Fruits after remove: {fruits_with_duplicates}")
