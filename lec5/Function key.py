def print_all(*args):
    for index, arg in enumerate(args):
        print(f"Argrument{index + 1}: {arg}")


#Example usage
print("python", 3.8, True , [1,2,3],{"key":"value"})
