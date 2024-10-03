#from functools import reduce
# reduce(function, iterable)

from functools import reduce

number = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y,number)
print(sum_of_numbers)