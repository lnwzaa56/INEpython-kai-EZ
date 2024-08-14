#Adding and removing items
fruits = {"apple", "banana","cherry", "apple"}

fruits.add("orange")
print(fruits) #output: {"apple","banana","cherry","orange"}

fruits.remove("banana")
print(fruits) #output: {"apple","cherry","orange"}

fruits.remove("grape")
print(fruits) #output: {"apple","cherry","orange"} (no error raised)

remove_item = fruits.pop()
print(remove_item)
print(fruits)
# output: {"cherry","orange"} (an arbitrary item remove)

fruits.clear()
print(fruits) #output: set() (empty set)
