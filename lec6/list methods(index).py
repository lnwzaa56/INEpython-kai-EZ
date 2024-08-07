#Using index() to fine the first occurrence of "dog"
animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot"]
first_dog_index = animals.index("dog")
print(f"the first occurrence of 'dog' is at index:{first_dog_index}")

#output: the first occurrence of "dog" is at index: 1

#using index()to find the second occurrence of "dog"
second_dog_index = animals.index("dog", first_dog_index + 1)
print(f"The second occurrence of 'dog' is at index: {second_dog_index}")
#output: the second occurrence of 'dog' is at index:4