def remove_duplicates(lst):
    return list(set(lst))

num = [1, 2, 3, 4, 5, 6, 5, 4, 3]
print(remove_duplicates(num))
#output: [1, 2, 3, 4, 5, 6]