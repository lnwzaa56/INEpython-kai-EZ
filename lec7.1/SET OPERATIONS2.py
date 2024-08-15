set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

#Union
union_set = set1 | set2
print("Union:", union_set) #output: {1, 2, 3, 4, 5, 6}

# Intersection
intersection_set = set1 & set2
print("intersection:",intersection_set) #output: {3, 4}

difference_set = set1 - set2
print("difference:", difference_set) #output: {1,2}

# Symmetric Difference
sym_diff_set = set1 ^ set2
print("symmetric difference:", sym_diff_set)
#output: {1, 2, 5, 6} 