def sum_all(*args):
    for arg in args:
        print(arg)
    return sum(args)

print(sum_all(1,2,3,4,5)) # Output: 15
