# Excample list
numbers = [4, 2, 9 ,1, 5, 6]

#1. len(): get the lenght of the list
length = len(numbers)
print(f"length of the list:{length}") # output: length of the list:6

# 2. sum() calculate the sum of all elements in the list
total_sum = sum(numbers)
print(f"sum of all elements: (total_sum)")
#output: sum of all element: 27

# 3. max(): find the maximum value in the list
max_value = max(numbers)
print(f"Maximum value: (max_value)")
#output: maximum value:9

# 4 min(): find the min value in the list
min_value = min(numbers)
print(f"Minimum value: (min_value)")
# output: minimum value: 1

# 5 sorted(): Return a sorted version of the list
sorted_numbers = sorted(numbers)
print(f"sorted list: {sorted_numbers}")
#output: sorted list:[1, 2, 4, 5, 6, 9]

# 6 any(): check if any element in the list is true
bool_list = [False, True, False]
any_true = any(bool_list)
print(f"is any element true? {any_true}")
#output: is any element true? true

# 7 all(): check if all element in the list are true
all_true = all(bool_list)
print(f"are all elements true? {all_true}")
#output: are all element true false

# 8 list(): covert an iterable to a list(if not already a list)
string = "hello"
char_list = list(string)
print(f"list of characters: {char_list}")
#output: list ofcharacters: ['h', 'e', 'l', 'l', 'o']

# 9 reversed(): Return a reverse iterator of the list
reversed_numbers = list(reversed(numbers))
print(f"reversed list: {reversed_numbers}")
#output: reversed list:[6, 5, 1, 9, 2, 4,]

# 10 enumerate(): return an iterator of tuples containing index an value
enumerated_numbers = list(enumerate(numbers))
print(f"enumerated list: {enumerated_numbers}")
#output: enumerated list: [(0,4), (1,2), (2,9), (3,1), (4,5), (5,6)]